def TranslationTranscription():
    nucleotideSequence = str(input("Please enter a 5-to-3 nucleotide sequence"))
    print("Is this strand a: ")
    print("a. A template DNA strand")
    print("b. A non-template DNA strand")
    print("c. A mRNA strand")
    typeOfStrand = str(
        input("Please enter the lower case letter listed above that describes your nucleotide sequence (a,b,c)"))
    if typeOfStrand == "a":
    elif typeOfStrand== "b":
    elif typeOfStrand=="c":
    else:
        print("please enter a valid lower case letter either a, b or c ")



TranslationTranscription()
