
_reference = ['Gallus_gallus','Homo_sapiens','Mus_musculus','Sus_scrofa','Suricata_suricatta']

_order = {
    # birds
    'Gallus_gallus': ['Accipiter_nisus', 'Otus_sunia','Falco_tinnunculus', 'Nothoprocta_perdicaria', 'Otus sunia', 'Strigops_habroptila', 'Corvus_moneduloides', 
                        'Coturnix_japonica', 'Anser_brachyrhynchus', 'Struthio_camelus_australis', 'Calidris_pugnax','Dromaius_novaehollandiae'],
    # primates
    'Homo_sapiens': ["Colobus_angolensis_palliatus", 'Otolemur_garnettii','Cebus_capucinus','Propithecus_coquereli',
                        'Mandrillus_leucophaeus','Theropithecus_gelada','Nomascus_leucogenys', 'Prolemur_simus',
                        'Aotus_nancymaae','Microcebus_murinus','Papio_anubis','Pongo_abelii','Macaca_nemestrina',
                        'Cercocebus_atys','Carlito_syrichta','Piliocolobus_tephrosceles','Chlorocebus_sabaeus'],
    # rodent
    'Mus_musculus' : ['Nannospalax_galili', 'Castor_canadensis', 'Jaculus_jaculus','Chinchilla_lanigera','Tupaia_belangeri',
                        'Fukomys_damarensis','Octodon_degus','Cavia_aperea','Rattus_norvegicus','Mus_spicilegus',
                        'Meriones_unguiculatus','Microtus_ochrogaster','Dipodomys_ordii','Spermophilus_dauricus','Oryctolagus_cuniculus'],    
    # Artiodactyla                     
    'Sus_scrofa' : ['Moschus_moschiferus', 'Catagonus_wagneri', 'Phocoena_sinus', 'Ovis_aries','Balaenoptera_musculus','Physeter_catodon',
                    'Tursiops_truncatus','Cervus_hanglu_yarkandensis','Monodon_monoceros'],
    # Carnivora
    'Suricata_suricatta' : ['Zalophus_californianus','Lynx_canadensis','Neovison_vison','Neovison_vison','Vulpes_vulpes','Sorex_araneus','Equus_caballus','Pteropus_vampyrus'],

    # Fish
    'Danio_rerio' : ['Larimichthys_crocea', 'Parambassis_ranga', 'Stegastes_partitus', 'Dicentrarchus_labrax', 'Lates_calcarifer', 'Myripristis_murdjan', 'Sphaeramia_orbicularis',
    'Gouania_willdenowi', 'Hippocampus_comes', 'Betta_splendens', 'Labrus_bergylta', 'Cynoglossus_semilaevis', 'Neogobius_melanostomus', 'Mastacembelus_armatus','Echeneis naucrates',
    'Mola_mola', 'Sparus_aurata','Pundamilia_nyererei']

}

'''
 Pomacentridae : Stegastes partitus
 Blenniiformes  :Gouania_willdenowi,  Salarias_fasciatus
 Osteoglossiformes : Paramormyrops_kingsleyae Scleropages_formosus
 Anabantiformes : Anabas testudineus
 Pleuronectiformes : Scophthalmus maximus
 Gobiidae : Periophthalmus_magnuspinnatus
 Synbranchiformes : Monopterus_albus
 Carangiformes : Seriola dumerili, Seriola lalandi dorsalis
 Tetraodontiformes : Tetraodon nigroviridis, Takifugu rubripes
 Cichlidae : Maylandia zebra, vertical barExpandAmphilophus citrinellus, Neolamprologus brichardi, Astatotilapia calliptera, Haplochromis burtoni, Oreochromis aureus, Oreochromis niloticus
 
'''

_family = {
    # birds 
    'Accipiter_nisus': ['Buteo_japonicus', 'Aquila_chrysaetos_chrysaetos'],
    'Otus_sunia': ['Athene_cunicularia', 'Bubo_bubo', 'Strix_occidentalis_caurina'],
    'Strigops_habroptila': ['Amazona_collaria', 'Melopsittacus_undulatus'],
    'Corvus_moneduloides': ['Manacus_vitellinus', 'Lepidothrix_coronata', 'Stachyris_ruficeps', 'Catharus_ustulatus', 'Ficedula_albicollis',
                            'Taeniopygia_guttata', 'Lonchura_striata_domestica', 'Camarhynchus_parvulus', 'Geospiza_fortis', 'Erythrura_gouldiae','Zonotrichia_albicollis', 
                            'Junco_hyemalis', 'Cyanistes_caeruleus', 'Parus_major', 'Serinus_canaria', 'Malurus_cyaneus_samueli', 'Zosterops_lateralis_melanops'],
    'Coturnix_japonica': ['Meleagris_gallopavo', 'Chrysolophus_pictus', 'Phasianus_colchicus', 'Pavo_cristatus', 'Numida_meleagris'],
    'Anser_brachyrhynchus': ['Anser_cygnoides', 'Anas_zonorhyncha', 'Anas_platyrhynchos', 'Anas_platyrhynchos_platyrhynchos', 'Cairina_moschata_domestica'],
    'Apteryx_rowi': ['Apteryx_owenii', 'Apteryx_haastii'],
    'Calidris_pugnax' : ['Calidris_pygmaea'],
    # primates
    'Pongo_abelii' : ['Pan_troglodytes','Pan_paniscus','Gorilla_gorilla'],
    'Piliocolobus_tephrosceles' : ['Rhinopithecus_roxellana','Rhinopithecus_bieti'],
    'Macaca_nemestrina' : ['Macaca_mulatta','Macaca_fascicularis'],
    'Cebus_capucinus' : ['Callithrix_jacchus','Saimiri_boliviensis_boliviensis'],
    # rodent
    'Fukomys_damarensis' : ['Heterocephalus_glaber_female','Heterocephalus_glaber_male'],
    'Cavia_aperea' : ['Cavia_porcellus'],
    'Mus_spicilegus' : ['Mus_spretus','Mus_pahari','Mus_caroli','Mus_musculus_129s1svimj','Mus_musculus_aj','Mus_musculus_akrj',
                'Mus_musculus_balbcj','Mus_musculus_c3hhej','Mus_musculus_c57bl6nj','Mus_musculus_casteij','Mus_musculus_cbaj',
                'Mus_musculus_dba2j','Mus_musculus_fvbnj','Mus_musculus_lpj','Mus_musculus_nodshiltj','Mus_musculus_nzohlltj','Mus_musculus_pwkphj','Mus_musculus_wsbeij'],

    'Microtus_ochrogaster' : ['Mesocricetus_auratus', 'Cricetulus_griseus_chok1gshd', 'Cricetulus_griseus_crigri','Cricetulus_griseus_picr', 'Peromyscus_maniculatus_bairdii'],
    'Spermophilus_dauricus' : ['Sciurus_vulgaris', 'Ictidomys_tridecemlineatus','Urocitellus_parryii','Marmota_marmota_marmota'],
    'Oryctolagus_cuniculus' : ['Ochotona_princeps'],
    # Artiodactyla
    'Ovis_aries' : ['Ovis_aries_rambouillet','Capra_hircus','Capra_hircus_blackbengal','Bos_mutus', 'Bos_grunniens' ,'Bos_indicus', 
                    'Bos_indicus_hybrid','Bos_taurus','Bos_taurus_hybrid','Bison_bison_bison','Vicugna_pacos','Camelus_dromedarius'],
    'Monodon_monoceros' : ['Delphinapterus_leucas'],
    # Carnivora
    'Lynx_canadensis' : ['Panthera_pardus','Panthera_leo','Panthera_tigris_altaica','Felis_catus'],
    'Neovison_vison' : ['Mustela_putorius_furo'],
    'Ailuropoda_melanoleuca' : ['Ursus_maritimus','Ursus_americanus','Ursus_thibetanus_thibetanus'],
    'Vulpes_vulpes' : ['Canis_lupus_dingo', 'Canis_lupus_familiaris','Canis_lupus_familiarisbasenji','Canis_lupus_familiarisgreatdane'],
    'Sorex_araneus' : ['Erinaceus_europaeus'],
    'Equus_caballus' : ['Equus_asinus_asinus'],
    'Pteropus_vampyrus' : ['Rhinolophus_ferrumequinum', 'Myotis_lucifugus']
}

'''
** birds
Accipitridae : Accipiter_nisus
Falco_tinnunculus
Nothoprocta perdicaria
Strigidae : Otus_sunia
Psittaciformes : Strigops_habroptila
Passeriformes : Corvus_moneduloides
Galliformes : Coturnix_japonica
Anatidae : Anser_brachyrhynchus
Apteryx : Apteryx_rowi
Struthio_camelus_australis

** primates
Hominidae : Pongo abelii
Cercopithecidae : Piliocolobus tephrosceles
Cebidae : Cebus capucinus
'''
