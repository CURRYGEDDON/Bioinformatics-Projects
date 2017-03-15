def translationAndTranscription(DNASequence):
    mRNAStrand = ""
    for i in range(len(DNASequence)):
        if DNASequence[i] == "A":
            mRNAStrand += "A"
        elif DNASequence[i] == "T":
            mRNAStrand += "U"
        elif DNASequence[i] == "G":
            mRNAStrand += "G"
        elif DNASequence[i] == "C":
            mRNAStrand += "C"
    codonOneDictionary = {"Phe": ["UUU", "UUC"],
                          "Leu": ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"],
                          "Ser": ["UCU", "UCC", "UCA", "UCG", "AGU", "AGC"],
                          "Tyr": ["UAU", "UAC"],
                          "Cys": ["UGU", "UGC"],
                          "Trp": ["UGG"],
                          "Pro": ["CCU", "CCC", "CCA", "CCG"],
                          "His": ["CAU", "CAC"],
                          "Gly": ["GGU", "GGC", "GGA", "GGG"],
                          "Arg": ["CGU", "CGC", "CGA", "CGG", "AGA", "AGG"],
                          "Ile": ["AUU", "AUC", "AUA"],
                          "Met": ["AUG"],
                          "Thr": ["ACU", "ACC", "ACA", "ACG"],
                          "Asn": ["AAU", "AAC"],
                          "Lys": ["AAA", "AAG"],
                          "Val": ["GUU", "GUC", "GUA", "GUG"],
                          "Ala": ["GCU", "GCC", "GCA", "GCG"],
                          "Asp": ["GAU", "GAC"],
                          "Glu": ["GAA", "GAG"]}

    counter = 0
    length = len(mRNAStrand)
    aminoAcidChain = ""
    counter = 0
    stopCodons=["UAG","UAA","UGA"]
    length = len(mRNAStrand)
    while counter <= length:
        aminoAcid = mRNAStrand[counter:counter + 3]
        for aminoAcidSequence, codonTable in codonOneDictionary.items():
            if aminoAcid in codonTable:
                aminoAcidChain += aminoAcidSequence
                break
        if aminoAcid in stopCodons:
            return aminoAcidChain


        counter += 3
    return aminoAcidChain






def codingSequence(DNASequence):
    startCodon = False
    endCodon = False
    counter = 0
    stopCodons = ["TAG", "TAA", "TGA"]
    length=len(DNASequence)
    codingSequence=""

    while startCodon != True :
        seq=DNASequence[counter:counter+3]
        if seq=="ATG":
            startCodon = True
            codingSequence+="ATG"

        counter+=3

    while endCodon != True:
        seq = DNASequence[counter:counter + 3]
        if seq  in stopCodons:
            DNASequence=DNASequence[:counter + 3]
            codingSequence+=seq
            return (codingSequence)
        codingSequence+=str(seq)
        counter += 3
    return(codingSequence)



def compare():
    masterSequence = "aaaTTTATGGGGCCCTAG"
        #str(
        #input("Please enter the master DNA Sequence you want to compare the other sequence to (5'-3' direction) ")).upper()
    SNPSequence = "AAAGGGATGCCCGGGTAG"
    #str(
    #    input("Please enter your other DNA sequence you want to compare against the master DNA sequence (5'-3' direction)")).upper()
    # Parse string until you find start and stop codon
    masterSequenceCodingSequence=codingSequence(masterSequence)
    SNPSequenceCodingSequence=codingSequence(SNPSequence)
    masterSequenceAminoAcid=translationAndTranscription(masterSequenceCodingSequence)
    SNPSequenceAminoAcid=translationAndTranscription(SNPSequenceCodingSequence)

    if len(masterSequenceAminoAcid)!=len(SNPSequenceAminoAcid):
        print("There has been a SNP in the second sequence that has caused a nonsense mutation resulting in the""\n"
              "second sequence being much shorter than the first sequence")
    else:
        length=len(masterSequenceAminoAcid)
        counter=0
        indexOfMismatch=[]
        while counter<=length:
            if masterSequenceAminoAcid[counter:counter+3]==SNPSequenceAminoAcid[counter:counter+3]:
                counter+=3
            elif masterSequenceAminoAcid[counter:counter+3]!=SNPSequenceAminoAcid[counter:counter+3]:
                for i in range(4):
                    if masterSequenceCodingSequence[counter:counter+i]!=SNPSequenceCodingSequence[counter:counter+i]:
                        indexOfMismatch.append(counter+i-1)
                counter+=3
        for i in range(len(indexOfMismatch)):
            index=indexOfMismatch[i]
            print("There was a SNP at index position", index, "where there was a substitution from", "a",
    masterSequenceCodingSequence[index], "to", SNPSequenceCodingSequence[index], "which caused a missense mutation""." )


compare()
