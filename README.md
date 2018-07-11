# ezUCSC
A series of different scripts to speed up the process of downloading data from the UCSC genome browser, including FASTA download from sequence ranges and LiftOver between any two libraries

## Fasta Download (getFasta)
Download fasta sequences for some chromosome range from a specific library.

### Pre-Requisites:
* bs4
* urllib

### Usage:
`getFasta(sequence, output-path, library)`

If a library is not specified, will assume that the library is in the filename, with the format of filename-library.file

Has been tested on dog, human, mouse, rabbit, rat, and guinea pig libraries, though further testing needed because of inconsistencies with url link between the former 4 and guinea pig.

## LiftOver (liftOver)
Takes in a single string with genomic positions separated by \n and converts to a specified library. Bed files can also be inserted, but must first be converted into the string format via `bed_to_string`. The function `total` combines both of these functions. 

### Pre-Requisites:
* urllib
* selenium

### Usage:
`liftOver(sequence-string, input-organism, output-organism, input-library, output-library)`

The input-library and output-library options are optional, and if not specified the most recent library for the specified species will be used. UCSC LiftOver does not support conversions between certain libraries and species, so attempts to convert directly between them will result in failure. 
