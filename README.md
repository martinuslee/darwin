# hisat2ncbi

## discription

```
pip install glob2
pip install figlet
```

## Build Reference File 

- hisat2ref.py

## Sample file mapping

- hisat2map.py

```
python3 hisat2map.py -t 4 --per sampled10% #example
python3 hisat2map.py -h

usage: hisat2map.py [-h] [-t THREAD] [-i INDEX_PATH] [-s SAMPLE_PATH] [--per SAMPLE_RATE] [--version]

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
  --version             show program's version number and exit
```