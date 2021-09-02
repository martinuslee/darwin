import os
from multiprocessing import Pool
import glob
import subprocess
import pprint
import time

def something(args):
    ref, species = args
    cmd = "mkdir 2.HISAT2REF/"+ species + " && " + "hisat2-build -p 4 " + ref + ' 2.HISAT2REF/' + species + '/' + species
    os.system(cmd)

#data = subprocess.check_output('ls -al', shell = True)
if __name__ == '__main__':
    start = time.time()  # 시작 시간 저장
    pool = Pool(10)

    path = '1.NCBI//*.fa' # fasta file path
    dir_path  = '1.NCBI//' # fasta file dir path 

    fasta = glob.glob(path) # get fasta path with file names
    fasta.sort() # sort A-Z 

    base_ref = os.listdir(dir_path) # get basename 
    base_ref = [(i.split('.')[0]) for i in base_ref] # split list and get species name
    base_ref.sort() # sort A-Z

    #pprint.pprint(base_ref) #test print list 
    #print(len(base_ref)) # 309 get the number of list elements

    args = zip(fasta, base_ref) #zip [(fasta path, basename), (), (), ...]
    pool.map(something, args)  # function and args
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
    