import os
import subprocess
import sys
import glob

def getIndex(path):
    file_list = glob.glob(path)
    print(file_list)

getIndex(sys.argv[0])


