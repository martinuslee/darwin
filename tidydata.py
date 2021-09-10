#! /usr/bin/env python3.8.10
####################################################################################
#                                                                                  #
#                                    HISAT2ENSEMBL                                 #
#                           implemented by Jongheon lee                            #
#                     https://github.com/martinuslee/hisat2ENSEMBL                 #
#                                                                                  #
####################################################################################

import os
import csv 

# example path '4.HISAT2MAP/sampled05%/logs/'

def getMapRate(path):
    log_dir = path + 'logs/' # dir path where map log files saved
    mapRate = []

    ### read logs 
    # get % values
    f_file = [log_dir + log for log in os.listdir(log_dir)] # logs
    f_file.sort()
    for log in f_file:
        with open(log, 'r') as f:
            for rate in f.readlines():
                 if "overall alignment rate" in rate:
                     mapRate.append([log, rate.replace(" overall alignment rate\n","")])


    ### save csv
    csv_file = path + "results.csv"

    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        for name, val in mapRate:
            name = name.split('/')[3].split('.')[0]
            writer.writerow([name, val])


