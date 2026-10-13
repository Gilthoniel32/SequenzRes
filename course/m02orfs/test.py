import unittest
from ..m01fasta.fasta import FastaSequence
from .seqops import reverse_complement,find_open_reading_frames

class TestReverseComplement(unittest.TestCase):
    def test_single_char(self):
        fasta = FastaSequence(">seq1","A")
        rfasta = reverse_complement(fasta)
        assert(rfasta.sequence=="T")
    def test_reverse_complement(self):
        fasta = FastaSequence(">seq1","ACGTTAGTA")
        rfasta = reverse_complement(fasta)
        assert(rfasta.sequence=="TACTAACGT")
    def test_is_copy(self):
        fasta = FastaSequence(">seq1","AGCTGATGATAGGA")
        rfasta = reverse_complement(fasta)
        assert(fasta is not rfasta)
        rrfasta = reverse_complement(rfasta)
        assert(fasta is not rrfasta)
        assert(fasta.sequence == rrfasta.sequence)
    
    
class TestFindOpenReadingFrames(unittest.TestCase):
    def test_none(self):
        fasta = FastaSequence(">seq1","AAAAAAAAAA")
        orfs = find_open_reading_frames(fasta)
        assert(len(orfs)==0)
    def test_one(self):
        fasta = FastaSequence(">seq1","GGATGGGGTAG")
        orfs = find_open_reading_frames(fasta)
        assert(len(orfs)==1)
        start,end = orfs[0]
        assert(start==2)
        assert(end==11)
    def test_none_frameshift(self):
        fasta = FastaSequence(">seq1","GGATGGGTAG")
        orfs = find_open_reading_frames(fasta)
        assert(len(orfs)==0)
    def test_reverse(self):
        fasta = FastaSequence(">seq1","TCTACATTT")
        orfs = find_open_reading_frames(fasta)
        assert(len(orfs)==1)
        start,end = orfs[0]
        assert(end==1)
        assert(start==7)
    def test_multi(self):
        fasta = FastaSequence(">seq1","ATGAAATAAGGGATGTTTTGA")
        orfs = find_open_reading_frames(fasta)
        assert(len(orfs)==2)
        orfs = set(orfs)
        assert((0,9) in orfs)
        assert((12,21) in orfs)
    def test_overlapping(self):
        fasta = FastaSequence(">seq1","ATGAAAATGTAG")
        orfs = find_open_reading_frames(fasta)
        assert(len(orfs)==2)
    def test_overlapping_reverse(self):
        fasta = FastaSequence(">seq1","ATGTTACATTAG")
        orfs = find_open_reading_frames(fasta)
        assert(len(orfs)==2)
        orfs = set(orfs)
        assert((0,12) in orfs)
        assert((9,3) in orfs)

if __name__ == '__main__':
    unittest.main()