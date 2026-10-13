from argparse import ArgumentParser
from ..m01fasta.fasta import read_mfasta
from .seqops import find_open_reading_frames

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("fasta")
    args = parser.parse_args()
    entries = read_mfasta(args.fasta)
    for entry in entries:
        orfs = find_open_reading_frames(entry)
        #TODO: Print the open reading frames and their fasta id
        #TODO: Implement size filtering (you have to add an argument to the command line parser)
