# function that takes in a single amino acid either in its 3 letter or one letter form and returns all of the possible codons that map to that amino acid

import itertools

def peptideEncoding():
    aminoAcid = str(input("Please enter either a 3 letter or 1 letter amino acid sequence"))
    aminoAcid = aminoAcid.upper()
    length = len(aminoAcid)
    #dictionaries that act like the codon tables
    codonThreeDictionary = {"PHE": ["TTT, TTC"],
                            "LEU": ["CTT, CTC, CTA, CTG, TTA, TTG"],
                            "SER": ["TCT, TCC, TCA, TCG, AGT, AGC"],
                            "TYR": ["TAT, TAC"],
                            "STOP": ["TAA, TAG, TGA"],
                            "CYS": ["TGT, TGC"],
                            "TRP": ["TGG"],
                            "PRO": ["CCT, CCC, CCA, CCG"],
                            "HIS": ["CAT, CAC"],
                            "GLY": ["GGT, GGC, GGA, GGG"],
                            "ARG": ["CGT, CGC, CGA, CGG, AGA, AGG"],
                            "ILE": ["ATT, ATC, ATA"],
                            "MET": ["ATG"],
                            "THR": ["ACT, ACC, ACA, ACG"],
                            "ASN": ["AAT, AAC"],
                            "LYS": ["AAA, AAG"],
                            "VAL": ["GTT, GTC, GTA, GTG"],
                            "ALA": ["GCT, GCC, GCA, GCG"],
                            "ASP": ["GAT, GAC"],
                            "GLU": ["GAA, GAG"], }
    codonOneDictionary = {"F": ["TTT, TTC"],
                          "L": ["CTT, CTC, CTA, CTG, TTA, TTG"],
                          "S": ["TCT, TCC, TCA, TCG, AGT, AGC"],
                          "Y": ["TAT, TAC"],
                          "STOP": ["TAA, TAG, TGA"],
                          "C": ["TGT, TGC"],
                          "W": ["TGG"],
                          "P": ["CCT, CCC, CCA, CCG"],
                          "H": ["CAT, CAC"],
                          "G": ["GGT, GGC, GGA, GGG"],
                          "R": ["CGT, CGC, CGA, CGG, AGA, AGG"],
                          "I": ["ATT, ATC, ATA"],
                          "M": ["ATG"],
                          "T": ["ACT, ACC, ACA, ACG"],
                          "N": ["AAT, AAC"],
                          "K": ["AAA, AAG"],
                          "V": ["GTT, GTC, GTA, GTG"],
                          "A": ["GCT, GCC, GCA, GCG"],
                          "D": ["GAT, GAC"],
                          "E": ["GAA, GAG"], }
    #find the list of values(codons) mapped to a desired key (amino acid)
    if length == 3:
        if aminoAcid in codonThreeDictionary:
            print(codonThreeDictionary[aminoAcid])
    elif length == 1:
        if aminoAcid in codonOneDictionary:
            print(codonOneDictionary[aminoAcid])

    else:
        print(
            "The amino acid you inputted was not in the correct format, please enter a single amino acid using either its 1 letter or 3 letter abbreviation")


def listPeptideEncoding():
    aminoAcid = str(input("Please enter an amino acid sequence: "))
    threeOrOneLetter = int(input("Did you enter the above amino acid sequence using the 1 or 3 letter abbreviation"
                                 " (type in either 1 or 3): "))
    aminoAcidList = []

    length = len(aminoAcid)
    #dictionaries that are codon tables
    codonThreeDictionary = {"PHE": ["TTT, TTC"],
                            "LEU": ["CTT, CTC, CTA, CTG, TTA, TTG"],
                            "SER": ["TCT, TCC, TCA, TCG, AGT, AGC"],
                            "TYR": ["TAT, TAC"],
                            "STOP": ["TAA, TAG, TGA"],
                            "CYS": ["TGT, TGC"],
                            "TRP": ["TGG"],
                            "PRO": ["CCT, CCC, CCA, CCG"],
                            "HIS": ["CAT, CAC"],
                            "GLY": ["GGT, GGC, GGA, GGG"],
                            "ARG": ["CGT, CGC, CGA, CGG, AGA, AGG"],
                            "ILE": ["ATT, ATC, ATA"],
                            "MET": ["ATG"],
                            "THR": ["ACT, ACC, ACA, ACG"],
                            "ASN": ["AAT, AAC"],
                            "LYS": ["AAA, AAG"],
                            "VAL": ["GTT, GTC, GTA, GTG"],
                            "ALA": ["GCT, GCC, GCA, GCG"],
                            "ASP": ["GAT, GAC"],
                            "GLU": ["GAA, GAG"], }
    codonOneDictionary = {"F": ["TTT, TTC"],
                          "L": ["CTT, CTC, CTA, CTG, TTA, TTG"],
                          "S": ["TCT, TCC, TCA, TCG, AGT, AGC"],
                          "Y": ["TAT, TAC"],
                          "STOP": ["TAA, TAG, TGA"],
                          "C": ["TGT, TGC"],
                          "W": ["TGG"],
                          "P": ["CCT, CCC, CCA, CCG"],
                          "H": ["CAT, CAC"],
                          "G": ["GGT, GGC, GGA, GGG"],
                          "R": ["CGT, CGC, CGA, CGG, AGA, AGG"],
                          "I": ["ATT, ATC, ATA"],
                          "M": ["ATG"],
                          "T": ["ACT, ACC, ACA, ACG"],
                          "N": ["AAT, AAC"],
                          "K": ["AAA, AAG"],
                          "V": ["GTT, GTC, GTA, GTG"],
                          "A": ["GCT, GCC, GCA, GCG"],
                          "D": ["GAT, GAC"],
                          "E": ["GAA, GAG"], }

    #creates the list of lists by looking up the amino acids as keys in the table and appending its mapped list of
    #codons to the list aminoAcidList
    if threeOrOneLetter == 1:
        aminoAcid = aminoAcid.upper()
        for oneLetterChar in aminoAcid:
            aminoAcidList.append(codonOneDictionary[oneLetterChar])
        print(aminoAcidList)

    elif threeOrOneLetter == 3:
        counter = 0
        aminoAcid = aminoAcid.upper()
        while counter < length:
            threeLetterAminoAcid = aminoAcid[counter:counter + 3]

            aminoAcidList.append((codonThreeDictionary[threeLetterAminoAcid]))
            counter += 3
        print(aminoAcidList)

    else:
        print(
            "Please enter in either 1 or 3 if the amino acid sequence you entered used the 3 or 1 letter abbreviation")








def checkIfSubStringInmRNA(mRNASequence, aminoAcidList):
    #itertool function creates every possible permutation from a list of lists i.e [1,2,3],[1,2] would return
    #[1,1],[1,2],[2,1],[2,2],[3,1],[3,2],
    possibleAminoAcidStrings = list(itertools.product(*aminoAcidList))
    numSubStrings = len(possibleAminoAcidStrings)
    for i in range(numSubStrings):
        substring = "".join(possibleAminoAcidStrings[i])
        substring.replace(" ", "")
        if substring in mRNASequence:
            return True, substring
    else:
        return False, "none"




def findAminoAcidinmRNA():
    mRNASequence = str(input("Please enter a mRNA Sequence")).upper()
    aminoAcid = str(input("Please enter an amino acid sequence: "))
    threeOrOneLetter = int(input("Did you enter the above amino acid sequence using the 1 or 3 letter abbreviation"
                                 " (type in either 1 or 3): "))
    aminoAcidList = []
    isAminoAcidInmRNA = False

    length = len(aminoAcid)
    codonThreeDictionary = {"PHE": ["UUU", "UUC"],
                            "LEU": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"],
                            "SER": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
                            "TYR": ["UAU", "UAC"],
                            "STOP": ["UAA", "UAG", "UGA"],
                            "CYS": ["UGU", "UGC"],
                            "TRP": ["UGG"],
                            "PRO": ["CCU", "CCC", "CCA", "CCG"],
                            "HIS": ["CAU", "CAC"],
                            "GLY": ["GGU", "GGC", "GGA", "GGG"],
                            "ARG": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
                            "ILE": ["AUU", "AUC", "AUA"],
                            "MET": ["AUG"],
                            "THR": ["ACU", "ACC", "ACA", "ACG"],
                            "ASN": ["AAU", "AAC"],
                            "LYS": ["AAA", "AAG"],
                            "VAL": ["GUU", "GUC", "GUA", "GUG"],
                            "ALA": ["GCU", "GCC", "GCA", "GCG"],
                            "ASP": ["GAU", "GAC"],
                            "GLU": ["GAA", "GAG"]}

    codonOneDictionary = {"F": ["UUU", "UUC"],
                          "L": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"],
                          "S": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
                          "Y": ["UAU", "UAC"],
                          "STOP": ["UAA", "UAG", "UGA"],
                          "C": ["UGU", "UGC"],
                          "W": ["UGG"],
                          "P": ["CCU", "CCC", "CCA", "CCG"],
                          "H": ["CAU", "CAC"],
                          "G": ["GGU", "GGC", "GGA", "GGG"],
                          "R": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
                          "I": ["AUU", "AUC", "AUA"],
                          "M": ["AUG"],
                          "T": ["ACU", "ACC", "ACA", "ACG"],
                          "N": ["AAU", "AAC"],
                          "K": ["AAA", "AAG"],
                          "V": ["GUU", "GUC", "GUA", "GUG"],
                          "A": ["GCU", "GCC", "GCA", "GCG"],
                          "D": ["GAU", "GAC"],
                          "E": ["GAA", "GAG"]}
    if threeOrOneLetter == 1:
        aminoAcid = aminoAcid.upper()
        for oneLetterChar in aminoAcid:
            aminoAcidList.append(codonOneDictionary[oneLetterChar])
        trueOrFalse, substring = checkIfSubStringInmRNA(mRNASequence, aminoAcidList)
        if trueOrFalse == True:
            print("The amino acid sequence", substring, "was found in the mRNA")
        if trueOrFalse == False:
            print("no amino acid sequence was found in the mRNA")

    elif threeOrOneLetter == 3:
        counter = 0
        aminoAcid = aminoAcid.upper()
        while counter < length:
            threeLetterAminoAcid = aminoAcid[counter:counter + 3]

            aminoAcidList.append((codonThreeDictionary[threeLetterAminoAcid]))
            counter += 3
        trueOrFalse, substring = checkIfSubStringInmRNA(mRNASequence, aminoAcidList)
        if trueOrFalse == True:
            print("The amino acid sequence", substring, "was found in the mRNA")
        if trueOrFalse == False:
            print("no amino acid sequence was found in the mRNA")

    else:
        print(
            "Please enter in either 1 or 3 if the amino acid sequence you entered used the 3 or 1 letter abbreviation")



