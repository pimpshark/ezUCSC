# Example Implementation of getFasta and liftOver

## BED coordinates for multiple different sites of the mm9 genome are recorded

### GOAL: convert these coordinates to genomic coordinates for other species, then download the fasta files of these coordinates.

For organization purposes, each BED coordinate will be stored in its own directory, and the fasta files for other coordinates will be outputed to the directory of the BED coordinate from which they were created.
