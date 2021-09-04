# hisat2ncbi

## Requirement

```
$ pip install glob2
$ pip install figlet
```

## Build Reference File 

- hisat2ref.py

```
$ python3 hisat2ref.py -t 4 -p 1.NCBI/ -o 2.HISAT2REF/
$ python3 hisat2ref.py -h
usage: hisat2ref.py [-h] [-t THREAD] [-p PATH] [-o OUTDIR]

HISAT2 INDEXING NCBI ENTIRE SPECIES SCRIPT

optional arguments:
  -h, --help            show this help message and exit
  -t THREAD, --thread THREAD
                        Launch NTHREADS parallel build threads
  -p PATH, --path PATH  Directory path NCBI Refernce fasta files stored
  -o OUTDIR, --outdIr OUTDIR
                        HISAT2 Output Directory path
```

## Sample file mapping

- hisat2map.py

```
$ python3 hisat2map.py -t 4 --per sampled10% #example
$ python3 hisat2map.py --help

usage: hisat2map.py [-h] [-t THREAD] [-i INDEX_PATH] [-s SAMPLE_PATH] --per SAMPLE_RATE [--save] [--no-save] [--version]

HISAT2 MAPPING NCBI ENTIRE SPECIES SCRIPT

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

- tidydata.py


