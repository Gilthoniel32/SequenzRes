from ..m01fasta.fasta import FastaSequence


COMPLEMENT = {'A':'T','T':'A','C':'G','G':'C'}

START_CODONS = ["ATG"]
STOP_CODONS = ["TAA","TAG","TGA"]



def reverse_complement(fasta : FastaSequence) -> FastaSequence:
    """
    TODO: Implement the reverse complement for the input fasta sequence.
    To prevent edits on the same data, ensure the object is copied!
    """
    pass

def find_open_reading_frames(fasta : FastaSequence) -> list[(int,int)]:
    """
    TODO
    Output the tuples with zero based coordinates and the last coordinate
    exclusive, such that for an output (i,j) fasta.sequence[i:j] is exactly
    the open reading frame, including start and stop codon.

    You may find it helpful to just write a function for forward reading frames,
    i.e. 'find_open_reading_frames_fwd' and then using 'reverse_complement' to
    find ORFs on the backward strand, converting the coordinates back to the forward
    direction.
    """
    pass
