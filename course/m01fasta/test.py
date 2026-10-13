import unittest
from .fasta import FastaSequence, read_mfasta


class TestFastaSequence(unittest.TestCase):
    """Tests for FastaSequence class"""
    
    def test_init_basic(self):
        seq = FastaSequence(">seq1 description", "ATCG")
        self.assertEqual(seq.header, "seq1 description")
        self.assertEqual(seq.sequence, "ATCG")
    
    def test_init_extracts_id(self):
        seq = FastaSequence(">seq1 description here", "ATCG")
        self.assertEqual(seq.id, "seq1")
    
    def test_init_id_without_description(self):
        seq = FastaSequence(">seq1", "ATCG")
        self.assertEqual(seq.id, "seq1")
    
    def test_init_id_removes_greater_than(self):
        seq = FastaSequence(">seq1", "ATCG")
        self.assertFalse(seq.id.startswith(">"))

    
    def test_len_basic(self):
        seq = FastaSequence(">seq1", "ATCGATCG")
        self.assertEqual(len(seq), 8)

    
    def test_to_str_single_line(self):
        seq = FastaSequence(">seq1 description", "ATCG")
        result = seq.to_str(60)
        expected = ">seq1 description\nATCG"
        self.assertEqual(result, expected)
    
    def test_to_str_multiple_lines(self):
        seq = FastaSequence(">seq1", "ATCGATCGATCGATCG")
        result = seq.to_str(8)
        expected = ">seq1\nATCGATCG\nATCGATCG"
        self.assertEqual(result, expected)
    
    def test_to_str_exact_column_boundary(self):
        seq = FastaSequence(">seq1", "ATCGATCGATCGATCG")
        result = seq.to_str(16)
        expected = ">seq1\nATCGATCGATCGATCG"
        self.assertEqual(result, expected)
    
    def test_to_str_default_columns(self):
        seq = FastaSequence(">seq1", "A" * 120)
        result = seq.to_str()
        lines = result.split("\n")
        self.assertEqual(len(lines), 3)  # header + 2 sequence lines
        self.assertEqual(len(lines[1]), 60)
        self.assertEqual(len(lines[2]), 60)

    def test_to_str_preserves_header(self):
        seq = FastaSequence(">seq1 with long description", "ATCG")
        result = seq.to_str()
        self.assertTrue(result.startswith(">seq1 with long description\n"))


class TestReadMfasta(unittest.TestCase):
    """Integration test for read_mfasta"""
    def test_read_mfasta(self):
        seqs = read_mfasta("data/test.fasta")
        assert(len(seqs)==5)
        ids = ["AB053182.1","NR_112116.2","U73144.1","AD001562.1","XM_069616597.1"]
        assert(ids==[s.id for s in seqs])
        assert(len(seqs[3])==379)




if __name__ == '__main__':
    unittest.main()