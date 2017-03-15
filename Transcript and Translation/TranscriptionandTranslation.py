def convertmRNAToAminoAcid(fiveToThreemRNA):
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
    length = len(fiveToThreemRNA)
    startCodon = False
    endCodon = False
    aminoAcidChain = ""
    stopCodons = ["UAG", "UAA", "UGA"]

    while startCodon != True:
        aminoAcid = fiveToThreemRNA[counter:counter + 3]
        if aminoAcid == "AUG":
            startCodon = True
            aminoAcidChain += "Met"
            counter+=3
            startofCodingSequence=fiveToThreemRNA[counter:]
        elif aminoAcid!=True:
            aminoAcidChain+="   "
        counter+=3

    counter=0
    length=len(startofCodingSequence)
    while counter <= length:
        aminoAcid = startofCodingSequence[counter:counter + 3]
        if aminoAcid in stopCodons==True:
            return aminoAcidChain
        else:
            for aminoAcidSequence, codonTable in codonOneDictionary.items():
                if aminoAcid in codonTable:
                    aminoAcidChain+=aminoAcidSequence
                    break

        counter += 3
    return aminoAcidChain





def templateDNA(templateStrand):
    nonTemplateStrand=""
    mRNAStrand=""
    revTemplate=templateStrand[::-1]
    length = len(revTemplate)
    print(revTemplate)


    for i in range(length):
        if revTemplate[i]=="A":
            nonTemplateStrand+="T"
            mRNAStrand+="U"
        elif revTemplate[i]=="T":
            nonTemplateStrand += "A"
            mRNAStrand+="A"
        elif revTemplate[i]=="G":
            nonTemplateStrand += "C"
            mRNAStrand += "C"
        elif revTemplate[i]=="C":
            nonTemplateStrand += "G"
            mRNAStrand += "G"
    aminoAcidSequence=convertmRNAToAminoAcid(mRNAStrand)
    print("The Template Strand:     ", "3' " + revTemplate + " 5'", "\n"
          "The non-template Strand: ", "5' " + nonTemplateStrand + " 3'", "\n"
          "The mRNA Strand:         ", "5' " + mRNAStrand + " 3'", "\n"
          "The Amino Acid Sequence: ", "5' " + aminoAcidSequence + " 3'"

          )


def nonTemplateDNA(nonTemplateStrand):
    length=len(nonTemplateStrand)
    templateStrand=""
    mRNAStrand=""

    for i in range(length):
        if nonTemplateStrand[i]=="A":
            templateStrand+="T"
            mRNAStrand+="A"
        elif nonTemplateStrand[i] == "T":
            templateStrand += "A"
            mRNAStrand+="U"
        elif nonTemplateStrand[i] == "G":
            templateStrand += "C"
            mRNAStrand += "G"
        elif nonTemplateStrand[i] == "C":
            templateStrand += "G"
            mRNAStrand += "C"
    aminoAcidSequence = convertmRNAToAminoAcid(mRNAStrand)

    print("The non-template Strand: ", "5' " + nonTemplateStrand + " 3'", "\n"
          "The Template Strand:     ", "3' " + templateStrand + " 5'", "\n"
          "The mRNA Strand:         ", "5' " + mRNAStrand + " 3'", "\n"
          "The Amino Acid Sequence: ", "5' " + aminoAcidSequence + " 3'"
          )


def mRNAStrand(mRNAStrand):
    nonTemplateStrand = ""
    templateStrand = ""
    aminoAcidSequence = convertmRNAToAminoAcid(mRNAStrand)
    length = len(mRNAStrand)
    for i in range(length):
        if mRNAStrand[i] == "A":
            templateStrand += "T"
            nonTemplateStrand += "A"
        elif mRNAStrand[i] == "G":
            templateStrand += "C"
            nonTemplateStrand += "G"
        elif mRNAStrand[i] == "C":
            templateStrand += "G"
            nonTemplateStrand += "C"
        elif mRNAStrand[i] == "U":
            templateStrand += "A"
            nonTemplateStrand += "T"

    print("The non-template Strand: ", "5' " + nonTemplateStrand + " 3'", "\n"
          "The Template Strand:     ", "3' " + templateStrand + " 5'", "\n"
          "The mRNA Strand:         ", "5' " + mRNAStrand + " 3'", "\n"
          "The Amino Acid Sequence: ", "5' " + aminoAcidSequence + " 3'"
          )








def TranslationTranscription():
    nucleotideSequence = str(input("Please enter a 5-to-3 nucleotide sequence")).upper()
    print("Is this strand: ")
    print("a. A template DNA strand")
    print("b. A non-template DNA strand")
    print("c. A mRNA strand")
    typeOfStrand = str(
        input("Please enter the lower case letter listed above that describes your nucleotide sequence (a,b,c)"))
    if typeOfStrand == "a":
        templateDNA(nucleotideSequence)
    elif typeOfStrand== "b":
        nonTemplateDNA(nucleotideSequence)
    elif typeOfStrand=="c":
        mRNAStrand(nucleotideSequence)
    else:
        print("please enter a valid lower case letter either a, b or c ")

TranslationTranscription()
