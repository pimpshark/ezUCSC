#!/usr/bin/python3

"""
This script automates the process of both using liftover on the UCSC genome browser
and the downloading of fasta sequences from the UCSC genome browser given a bed file.
These tasks can also be performed locally by purchasing liftover from the UCSC genome
website and downloading the genomes and bedtools to isolate the fasta sequences.

Takes in as input a bed file and outputs fasta files for each region for the specified
genomes.

This uses selenium to automate the process of performing liftover and getting the fasta
files from UCSC and is written for the use of Firefox only. Geckodriver must also be
placed within /usr/bin for selenium to work with Firefox. Look at the selenium doc for
more information.
"""
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import urllib.request

#read bed file to list
def bed_to_string(bed):
    lists = []
    with open(bed, "rt") as x:
        for i in x:
            lists.append(i)
    comb = "".join(lists)
    return comb

#liftOver('mouse-hcn4-en.bed', 'mouse', 'human', 'temp', 'mm9')

#read list to liftover
def liftOver(seq,input,output,outpath, inlib='default', outlib='default'):
    site = 'https://genome.ucsc.edu/cgi-bin/hgLiftOver'
    assertion = 'Lift'
    browser=webdriver.Firefox()
    browser.get(site)
    assert assertion in browser.title
    seq_box = 'hglft_userData'
    select = Select(browser.find_element_by_xpath("//select[@name='hglft_fromOrg']"))
    option = select.options
    animalin = []
    for x in option:
        animalin.append(x.get_attribute('label'))
    t=0
    for a in animalin:
        if input.lower() == a.lower():
            inanimal = a
            path = "//select[@name='hglft_fromOrg']/option[text()=" + "'" + inanimal + "'" + "]"
            t=1
            break
    if t == 0:
        print('your input organism, ' + input + ', could not be read or is not on the UCSC genome browser')
        return
    if inlib == 'default':
        browser.find_element_by_xpath(path).click()
    else:
        browser.find_element_by_xpath(path).click()
        select = Select(browser.find_element_by_xpath("//select[@name='hglft_fromDb']"))
        option = select.options
        animalinlib = []
        for x in option:
            animalinlib.append(x.get_attribute('label'))
        l = 0
        for i in animalinlib:
            if inlib.lower() in i.lower():
                print('selecting ' + i + ' as input library')
                pathinlib = "//select[@name='hglft_fromDb']/option[text()=" + "'" + i + "'" + "]"
                browser.find_element_by_xpath(pathinlib).click()
                l=1
        if l == 0:
            print('failed to find the input library, ' + inlib + ' on the liftover website')
            return
    select = Select(browser.find_element_by_xpath("//select[@name='hglft_toOrg']"))
    option = select.options
    animalout = []
    for x in option:
        animalout.append(x.get_attribute('label'))
    s = 0
    for a in animalout:
        if output.lower() == a.lower():
            outanimal = a
            path = "//select[@name='hglft_toOrg']/option[text()=" + "'" + outanimal + "'" + "]"
            s = 1
            break
    if s == 0:
        print('your output organism, ' + output + ', could not be read or cannot be directly compared with the input organism and library')
        return
    browser.find_element_by_xpath(path).click()
    select = Select(browser.find_element_by_xpath("//select[@name='hglft_toDb']"))
    option = select.options
    animaloutlib = []
    for x in option:
        animaloutlib.append(x.get_attribute('label'))
    if outlib == 'default':
        database = animaloutlib[0]
        libused = database.split('/')[1].split(')')[0]
        print("will use " + libused)
    else:
        y = 0
        for i in animaloutlib:
            if outlib.lower() in i.lower():
                print('selecting ' + i + ' as output library')
                pathoutlib = "//select[@name='hglft_toDb']/option[text()=" + "'" + i + "'" + "]"
                browser.find_element_by_xpath(pathoutlib).click()
                y=1
                print('outlib is ' + outlib)
                #return(outlib)
        if y == 0:
            print('failed to find the output library, ' + outlib + ' on the liftover website')
            return

    print('sending sequences')
    elem = browser.find_element_by_name(seq_box)
    elem.send_keys(seq + Keys.RETURN)
    pathsub = "//input[@name='Submit']"
    browser.find_element_by_xpath(pathsub).click()
    browser.implicitly_wait(15)
    elem = browser.find_element_by_link_text('View Conversions')
    link = elem.get_attribute('href')
    browser.quit()
    urllib.request.urlretrieve(link, outpath)
    if outlib == 'default':
        print(libused)
        return libused
    else:
        print(outlib)
        return outlib

def total(one, two, three, four, five='default', six='default'):
    sequences = bed_to_string(one)
    return liftOver(sequences, two, three, four, five, six)


#if len(sys.argv) == 5:
#    total(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
#elif len(sys.argv) == 7:
#    total(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
