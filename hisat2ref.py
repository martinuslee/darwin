####################################################################################
#                                                                                  #
#                                    HISAT2NCBI                                    #
#                           implemented by Jongheon lee                            #
#                     https://github.com/martinuslee/hisat2ncbi                    #
#                                                                                  #
####################################################################################

import os
import argparse
from multiprocessing import Pool
import glob
import time

# instance generate
parser = argparse.ArgumentParser(
    description='HISAT2 INDEXING NCBI ENTIRE SPECIES SCRIPT')

# argument enrollment
parser.add_argument("-t", '--thread', dest='thread', type=str, default=1, action="store",
                    help='Launch NTHREADS parallel build threads')

args = parser.parse_args()
print(args.thread)

def getIndex(args_f):
    ref, species = args_f  # ref : fasta, species : species name
    cmd = "mkdir 2.HISAT2REF/" + species + " && " + "hisat2-build -p " + \
        args.thread + " " + ref + ' 2.HISAT2REF/' + species + '/' + species
    print(cmd)

#data = subprocess.check_output('ls -al', shell = True)
if __name__ == '__main__':
    start = time.time()  # 시작 시간 저장
    pool = Pool(10)

    path = '1.NCBI/*.fa'  # fasta file path
    dir_path = '1.NCBI/'  # fasta file dir path

    fasta = glob.glob(path)  # get fasta path with file names
    fasta.sort()  # sort A-Z

    base_ref = os.listdir(dir_path)  # get basename
    base_ref = [(i.split('.')[0])
                for i in base_ref]  # split list and get species name
    base_ref.sort()  # sort A-Z

    # pprint.pprint(base_ref) #test print list
    # print(len(base_ref)) # 310 get the number of list elements

    args_f = zip(fasta, base_ref)  # zip [(fasta path, basename), (), (), ...]
    pool.map(getIndex, args_f)  # function and args
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
