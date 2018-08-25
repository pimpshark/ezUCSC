#!/usr/bin/python3

"""

input genomic positions into the ucsc genome website and download the concurrent fasta files for any indicated organism and library
if no library is specified, it will assume the library is in the file name in this format filename-lib.bed

"""
from bs4 import BeautifulSoup
import bs4
from bs4 import *
import urllib.request
import sys
import os

def getFasta(seq, output, lib="default"):

    if lib == 'default':
        lib = seq.split('.')[0].split('-')[1]
    print('using ' + lib + ' as library')
    with open(seq, 'rt') as pls:
        current = pls.read()
    list = current.split('\n')
    sequencelist = list[:len(list)-1]
    for i in sequencelist:
        if ':' in i:
            print(i)
            chrom = i.split(':')
            chr = chrom[0]
            positions = chrom[1].split('-')
            pos1int = positions[0]
            pos1 = str(int(pos1int)-1)
            pos2 = positions[1]
            sitept0='https://genome.ucsc.edu/cgi-bin/hgc?hgsid='
            sitept2 = '&g=htcGetDna2&table=&i=mixed&o=' + pos1 + '&l=' + pos1 + '&r=' + pos2 + '&getDnaPos=' + chr + '%3A'
            sitept3 = pos1[:2] + '%2C' + pos1[2:5] + '%2C' + pos1[5:8] + '-' + pos2[:2] + '%2C' + pos2[2:5] + '%2C' + pos2[5:8] + '&db=' + lib
            sitept4 = '&hgSeq.cdsExon=1&hgSeq.padding5=0&hgSeq.padding3=0&hgSeq.casing=upper&boolshad.hgSeq.maskRepeats=0&hgSeq.repMasking=lower&boolshad.hgSeq.revComp=0&submit=get+DNA'
            sitepta=['685472393_vBUENpT6tcuafSI3JgJpSjkORRhJ','685497575_vSIBY6HIaxZ0VKQ2wZsZHchqaIz5','686027371_0rkyREP7ERYGvqf6uqyibK97oCPw','686027665_LmOlufHfBd3jl6ImkDWMFTTYt7Jy','686073789_CqNli04kaR2OAsjPQGiZY3uqBb9Z']
            siteptb=['686073943_7Axa7grV9xaAgnRMpAh3NtowisQI','686074023_uD5eIDhbTN03chKu3OGnORAsXbdc','686074119_lQUUsOASN5dfYPRU0SOZfZmNuCws','686074177_x51ADHLw3ZUfEU65GwRK3iD2Ylqs','686074229_ywPXI4ziMofGc5WyUVMC6qK1DBSL']
            siteptc=['686074271_qQWGR7aOaoRNsr8pJbR9dNDIJRMa','686074303_hn5s7xHJuSujGH3pd0BkFLceztwG','686074367_5GOCIbavVkrALcKrtFYemxTtkPmq','686074431_fPAa83bizAWTlXZZHn3abxPIO99J','686074683_zcTeUqjieLSuchEWqysoYbZqw6JT']
            siteptd=['686990223_nFFK8K7rn2JYbK6Or7ZzoJZiHBfS','686074723_rp0xEu2LRtxrh2xlFe3NPKAKmx0y','686074753_gSYnh8YtQKurnxz3JDIjNX6GsaMy','686074825_a0KqnNGBOJjlMIaSUCbfAE6awMKk','686074845_ujVLSTDkKNAwBTHzuDJ099zlyaDr','686074975_ZHhlf9C9tFqnkdoMaZaTHJE5ABaS']
            sitept = sitepta+siteptb+siteptc+siteptd
            def readFasta(sitept1):
                site = sitept0 + sitept1 + sitept2 + sitept3 + sitept4
                soup = BeautifulSoup(urllib.request.urlopen(site), "lxml")
                for i in soup.findAll(text=True):
                    if 'hgc' in i:
                        raise ValueError("Bad Link")
                        break
                    elif chr in i:
                        fasta = i[1:]
                        break
                    elif "scaffold" in i:
                        fasta = i
                type(fasta)
                print("Fasta Found!")
                print('reading from ' + site)
                return(fasta)

            for i in sitept:
                try:
                    fasta=readFasta(i)
                    break
                except:
                    pass
    with open(output, "a") as file:
        file.write(fasta)
        file.write('\n')
"""
            try:
                sitept1 = 'https://genome.ucsc.edu/cgi-bin/hgc?hgsid=685472393_vBUENpT6tcuafSI3JgJpSjkORRhJ&g=htcGetDna2&table=&i=mixed&o='
                fasta = readFasta(sitept1)

            except:
                try:
                    sitept1 = 'https://genome.ucsc.edu/cgi-bin/hgc?hgsid=685497575_vSIBY6HIaxZ0VKQ2wZsZHchqaIz5&g=htcGetDna2&table=&i=mixed&o='
                    fasta = readFasta(sitept1)

                except:
                    try:
                        1sitept1 = 'https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686027371_0rkyREP7ERYGvqf6uqyibK97oCPw&g=htcGetDna2&table=&i=mixed&o='
                        fasta = readFasta(sitept1)
                    except:
                        try:
                        2    sitept1 = 'https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686027665_LmOlufHfBd3jl6ImkDWMFTTYt7Jy&g=htcGetDna2&table=&i=mixed&o='
                            fasta = readFasta(sitept1)
                        except:
                            try:
                        3        sitept1 = 'https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686073789_CqNli04kaR2OAsjPQGiZY3uqBb9Z&g=htcGetDna2&table=&i=mixed&o='
                                fasta = readFasta(sitept1)
                            except:
                                try:
                        4            sitept1 = 'https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686073943_7Axa7grV9xaAgnRMpAh3NtowisQI&g=htcGetDna2&table=&i=mixed&o='
                                    fasta = readFasta(sitept1)
                                except:
                                    try:
                        5                sitept1 = 'https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074023_uD5eIDhbTN03chKu3OGnORAsXbdc&g=htcGetDna2&table=&i=mixed&o='
                                        fasta = readFasta(sitept1)
                                    except:
                                        try:
                        6                    sitept1 = 'https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074119_lQUUsOASN5dfYPRU0SOZfZmNuCws&g=htcGetDna2&table=&i=mixed&o='
                                            fasta = readFasta(sitept1)
                                        except:
                                            try:
                        7                        sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074177_x51ADHLw3ZUfEU65GwRK3iD2Ylqs&g=htcGetDna2&table=&i=mixed&o='
                                                fasta=readFasta(sitept1)
                                            except:
                                                try:
                        8                            sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074229_ywPXI4ziMofGc5WyUVMC6qK1DBSL&g=htcGetDna2&table=&i=mixed&o='
                                                    fasta=readFasta(sitept1)
                                                except:
                                                    try:
                        9                                sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074271_qQWGR7aOaoRNsr8pJbR9dNDIJRMa&g=htcGetDna2&table=&i=mixed&o='
                                                        fasta=readFasta(sitept1)
                                                    except:
                                                        try:
                        10                                    sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074303_hn5s7xHJuSujGH3pd0BkFLceztwG&g=htcGetDna2&table=&i=mixed&o='
                                                            fasta=readFasta(sitept1)
                                                        except:
                                                            try:
                        11                                        sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074367_5GOCIbavVkrALcKrtFYemxTtkPmq&g=htcGetDna2&table=&i=mixed&o='
                                                                fasta=readFasta(sitept1)
                                                            except:
                                                                try:
                        12                                            sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074431_fPAa83bizAWTlXZZHn3abxPIO99J&g=htcGetDna2&table=&i=mixed&o='
                                                                    fasta=readFasta(sitept1)
                                                                except:
                                                                    try:
                        13                                                sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074519_B9NfddBcoXFe5QOTdBCT0f57J6Z8&g=htcGetDna2&table=&i=mixed&o='
                                                                        fasta=readFasta(sitept1)
                                                                    except:
                                                                        try:
                        14                                                    sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074581_x1AxJs9w29yOZV5qrVybAx5oHnnU&g=htcGetDna2&table=&i=mixed&o='
                                                                            fasta=readFasta(sitept1)
                                                                        except:
                                                                            try:
                                                                                #nakedmolerat
                        15                                                        sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074683_zcTeUqjieLSuchEWqysoYbZqw6JT&g=htcGetDna2&table=&i=mixed&o='
                                                                                fasta=readFasta(sitept1)
                                                                            except:
                                                                                try:
                                                                                    #shrew
                        16                                                            sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074723_rp0xEu2LRtxrh2xlFe3NPKAKmx0y&g=htcGetDna2&table=&i=mixed&o='
                                                                                    fasta=readFasta(sitept1)
                                                                                except:
                                                                                    try:
                        17                                                                #squirrel
                                                                                        sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074753_gSYnh8YtQKurnxz3JDIjNX6GsaMy&g=htcGetDna2&table=&i=mixed&o='
                                                                                        fasta=readFasta(sitept1)
                                                                                    except:
                                                                                        pass

                                                                                        try:
                        18                                                                    #squirrel monkey
                                                                                            sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074825_a0KqnNGBOJjlMIaSUCbfAE6awMKk&g=htcGetDna2&table=&i=mixed&o='
                                                                                            fasta=readFasta(sitept1)
                                                                                        except:
                        19                                                                    try:
                                                                                                #tarsier
                                                                                                sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074845_ujVLSTDkKNAwBTHzuDJ099zlyaDr&g=htcGetDna2&table=&i=mixed&o='
                                                                                                fasta=readFasta(sitept1)
                                                                                            except:
                        20                                                                        try:
                                                                                                    #whiterhinoceros
                                                                                                    sitept1='https://genome.ucsc.edu/cgi-bin/hgc?hgsid=686074975_ZHhlf9C9tFqnkdoMaZaTHJE5ABaS&g=htcGetDna2&table=&i=mixed&o='
686074723_rp0xEu2LRtxrh2xlFe3NPKAKmx0y,686074753_gSYnh8YtQKurnxz3JDIjNX6GsaMy,686074825_a0KqnNGBOJjlMIaSUCbfAE6awMKk,686074845_ujVLSTDkKNAwBTHzuDJ099zlyaDr,686074975_ZHhlf9C9tFqnkdoMaZaTHJE5ABaS                                                                                  fasta=readFasta(sitept1)
                                                                                                except:

                                                                                                    print("\n\nERROR in pulling Fasta\n\n")
                                                                                                    print(site)
                                                                                                    print(lib)
                                                                                                    print(chr)
                                                                                                    print(positions)
                                                                                                    print("\n\n")
                                                                                                    return
"""




#if len(sys.argv) == 3:
#    getFasta(sys.argv[1], sys.argv[2])
#elif len(sys.argv) == 4:
#    getFasta(sys.argv[1], sys.argv[2], sys.argv[3])
#else:
#    print("ERROR: this script requires either two or three inputs")
