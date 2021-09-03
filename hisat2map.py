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
from glob import glob
from functools import partial
import time
from pyfiglet import Figlet


####################################################################################
# instance generate
parser = argparse.ArgumentParser(
    description='HISAT2 MAPPING NCBI ENTIRE SPECIES SCRIPT')

# argument enrollment
parser.add_argument("-t", '--thread', dest='thread', type=str, default='1', action="store",
                    help='Launch NTHREADS parallel build threads')
parser.add_argument("-p", '--path', dest='index_path', type=str, default='2.HISAT2REF/', action="store",
                    help='Directory path HISAT2 index files stored')
parser.add_argument("-s", '--sample', dest='sample_path', type=str, default='3.SAMPLE/', action="store",
                    help='Directory path Sample files stored')

args = parser.parse_args()

f = Figlet(font='slant')
#print(f.renderText('* * * * * * * * *'))
print(f.renderText('   HISAT2\nEVERYTHING'))
#print(f.renderText('* * * * * * * * *'))

print(f"Thread : {args.thread}")
print(f"Index Path : {args.index_path}")
print(f"Sample Path : {args.sample_path}")

####################################################################################

def getMapped(indexFile, f1, f2):
    # indexFile, f1, f2 = args_f  # ref : fasta, species : species name
    try:
        directory = '4.HISAT2MAP/logs/'
        if not os.path.exists(directory): # if there is not a directory..
            os.makedirs(directory)
        basename  = indexFile.split('/')[1]
        cmd = "time hisat2 -p " + args.thread + " --rna-strandness RF -x " + indexFile + \
            " -1 " + f1 + " -2 " + f2 + " -S 4.HISAT2MAP/" + basename + ".sam 1> " + \
            directory + basename + ".log 2>> " +  directory + basename + ".log"# HISAT2 command line
        #os.system(cmd)  #### RUN!! ####
        #print(cmd) #test
    except OSError:
        print('Error: Creating directory. ' + directory)


####################################################################################
#
#   --rna-strandness <string>
#   Specify strand-specific information: the default is unstranded.
#   For single-end reads, use F or R.
#
####################################################################################

if __name__ == '__main__':

    start = time.time()  # 시작 시간 저장
    pool = Pool(10)  # 10개씩 돌아감
    dirList = glob(args.index_path + '*/') #get sub directories
    dirList = [path + path.split('/')[1] for path in dirList] # get sub dir with basename of index files
    dirList.sort() # sort A-Z
    
    fastq1, fastq2 = glob('3.SAMPLE/*.fastq')

    pool.starmap(getMapped, [ [item, fastq1, fastq2] for item in dirList])
    pool.close()
    pool.join()

    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    