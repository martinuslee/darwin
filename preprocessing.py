from Bio import SeqIO
import random

#"3.SAMPLE/SRR1758114_2.fastq"
def sampling(path, origin1, origin2, per):
    per = float(per)
    per = per/100.0 # percentage to float 10% == 0.1
    records = list(SeqIO.parse(path + origin1,"fastq"))
    records_2 = list(SeqIO.parse(path + origin2,"fastq"))
    print(records[0])
    sam = int(len(records)*per) #0.1%
    sam
    index = list(range(1,len(records)+1))
    print("index length : ",len(index))
    sampleIdx = random.sample(index, sam)
    sampleIdx.sort()
    #sampleRecords

    sampleRecords=list()
    sampleRecords_2=list()
    for i in sampleIdx:
        sampleRecords.append(records[i])
        sampleRecords_2.append(records_2[i])
    per = per * 100
    int(per) if per > 0 else per
    per = str(per)
    per = per.replace(".","")
    print(path+"sampled"+ per + "%_"+origin1, "fastq")
    SeqIO.write(sampleRecords, path+"sampled"+ per + "%_"+origin1, "fastq")
    SeqIO.write(sampleRecords_2, path+"sampled"+ per + "%_"+origin2, "fastq")

sampling('3.SAMPLE/', 'SRR1758114_1.fastq','SRR1758114_2.fastq', 0.00005)
