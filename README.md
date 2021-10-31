# hisat2ENSEMBL

```

             __  ___________ ___  _________ 
            / / / /  _/ ___//   |/_  __/__ \
           / /_/ // / \__ \/ /| | / /  __/ /
          / __  // / ___/ / ___ |/ /  / __/ 
         /_/ /_/___//____/_/  |_/_/  /____/ 
                                            
    _______    ______________  __________  _______   ________
   / ____/ |  / / ____/ __ \ \/ /_  __/ / / /  _/ | / / ____/
  / __/  | | / / __/ / /_/ /\  / / / / /_/ // //  |/ / / __  
 / /___  | |/ / /___/ _, _/ / / / / / __  // // /|  / /_/ /  
/_____/  |___/_____/_/ |_| /_/ /_/ /_/ /_/___/_/ |_/\____/   
                                                             

---------------------------------------------------------------------------
- Thread : 10
- Index Path : 2.HISAT2REF/
- Sample Path : 3.SAMPLE/
- Sample % : sampled05%
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
│   ├── sample_1.fastq
│   └── sample_2.fastq
├── 4.HISAT2MAP # MAP DIR
│   ├── sampled01%
│   ├── logs
│   ├── results.csv
│   └── SAM
├── hisat2map.py # HISAT2 MAPPING
├── hisat2ref.py # HISAT2 INDEX
├── LICENSE
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

- hisat2map.py

```
$ python3 hisat2map.py -t 4 --per sampled10% #example
```
```
$ python3 hisat2map.py --help

usage: hisat2map.py [-h] [-t THREAD] [-i INDEX_PATH] [-s SAMPLE_PATH] --per SAMPLE_RATE [--save] [--no-save] [--version]

HISAT2 MAPPING ENSEMBL ENTIRE SPECIES SCRIPT

optional arguments:
  -h, --help            show this help message and exit
  -t THREAD, --thread THREAD
                        Launch NTHREADS parallel build threads
  -i INDEX_PATH, --index INDEX_PATH
                        Directory path HISAT2 index files stored
  -s SAMPLE_PATH, --sample SAMPLE_PATH
                        Directory path Sample files stored
  --per SAMPLE_RATE     Sample rate ( e.g. sampled10%, sampled5%, sampled05% )
  --save                Mapping Rate Result CSV file save (Default : save)
  --no-save             Mapping Rate Result CSV file do not save
  --version             show program's version number and exit
```

## Mapping Rate CSV file Save

- tidydata.py # result.csv

## Client S/W

