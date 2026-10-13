
class FastaSequence:
    """
    A class to represent a FASTA sequence entry.
    
    Attributes:
        id (str): The identifier (header until the first space)
        header (str): The full header line without the '>' character
        sequence (str): The biological sequence (DNA, RNA, or protein)
    """
    id : str
    header: str
    sequence: str
    def __init__(self,header,sequence):
        """
        TODO: Implement this initialization of the FastaSequence object.
        
        Args:
            header (str): The header line (with or without the '>' character)
            sequence (str): The sequence string (may contain whitespace/newlines)
        
        Example:
            >>> seq = FastaSequence(">sp|P12345|PROT_HUMAN Protein name", "ACGTACGT")
            >>> seq.id
            'sp|P12345|PROT_HUMAN'
            >>> seq.header
            'sp|P12345|PROT_HUMAN Protein name'
        """
        pass
    def __len__(self):
        #TODO: Implement the length of the fasta sequence (just the sequence, not the header)
        pass
    def to_str(self,max_columns:int=60):
        """
        TODO: Convert the FASTA sequence to a formatted string representation.
        
        This method wraps the sequence (but not the header!) at a specified column 
        width.
        
        Args:
            max_columns (int): Maximum number of sequence characters per line.        
        Returns:
            str: Formatted FASTA string with:
                 - Header line starting with '>'
                 - Sequence wrapped at max_columns width
        
        Example:
            >>> seq = FastaSequence(">test1", "ACGTACGTACGT")
            >>> print(seq.to_str(max_columns=5))
            >test1
            ACGTA
            CGTAC
            GT
        """
        pass


def read_mfasta(path : str) -> list[FastaSequence]:
    """TODO: Implement reading a multiple fasta file and parsing it into  FastaSequence objects.
    A multi-FASTA file contains one or more sequences, where each sequence
    starts with a header line beginning with '>' followed by one or more
    lines of sequence data.
    """
    pass
