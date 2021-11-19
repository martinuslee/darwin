#! /usr/bin/env python3.8.10
####################################################################################
#                                                                                  #
#                                    HISAT2ENSEMBL                                 #
#                           implemented by Jongheon lee                            #
#                     https://github.com/martinuslee/hisat2ENSEMBL                 #
#                                                                                  #
####################################################################################

import os
import sys
import argparse
import multiprocessing as mp
import subprocess
import concurrent.futures
from glob import glob
from functools import partial
import time
from pyfiglet import Figlet
from tidydata import getMapRate  # custom function
from termcolor import colored
import taxonomy


####################################################################################
# instance generate
parser = argparse.ArgumentParser(
    description='HISAT2 MAPPING ENSEMBL ENTIRE SPECIES SCRIPT')

# argument enrollment
parser.add_argument("-t", '--thread', dest='thread', type=str, default='1', action="store",
                    help='Launch NTHREADS parallel build threads')
parser.add_argument("-i", '--index', dest='index_path', type=str, default='2.HISAT2REF/', action="store",
                    help='Directory path HISAT2 index files stored')
parser.add_argument("-s", '--sample', dest='sample_path', type=str, default='3.SAMPLE/', action="store",
                    help='Directory path Sample files stored')
parser.add_argument('--name', dest='sample_name', type=str, action="store",
                    help='Sample file name', required=True)
parser.add_argument('--per', dest='sample_rate', type=str, default='', action="store",
                    help='Sample rate ( e.g. sampled10%%, sampled5%%, sampled05%% )', required=True)  # required option

parser.add_argument('--save', dest='save', action='store_true',
                    help="Mapping Rate Result CSV file save (Default : save)")
parser.add_argument('--no-save', dest='save', action='store_false',
                    help="Mapping Rate Result CSV file do not save")
parser.set_defaults(save=True)

parser.add_argument('--version', action='version', version='%(prog)s 1.0')
args = parser.parse_args()

f = Figlet(font='slant')
#print(f.renderText('* * * * * * * * *'))
print(colored(f.renderText('    DARWIN'), 'cyan'))
#print(f.renderText('* * * * * * * * *'))

print(f"---------------------------------------------------------------------------")
print(f"- Thread : {args.thread}")
print(f"- Index Path : {args.index_path}")
print(f"- Sample Path : {args.sample_path}")
print(f"- Sample % : {args.sample_rate}")
print(f"- Save Result csv : {args.save}")
print(f"---------------------------------------------------------------------------")

####################################################################################
# global variables
# order = {
#     'Chelydra_serpentina': ['Chelonoidis_abingdonii', 'Gopherus_agassizii', 'Salvator_merianae','Crocodylus_porosus','Laticauda_laticaudata','Pogona_vitticeps','Pelodiscus_sinensis','Chelydra_serpentina','Podarcis_muralis','Pseudonaja_textilis','Gopherus_evgoodei','Anolis_carolinensis','Naja_naja','Varanus_komodoensis','Notechis_scutatus','Chrysemys_picta_bellii','Terrapene_carolina_triunguis','Sphenodon_punctatus','Pelusios_castaneus'],
#     'Carnivora': ['Vulpes_vulpes', 'Zalophus_californianus', 'Ailuropoda_melanoleuca', 'Suricata_suricatta'],
#     'Danio_rerio': ['Acanthochromis_polyacanthus', 'Amphilophus_citrinellus', 'Amphiprion_ocellaris', 'Amphiprion_percula', 'Anabas_testudineus'],
#     #'Sus_scrofa': ["Ursus_maritimus", "Vulpes_vulpes", "Ovis_aries_rambouillet"],
#     'Gallus_gallus': ['Accipiter_nisus', 'Amazona_collaria', 'Anas_platyrhynchos', 'Coturnix_japonica','Taeniopygia_guttata', 'Struthio_camelus_australis', 'Zosterops_lateralis_melanops', 'Zonotrichia_albicollis'],
#     #'Mus_musculus': ["Mus_spretus", "Marmota_marmota_marmota", "Castor_canadensis"],
#     #'Homo_sapiens': ["Colobus_angolensis_palliatus", "Rhinopithecus_bieti", "Saimiri_boliviensis_boliviensis",'Pan_paniscus','Otolemur_garnettii','Cebus_capucinus','Pan_troglodytes','Propithecus_coquereli','Macaca_fascicularis','Mandrillus_leucophaeus','Theropithecus_gelada','Nomascus_leucogenys','Rhinopithecus_roxellana','Gorilla_gorilla','Prolemur_simus','Aotus_nancymaae','Macaca_mulatta','Callithrix_jacchus','Microcebus_murinus','Papio_anubis','Pongo_abelii','Macaca_nemestrina','Cercocebus_atys','Carlito_syrichta','Piliocolobus_tephrosceles','Chlorocebus_sabaeus'],
#     'Homo_sapiens': ["Colobus_angolensis_palliatus", "Rhinopithecus_bieti"],
#     #'Others': ['Latimeria chalumnae', 'Callorhinchus milii', 'Eptatretus burgeri', 'Petromyzon marinus', 'Ciona intestinalis', 'Ciona savignyi', 'Caenorhabditis elegans', 'Drosophila melanogaster', 'Saccharomyces cerevisiae','Vombatus_ursinus','Phascolarctos_cinereus','Monodelphis_domestica' ,'Ornithorhynchus_anatinus','Sarcophilus_harrisii','Notamacropus_eugenii']
# }

sam_dir = '4.HISAT2MAP/' + args.sample_name + '/' + args.sample_rate + '/'
directory = sam_dir + 'logs/'
if not os.path.exists(sam_dir):  # if there is not a directory..
    os.makedirs(directory)
    os.makedirs(sam_dir + 'SAM/')


def getMapped(list):
    indexFile, f1, f2 = list  # ref : fasta, species : species name
    try:
        basename = indexFile.split('/')[1]
        cmd = "time hisat2 -p " + args.thread + " " + indexFile + \
            " -1 " + f1 + " -2 " + f2 + " -S " + sam_dir + 'SAM/' + basename + ".sam 1> " + \
            directory + basename + ".log 2>> " + directory + \
            basename + ".log"  # HISAT2 command line
        #cmd = ["time", "hisat2", "-p", args.thread, indexFile, "-1", f1, +'-2', f2, "-S", sam_dir, "SAM/", basename, ".sam", "1>", directory, basename, ".log", "2>>", directory, basename, ".log"]
        subprocess.run(cmd, shell=True)  # RUN!! ####
        # print(cmd)  # test
    except OSError:
        print('Error: Creating directory. ' + directory)


if __name__ == '__main__':

    start = time.time()  # set timer to check execution time
    real_start = start

    def makeRefPath(ref_list):
        try:
            dirList = [args.index_path + species for species in ref_list]
            # dirList = glob(args.index_path + '*/')  # get sub directories
            # get sub dir with basename of index files
            dirList = [path + "/" + path.split('/')[1] for path in dirList]
            dirList.sort()  # sort A-Z
            # print(dirList)
            if(args.sample_path[-1] != '/'):
                args.sample_path += '/'
            # print(f'{args.sample_path}{args.sample_name}/{args.sample_rate}_*.fastq')
            fastq1, fastq2 = sorted(
                glob(f'{args.sample_path}{args.sample_name}/{args.sample_rate}_*.fastq'))
            # print(fastq1,fastq2)
            return dirList, fastq1, fastq2
        except ValueError as e:
            print(" Wrong sample percentage input check --per option \n", e)

    dirList, fastq1, fastq2 = makeRefPath(taxonomy._reference)

    with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
        executor.map(getMapped, [[item, fastq1, fastq2]
                                 for item in dirList], chunksize=20000)

    print(" - HISAT2 execution time :", time.time() - start)

    orderResult = list()
    if args.save:
        start = time.time()  # set timer to check execution time
        orderResult = getMapRate(sam_dir)
        orderResult = dict(orderResult)

        print("CSV execution time :", time.time() - start)

    dicts = dict(filter(lambda x: x[1] > '0.00%', orderResult.items()))
    print(dicts)
    
    if not dicts:
        sys.exit('empty')

    else:
        max_species = max(orderResult, key=lambda x: float(orderResult[x]))
        print(max_species)
        print('not empty')
        print(taxonomy._order[max_species])
        dirList, fastq1, fastq2 = makeRefPath(taxonomy._order[max_species])

        with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
            executor.map(getMapped, [[item, fastq1, fastq2]
                                    for item in dirList], chunksize=20000)

    print(" - HISAT2 execution time :", time.time() - real_start)
    getMapRate(sam_dir)

    if args.save:
        start = time.time()  # set timer to check execution time
        orderResult = getMapRate(sam_dir)
        orderResult = dict(orderResult)

        print("CSV execution time :", time.time() - start)

    dicts = dict(filter(lambda x: x[1] > '0.00%', orderResult.items()))
    print(dicts)
    
    if not dicts:
        #dirList, fastq1, fastq2 = makeRefPath(taxonomy._family['Others'])
        sys.exit('empty')

    else:
        try:
            max_species = max(orderResult, key=lambda x: float(orderResult[x]))
            print(max_species)
            print('not empty')
            print(taxonomy._family[max_species])
            dirList, fastq1, fastq2 = makeRefPath(taxonomy._family[max_species])

            with concurrent.futures.ThreadPoolExecutor(max_workers=None) as executor:
                executor.map(getMapped, [[item, fastq1, fastq2]
                                        for item in dirList], chunksize=20000)
            print(" - HISAT2 execution time :", time.time() - real_start)
            getMapRate(sam_dir)

        except KeyError:
            sys.exit("Doesn't match any family")

