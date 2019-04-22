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

def getFasta(seq, output, lib):

    print('using ' + lib + ' as library')
    with open(seq, 'rt') as pls:
        current = pls.read()
    list = current.split('\n')
    sequence = list[0]
    #sequencelist = list[:len(list)-1]
    if ',' in sequence:
        sequence = ''.join(sequence.split(','))
    print(sequence)
    chrom = sequence.split(':')
    chr = chrom[0]
    positions = chrom[1].split('-')
    pos1int = positions[0]
    pos1 = str(int(pos1int)-1)
    pos2 = positions[1]
    bad=0

    sitept1 = 'https://genome.ucsc.edu/cgi-bin/hgc?g=htcGetDna2&table=&i=mixed&c=' + chr + '&o=' + pos1 + '&l=' + pos1 + '&r=' + pos2 + '&getDnaPos=' + chr + '%3A'
    sitept2 = pos1[:2] + '%2C' + pos1[2:5] + '%2C' + pos1[5:8] + '-' + pos2[:2] + '%2C' + pos2[2:5] + '%2C' + pos2[5:8] + '&db=' + lib
    sitept3 = '&hgSeq.cdsExon=1&hgSeq.padding5=0&hgSeq.padding3=0&hgSeq.casing=upper&boolshad.hgSeq.maskRepeats=0&hgSeq.repMasking=lower&boolshad.hgSeq.revComp=0&submit=get+DNA'
    site = sitept1 + sitept2 + sitept3
    soup = BeautifulSoup(urllib.request.urlopen(site), "lxml")
    for i in soup.findAll(text=True):
        if 'bad input' in i:
            print(site)
            print('could not find site based on input')
            return
        if chr in i:
            fasta = i[1:]
            break
        elif 'scaffold' in i:
            fasta = i
    type(fasta)
    print("Fasta Found!")
    print('reading from ' + site)
    with open(output, "a") as file:
        file.write(fasta)
        file.write('\n')

if len(sys.argv) == 4:
    getFasta(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("ERROR: this script requires either two or three inputs")
