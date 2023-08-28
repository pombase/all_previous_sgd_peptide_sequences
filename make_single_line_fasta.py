"""
Takes a fasta file with multiple sequences, and turns it into a tsv file where the first column is the sequence ID and the second column is the sequence itself.
For example:

>YAL001C
MVLTIYPDELVQIVSDKIASNKGKITLNQLWDISGKYFDLSDKKVKQFVLSCVILKKDIE
>YAL002W
MTAPAFANLSNNSSSNNNSNNN

becomes

YAL001C MVLTIYPDELVQIVSDKIASNKGKITLNQLWDISGKYFDLSDKKVKQFVLSCVILKKDIE
YAL002W MTAPAFANLSNNSSSNNNSNNN

Usage:
    python make_single_line_fasta.py file1.fasta file2.fasta file3.fasta

Output (written where the input files are):
    file1_single_line.tsv, file2_single_line.tsv, file3_single_line.tsv

"""

import sys
from Bio.SeqIO import parse
import subprocess

def main(fasta_file):
    no_extension = fasta_file.split('.')[0]
    out_file = f'{no_extension}_single_line.tsv'
    with open(out_file, 'w') as out:
        for record in parse(fasta_file, 'fasta'):
            out.write(f'{record.id}\t{record.seq}\n')

    # sort -o filename
    subprocess.call(['sort', '-o', out_file, out_file])

if __name__ == '__main__':
    for arg in sys.argv[1:]:
        main(arg)