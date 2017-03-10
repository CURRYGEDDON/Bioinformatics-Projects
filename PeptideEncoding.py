def PeptideEncoding():
    AminoAcid = str(input("Please enter either a 3 letter or 1 letter amino acid sequence"))
    AminoAcid = AminoAcid.upper()
    length = len(AminoAcid)
    CodonThreeDictionary = {"PHE": ["TTT, TTC"],
                       "LEU": ["CTT, CTC, CTA, CTG, TTA, TTG"],
                       "SER": ["TCT, TCC, TCA, TCG, AGT, AGC"],
                       "TYR": ["TAT, TAC"],
                       "STOP": ["TAA, TAG, TGA"],
                       "CYS": ["TGT, TGC"],
                       "TRP": ["TGG"],
                       "PRO": ["CCT, CCC, CCA, CCG"],
                       "HIS":["CAT, CAC"],
                       "GLY":["GGT, GGC, GGA, GGG"],
                       "ARG":["CGT, CGC, CGA, CGG, AGA, AGG"],
                       "ILE":["ATT, ATC, ATA"],
                       "MET": ["ATG"],
                       "THR": ["ACT, ACC, ACA, ACG"],
                       "ASN": ["AAT, AAC"],
                       "LYS": ["AAA, AAG"],
                       "VAL": ["GTT, GTC, GTA, GTG"],
                       "ALA": ["GCT, GCC, GCA, GCG"],
                       "ASP": ["GAT, GAC"],
                       "GLU": ["GAA, GAG"],}
    CodonOneDictionary={"PHE": ["TTT, TTC"],
                       "L": ["CTT, CTC, CTA, CTG, TTA, TTG"],
                       "SER": ["TCT, TCC, TCA, TCG, AGT, AGC"],
                       "TYR": ["TAT, TAC"],
                       "STOP": ["TAA, TAG, TGA"],
                       "C": ["TGT, TGC"],
                       "TRP": ["TGG"],
                       "P": ["CCT, CCC, CCA, CCG"],
                       "H":["CAT, CAC"],
                       "G":["GGT, GGC, GGA, GGG"],
                       "R":["CGT, CGC, CGA, CGG, AGA, AGG"],
                       "I":["ATT, ATC, ATA"],
                       "M": ["ATG"],
                       "THR": ["ACT, ACC, ACA, ACG"],
                       "N": ["AAT, AAC"],
                       "K": ["AAA, AAG"],
                       "VAL": ["GTT, GTC, GTA, GTG"],
                       "A": ["GCT, GCC, GCA, GCG"],
                       "D": ["GAT, GAC"],
                       "E": ["GAA, GAG"],}
    if length == 3:
        if AminoAcid in CodonDictionary:
            for AA in CodonDictionary:
                print (AA[AminoAcid])
    elif length == 1:


    else:
        print(
            "The amino acid you inputted was not in the correct format, please enter a single amino acid using either its 1 letter or 3 letter abbreviation")


PeptideEncoding()
