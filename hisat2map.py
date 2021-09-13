#! /usr/bin/env python3.8.10
####################################################################################
#                                                                                  #
#                                    HISAT2ENSEMBL                                 #
#                           implemented by Jongheon lee                            #
#                     https://github.com/martinuslee/hisat2ENSEMBL                 #
#                                                                                  #
####################################################################################

import os
import argparse
from multiprocessing import Pool
from glob import glob
from functools import partial
import time
from pyfiglet import Figlet
from tidydata import getMapRate #custom function


####################################################################################
# instance generate
parser = argparse.ArgumentParser(
    description='HISAT2 MAPPING ENSEMBL ENTIRE SPECIES SCRIPT')

# argument enrollment
parser.add_argument("-t", '--thread', dest='thread', type=str, default='1', action="store",
                    help='Launch NTHREADS parallel build threads')
parser.add_argument("-i", '--index', dest='index_path', type=str, default='2.HISAT2REF/', action="store",
                    help='Directory path HISAT2 index files stored')
parser.add_argument("-s", '--sample', dest='sample_path', type=str, default='3.SAMPLE/', action="store",
                    help='Directory path Sample files stored')
parser.add_argument('--per', dest='sample_rate', type=str, default='', action="store",
                    help='Sample rate ( e.g. sampled10%%, sampled5%%, sampled05%% )', required=True)  # required option

parser.add_argument('--save', dest='save', action='store_true', help="Mapping Rate Result CSV file save (Default : save)")
parser.add_argument('--no-save', dest='save', action='store_false', help="Mapping Rate Result CSV file do not save")
parser.set_defaults(save=True)

parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

f = Figlet(font='slant')
#print(f.renderText('* * * * * * * * *'))
print(f.renderText('\n    HISAT2\nEVERYTHING'))
#print(f.renderText('* * * * * * * * *'))

print(f"---------------------------------------------------------------------------")
print(f"- Thread : {args.thread}")
print(f"- Index Path : {args.index_path}")
print(f"- Sample Path : {args.sample_path}")
print(f"- Sample % : {args.sample_rate}")
print(f"- Save Result csv : {args.save}")
print(f"---------------------------------------------------------------------------")

####################################################################################
# global variables
sam_dir = '4.HISAT2MAP/' + args.sample_rate + '/'
directory = sam_dir +'logs/'
def getMapped(indexFile, f1, f2):
    # indexFile, f1, f2 = args_f  # ref : fasta, species : species name
    try:
        if not os.path.exists(sam_dir):  # if there is not a directory..
            os.makedirs(directory)
            os.makedirs(sam_dir + 'SAM/')
        basename = indexFile.split('/')[1]
        cmd = "time hisat2 -p " + args.thread + " --rna-strandness RF -x " + indexFile + \
            " -1 " + f1 + " -2 " + f2 + " -S " + sam_dir + 'SAM/' + basename + ".sam 1> " + \
            directory + basename + ".log 2>> " + directory + \
            basename + ".log"  # HISAT2 command line
        
        os.system(cmd)  #### RUN!! ####
        #print(cmd)  # test
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

    start = time.time()  # set timer to check execution time
    pool = Pool(30)  # Core 수에 맞게 돌아감
    try:
        dirList = glob(args.index_path + '*/')  # get sub directories
        # get sub dir with basename of index files
        dirList = [path + path.split('/')[1] for path in dirList]
        dirList.sort()  # sort A-Z

        fastq1, fastq2 = glob('3.SAMPLE/' + args.sample_rate + '*.fastq')
    except ValueError as e:
        print(" Wrong sample percentage input check --per option \n", e) 

    pool.starmap_async(getMapped, [[item, fastq1, fastq2] for item in dirList])
    pool.close()
    pool.join()
    # current time - start time  = sys time
    print("HISAT2 execution time :", time.time() - start)


    if args.save: 
        start = time.time()  # set timer to check execution time
        getMapRate(sam_dir)
        print("CSV execution time :", time.time() - start)
