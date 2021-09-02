import os
from multiprocessing import Pool
import glob
import subprocess
import pprint

def something(args):
    ref, species = args
    cmd = "hisat2-build -p 8 " + ref + ' ' + species
    print(cmd)

#data = subprocess.check_output('ls -al', shell = True)

if __name__ == '__main__':
    pool = Pool(8)

    path = './1.ncbi/*.fa' # fasta file path
    dir_path  = './1.ncbi/' # fasta file dir path 

    fasta = glob.glob(path) # get fasta path with file names
    fasta.sort() # sort A-Z 

    base_ref = os.listdir(dir_path) # get basename 
    base_ref = [ (i.split('.')[0]) for i in base_ref] # split list and get species name
    base_ref.sort() # sort A-Z

    pprint.pprint(base_ref) #test print list 
    print(len(base_ref)) # 309 get the number of list elements

    args = zip(fasta, base_ref) #zip [(fasta path, basename), (), (), ...]
    pool.map(something, args)  # function and args
