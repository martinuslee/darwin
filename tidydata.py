####################################################################################
#                                                                                  #
#                                    HISAT2NCBI                                    #
#                           implemented by Jongheon lee                            #
#                     https://github.com/martinuslee/hisat2ncbi                    #
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
                     mapRate.append(rate.replace(" overall alignment rate\n",""))


    ### save csv
    csv_file = path + "results.csv"

    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        for val in mapRate:
            writer.writerow([val])


getMapRate('4.HISAT2MAP/sampled05%/')