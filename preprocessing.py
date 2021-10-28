from Bio import SeqIO
import random

#len(identifiers)

sample = input() # SRR1758114_1.fastq

#File Read
records , records_2= list(SeqIO.parse(f"3.SAMPLE/{sample}","fastq")), list(SeqIO.parse(f"3.SAMPLE/{sample}","fastq"))

index = list(range(1,len(records)+1))

sampleIdx = sorted(random.sample(index, 10))

print(sampleIdx)

sampleRecords, sampleRecords_2 = [], []
for i in sampleIdx:
    sampleRecords.append(records[i])
    sampleRecords_2.append(records_2[i])

# File Write
SeqIO.write(sampleRecords, f'3.SAMPLE/Coturnix_japonica/test_r10_SRR1758114_1.fastq', "fastq")
SeqIO.write(sampleRecords_2, f'3.SAMPLE/Coturnix_japonica/test_r10_SRR1758114_2.fastq', "fastq")