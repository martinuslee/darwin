import os
import io
import csv 

# example path '4.HISAT2MAP/sampled10%/logs/'

def getMapRate(path):
    
    mapRate = []
    f_file = [path + log for log in os.listdir(path)]

    for log in f_file:
        with open(log, 'r') as f:
            for rate in f.readlines():
                 if "overall alignment rate" in rate:
                     mapRate.append(rate.replace(" overall alignment rate\n",""))

    csv_file = path + "results.csv"
    with open(csv_file, 'w') as f:
        writer = csv.writer(f)
        for val in mapRate:
            writer.writerow([val])
