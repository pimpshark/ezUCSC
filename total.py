from liftover import *
from getfasta_ucsc import *
import os

animals = ['rat', 'rabbit', 'human', 'cat', 'cow', 'white rhinoceros','chimp', 'gibbon', 'shrew', 'dog', 'chinese pangolin', 'bison', 'microbat', 'tarsier', 'squirrel monkey']
#animals = ['shrew', 'dog', 'chinese pangolin', 'bison', 'microbat', 'tarsier', 'squirrel monkey']
#animals = ['dog', 'chinese pangolin', 'bison', 'megabat']
#animals = ['microbat']
#animals = ['tarsier', 'squirrel monkey']
#animals = ['gibbon']
animals = ['Chinese hamster', 'kangaroo rat', 'naked mole-rat', 'guinea pig', 'squirrel', 'pika', 'malayan flying lemur', 'tree shrew']
number = "8"

path = "/home/rawrvi/Documents/hcn4-en/isl1-b" + number + "/"
#path = "/home/rawrvi/Documents/isl1/enhancer/"
mm10 = path + "mm10"
#filename = "small-b" + number + "-"
filename = ""
fullpath = path + filename
fullpath = path


#total("/home/rawrvi/Documents/hcn4-en/isl1-b1/mm9-small.bed","mouse","mouse","/home/rawrvi/Documents/hcn4-en/isl1-b1/mm10",'mm9')
total(path + "mm9.bed","mouse", "mouse", mm10, 'mm9')
#getFasta(mm10, fullpath + "mouse.fa","mm10")
#os.remove(mm10)

for s in animals:
    print(s)
    if s == 'human':
        total(mm10,"mouse","human","temp","mm10")
        getFasta("temp", fullpath + "human.fa", "hg19")
    else:
        lib = total(mm10,"mouse",s,"temp","mm10")
        getFasta("temp", fullpath + s + ".fa", lib)
    os.remove("temp")

getFasta(mm10, fullpath + "mouse.fa","mm10")
os.remove(mm10)
