from argparse import ArgumentParser
from .fasta import read_mfasta

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("fasta")
    parser.add_argument("--max-cols",type=int,default=30)
    args = parser.parse_args()
    mfasta=read_mfasta(args.fasta)
    for entry in mfasta:
        print(entry.to_str(args.max_cols))