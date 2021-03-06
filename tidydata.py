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
                     mapRate.append([os.path.basename(log).split('.')[0], rate.replace("% overall alignment rate\n","")])


    ### save csv
    csv_file = path + "results.csv"

    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['species', 'mapping_rate'])
        for name, val in mapRate:
            #name = os.path.basename(name).split('.')[0]
            writer.writerow([name, val])
    return mapRate
