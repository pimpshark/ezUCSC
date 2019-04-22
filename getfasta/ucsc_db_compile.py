#!/usr/bin/python3

# compile database containing the name of every genomic library on the UCSC genome browser, as well as a corresponding hgsid tag

import sqlite3

species = ['human', 'chimp', 'bonobo', 'gorilla', 'orangutan', 'gibbon', 'green monkey', 'crab-eating macaque', 'rhesus', 'baboon', 'proboscis monkey', 'golden snub-nosed monkey', 'marmoset', 'squirrel monkey',
'tarsier', 'mouse lemur', 'bushbaby', 'mouse', 'rat', 'chinese hamster', 'kangaroo rat', 'naked mole-rat', 'guinea pig', 'squirrel', 'rabbit', 'pika', 'malayan flying lemur', 'tree shrew', 'hedgehog', 'shrew',
'pig', 'cow', 'bison', 'sheep', 'dolphin', 'minke whale', 'alpaca', 'horse', 'white rhinoceros', 'dog', 'ferret', 'panda', 'cat', 'megabat', 'microbat', 'chinese pangolin', 'elephant', 'manatee', 'rock hyrax',
'tenrec', 'armadillo', 'sloth', 'wallaby', 'tasmanian devil', 'opossum', 'platypus', 'chicken', 'turkey', 'golden eagle', 'zebra finch', 'medium ground finch', 'budgerigar', 'brown kiwi', 'american alligator',
'painted turtle', 'lizard', 'garter snake', 'x. tropicalis', 'african clawed frog', 'tibetan frog', 'coelacanth', 'zebrafish', 'stickleback', 'fugu', 'tetraodon', 'medaka', 'nile tilapia', 'atlantic cod',
'elephant shark', 'lamprey', 'lancelet', 'c. intestinalis', 's. purpuratus', 'd. melanogaster', 'd. erecta', 'd. sechellia', 'd. simulans', 'd. yakuba', 'd. ananassae', 'd. persimilis', 'd. pseudoobscura',
'd. mojavensis', 'd. virilis', 'd. grimshawi', 'a. gambiae', 'a. mellifera', 'c. elegans', 'c. brenneri', 'c. briggsae', 'c. japonica', 'c. remanei', 'p. pacificus', 'sea hare', 's. cerevisiae', 'ebola virus']

recent = ['hg38','panTro6','panPan2','gorGor5',,'ponAbe3','nomLeu3','chlSab2','macFas5','rheMac8','papAnu2','nasLar1','rhiRox1','calJac3','saiBol1','tarSyr2','micMur2','otoGar3','mm10','rn5','criGri1','dipOrd1','hetGla2',
'cavPor3','speTri2','oryCun2','ochPri3','galVar1','tupBel1','eriEur2','sorAra2','susScr11','bosTau8','bisBis1','oviAri4','turTru2','balAcu1','vicPac2','equCab2','cerSim1','canFam3','musFur1','ailMel1','felCat8','pteVam1',
'myoLuc2','manPen1','loxAfr3','triMan1','proCap1','echTel2','dasNov3','choHof1','macEug2','sarHar1','monDom5','ornAna2','galGal6','melGal5','aquChr2','taeGut2','geoFor1','melUnd1','aptMan1','allMis1','chrPic1','anoCar2',
'thaSir1','xenTro9','xenLae2','nanPar1','latCha1','danRer11','gasAcu1','fr3','tetNig2','oryLat2','oreNil2','gadMor1','calMil1','petMar3','braFlo1','ci3','strPur2','dm6','droEre1','']

previous = ['hg19','panTro5','panPan1','gorGor4','ponAbe2','nomLeu2','chlSab2','macFas5','rheMac3','papHam1','nasLar1','rhiRox1','calJac1','saiBol1','tarSyr1','micMur1','otoGar3','mm9','rn5','criGriChoV1','dipOrd1','hetGla1',
'cavPor3','speTri2','oryCun2','ochPri2','galVar1','tupBel1','eriEur1','sorAra1','susScr3','bosTau7','bisBis1','oviAri3','turTru2','balAcu1','vicPac1','equCab1','cerSim1','canFam2','musFur1','ailMel1','felCat5','pteVam1',
'myoLuc2','manPen1','loxAfr3','triMan1','proCap1','echTel1','dasNov3','choHof1','macEug2','sarHar1','monDom4','ornAna1','galGal5','melGal1','aquChr2','taeGut1','geoFor1','melUnd1','aptMan1','allMis1','chrPic1','anoCar2',
'thaSir1','xenTro7','xenLae2','nanPar1','latCha1','danRer10','gasAcu1','fr2','tetNig1','oryLat2','oreNil2','gadMor1','calMil1','petMar2','braFlo1','ci2','strPur1','dm3','droEre1','']

most_used = ['hg38','panTro4','panPan2','gorGor4','ponAbe3','nomLeu3','chlSab2','macFas5','rheMac8','papAnu2','nasLar1','rhiRox1','calJac3','saiBol1','tarSyr2','micMur2','otoGar3','mm10','rn6','criGri1','dipOrd1','hetGla2',
'cavPor3','speTri2','oryCun2','ochPri3','galVar1','tupBel1','eriEur2','sorAra2','susScr11','bosTau8','bisBis1','oviAri4','turTru2','balAcu1','vicPac2','equCab2','cerSim1','canFam3','musFur1','ailMel1','felCat8','pteVam1',
'myoLuc2','manPen1','loxAfr3','triMan1','proCap1','echTel2','dasNov3','choHof1','macEug2','sarHar1','monDom5','ornAna2','galGal6','melGal5','aquChr2','taeGut2','geoFor1','melUnd1','aptMan1','allMis1','chrPic1','anoCar2',
'thaSir1','xenTro9','xenLae2','nanPar1','latCha1','danRer11','gasAcu1','fr3','tetNig2','oryLat2','oreNil2','gadMor1','calMil1','petMar2','braFlo1','ci3','strPur2','dm6','droEre1','']

conn = sqlite3.connect('ucsc-genomes.db')
c = conn.cursor()

c.execute("""CREATE TABLE organisms (name TEXT,
                                     genome-header TEXT);""")

c.execute("""CREATE TABLE genomes-recent (genome-header TEXT,
                                            library-name TEXT);""")

c.execute("""CREATE TABLE genomes-oldest (genome-header TEXT,
                                        library-name TEXT);""")

c.execute("""CREATE TABLE genomes-most-used (genome-header TEXT,
                                        library-name TEXT);""")

c.execute("""CREATE TABLE IDs (library-name TEXT,
                                hgsid TEXT);""")


conn.commit()
