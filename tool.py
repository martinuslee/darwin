import os
import argparse
from multiprocessing import Pool
from glob import glob
from functools import partial
import time
from pyfiglet import Figlet
from tidydata import getMapRate #custom function
from preprocessing import sampling
#from hisat2ref import getIndex
from hisat2map import getMapped

# instance generate
parser = argparse.ArgumentParser(description='HISAT2 ENSEMBL ENTIRE SPECIES SCRIPT')

# argument enrollment
# Mode 
parser.add_argument("-M", '--mode', dest='mode', type=int, default=1, action="store",
                    help='Execution Mode (Index = 1, MAP = 2, SAMPING = 3)', required=True)
# Thread
parser.add_argument("-t", '--thread', dest='thread', type=str, default='1', action="store",
                    help='Launch NTHREADS parallel build threads')
# ENSEMBL DB PATH
parser.add_argument("-p", '--path', dest='path', type=str, default='1.ENSEMBL/', action="store",
                    help='Directory path ENSEMBL Refernce fasta files stored')
# HISAT2 OUTPUT PATH
parser.add_argument("-o", '--outdIr', dest='outdir', type=str, default='2.HISAT2REF/', action="store",
                    help='HISAT2 Output Directory path')
# HISAT2 INDEX PATH
parser.add_argument("-i", '--index', dest='index_path', type=str, default='2.HISAT2REF/', action="store",
                    help='Directory path HISAT2 index files stored')
# SAMPLE DIR PATH
parser.add_argument("-s", '--sample', dest='sample_path', type=str, default='3.SAMPLE/', action="store",
                    help='Directory path Sample files stored')
# FASTQ1
parser.add_argument('--fastq1', dest='sample1', type=str, default='', action="store",
                    help='fastq sameple')  
# FASTQ2
parser.add_argument('--fastq2', dest='sample2', type=str, default='', action="store",
                    help='fastq sameple')  
# SAMPLE RATE
parser.add_argument('--per', dest='sample_rate', type=str, default='', action="store",
                    help='Sample rate ( e.g. sampled10%%, sampled5%%, sampled05%% )')  
# CSV SAVE
parser.add_argument('--save', dest='save', action='store_true', help="Mapping Rate Result CSV file save (Default : save)")
parser.add_argument('--no-save', dest='save', action='store_false', help="Mapping Rate Result CSV file do not save")
parser.set_defaults(save=True)
# VERSION
parser.add_argument('--version', action='version', version='%(prog)s 1.0')

args = parser.parse_args()


f = Figlet(font='slant')
#print(f.renderText('* * * * * * * * *'))
print(f.renderText('    HISAT2\nEVERYTHING'))
#print(f.renderText('* * * * * * * * *'))

print("---------------------------------------------------------------------------")
print("                         ENSEMBL Release-104")
print("                     HISA2 INDEX Build - Sep 04th 2021")
print("---------------------------------------------------------------------------")
print(f"- Mode : {args.mode}")
print(f"- Thread : {args.thread}")
print(f"- Reference Path : {args.path}")
print(f"- Output Directory Path : {args.outdir}")
print(f"- Index Path : {args.index_path}")
print(f"- Sample Path : {args.sample_path}")
print(f"- Sample % : {args.sample_rate}")
print(f"- Save Result csv : {args.save}")
print(f"---------------------------------------------------------------------------")


if __name__ == "__main__":

    start = time.time()  # 시작 시간 저장
    pool = Pool(10)
    if args.mode == 1:

        # path = '1.NCBI/*.fa'  # fasta file path
        path = args.path + '/*.fa'  # fasta file path
        # dir_path = '1.NCBI/'  # fasta file dir path
        dir_path = args.path  # fasta file dir path

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
        
    elif args.mode == 2:

        args.sample_rate = str(args.sample_rate)
        sam_dir = '4.HISAT2MAP/' + args.sample_rate + '/'
        directory = sam_dir +'logs/'

        dirList = glob(args.index_path + '*/')  # get sub directories
        # get sub dir with basename of index files
        dirList = [path + path.split('/')[1] for path in dirList]
        dirList.sort()  # sort A-Z

        fastq1, fastq2 = glob('3.SAMPLE/' + args.sample_rate + '*.fastq')

        pool.starmap(getMapped, [[item, fastq1, fastq2, sam_dir, directory, args.thread] for item in dirList])
        pool.close()
        pool.join()

        # current time - start time  = sys time
        print("HISAT2 execution time :", time.time() - start)

        if args.save: 
            start = time.time()  # set timer to check execution time
            getMapRate(sam_dir)
            print("CSV execution time :", time.time() - start)
        
    else:
        fastq1, fastq2 = args.sample1, args.sample2
        sampling(args.sample_path, fastq1, fastq2, args.sample_rate)
        print("this is test")
