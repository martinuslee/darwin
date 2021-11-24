# DARWIN - Data Alignment of RNA-seq for Web-based Interspecies Navigator

```
             ____  ___    ____ _       _______   __
            / __ \/   |  / __ \ |     / /  _/ | / /
           / / / / /| | / /_/ / | /| / // //  |/ / 
          / /_/ / ___ |/ _, _/| |/ |/ // // /|  /  
         /_____/_/  |_/_/ |_| |__/|__/___/_/ |_/   
                                                   

---------------------------------------------------------------------------
- Thread : 32
- Index Path : 2.HISAT2REF/
- Sample Path : 3.SAMPLE/
- Sample % : r10
- Save Result csv : True
---------------------------------------------------------------------------
```

## Copyright

:copyright: ABCLab Jongheon Lee

## Requirement

```
$ pip install glob2
$ pip install figlet
```

## Structure

```
.
├── 1.ENSEMBL # FASTA DATA FROM ENSEMBL
│   ├── Acanthochromis_polyacanthus.ASM210954v1.dna.toplevel.fa
│   ├── ...
│   └── Zosterops_lateralis_melanops.ASM128173v1.dna.toplevel.fa
├── 2.HISAT2REF # INDEX DIR
│   ├── Acanthochromis_polyacanthus
│   ├── ...
│   └── Zosterops_lateralis_melanops
├── 3.SAMPLE # SAMPLE DIR
│   ├── r10_sample_1.fastq
│   └── r10_sample_2.fastq
├── 4.HISAT2MAP # MAP DIR
│   ├── logs
│   ├── results.csv
│   └── SAM
├── hisat2map.py # HISAT2 MAPPING
├── darwin.py # HISAT2 MAPPING - main script
├── hisat2ref.py # HISAT2 INDEX
├── taxonomy.py # TAXONOMY SPECIES INFO 
├── LICENSE
├── seqchop.py # CLIENT S/W PyQt5
├── preprocessing_fastq.ipynb # BIOPYTHON SAMPLING Fastq SAMPLE
├── __pycache__
├── README.md
└── tidydata.py # To build CSV result file.
```

## Build Reference File 

- hisat2ref.py

```
$ python3 hisat2ref.py -t 4 -p 1.NCBI/ -o 2.HISAT2REF/
```
```
$ python3 hisat2ref.py -h

usage: hisat2ref.py [-h] [-t THREAD] [-p PATH] [-o OUTDIR]

HISAT2 INDEXING ENSEMBL ENTIRE SPECIES SCRIPT

optional arguments:
  -h, --help            show this help message and exit
  -t THREAD, --thread THREAD
                        Launch NTHREADS parallel build threads
  -p PATH, --path PATH  Directory path ENSEMBL Refernce fasta files stored
  -o OUTDIR, --outdIr OUTDIR
                        HISAT2 Output Directory path
```

## Sample file mapping

- darwin.py

```
$ python3 darwin.py -t 32 --name Homo_sapiens --per r10 #example
```
```
$ python3 darwin.py -h

usage: darwin.py [-h] [-t THREAD] [-i INDEX_PATH] [-s SAMPLE_PATH] --name SAMPLE_NAME --per SAMPLE_RATE [--save] [--no-save] [--version]

DARWIN : Data Alignment of RNA-seq for Web-based Interspecies Navigator - HISAT2 MAPPING ENSEMBL ENTIRE SPECIES SCRIPT

optional arguments:
  -h, --help            show this help message and exit
  -t THREAD, --thread THREAD
                        Launch NTHREADS parallel build threads
  -i INDEX_PATH, --index INDEX_PATH
                        Directory path HISAT2 index files stored
  -s SAMPLE_PATH, --sample SAMPLE_PATH
                        Directory path Sample files stored
  --name SAMPLE_NAME    Sample file name
  --per SAMPLE_RATE     the number of reads ( e.g. r50, r10, r1 )
  --save                Mapping Rate Result CSV file save (Default : save)
  --no-save             Mapping Rate Result CSV file do not save
  --version             show program's version number and exit
```

## Mapping Rate CSV file Save

- tidydata.py # result.csv

## Client S/W

- seqchop.py


