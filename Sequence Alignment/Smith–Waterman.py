import numpy


def buildDirectionalStringWaterman(matrix, N, M, gap):
    dstring = ""
    currentRow = N
    currentCol = M
    while currentRow != 0 or currentCol != 0:
        if currentRow == 0:
            dstring += "H"
            currentCol -= 1
        elif currentCol == 0:
            dstring += "V"
            currentRow -= 1
        elif (matrix[currentRow][currentCol - 1] + gap) == matrix[currentRow][currentCol]:
            dstring += "H"
            currentCol -= 1
        elif (matrix[currentRow - 1][currentCol] + gap) == matrix[currentRow][currentCol]:
            dstring += "V"
            currentRow -= 1
        else:
            dstring += "D"
            currentRow -= 1
            currentCol -= 1
    return dstring


def Smith_Waterman():
    seq1 = (input("Please enter sequence 1:")).upper()
    seq2 = (input("Please enter sequence 2:")).upper()
    gap = int(input("Please enter a value for gap"))
    mismatch = int(input("Please enter a value for mismatch"))
    match = int(input("Please enter a value for match"))
    N = len(seq1)
    M = len(seq2)
    highestScore=0
    positionOfHighestScore=None
    matrix = numpy.zeros((N + 1, M + 1))

    matrix[0][0] = 0

    for i in range(1, N + 1):
        matrix[i][0] = 0
    for j in range(1, M + 1):
        matrix[0][j] = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if seq1[i - 1] == seq2[j - 1]:
                score1 = matrix[i - 1][j - 1] + match
            else:
                score1 = matrix[i - 1][j - 1] + mismatch
            score2 = matrix[i][j - 1] + gap
            score3 = matrix[i - 1][j] + gap
            maxScore = max(0, score1, score2, score3)
            matrix[i][j]=maxScore
            if maxScore>highestScore:
                highestScore=maxScore
                positionOfHighestScoreX=i
                positionOfHighestScoreY=j

    dstring = buildDirectionalStringWaterman(matrix, positionOfHighestScoreX, positionOfHighestScoreY, gap)
    seq1pos = N-1
    seq2pos = M-1
    dirpos = 0
    string1=[]
    string2=[]
    matches=[]

    while dirpos < len(dstring):
        if dstring[dirpos] == "D":
            string1.insert(0, seq1[seq1pos])
            string2.insert(0, seq2[seq2pos])
            if seq1[seq1pos]==seq2[seq2pos]:
                matches.insert(0, "|")
            else:
                matches.insert(0,"*")
            seq1pos -= 1
            seq2pos -= 1

        elif dstring[dirpos] == "V":
            string1.insert(0, seq1[seq1pos])
            string2.insert(0, "-")
            matches.insert(0, " ")
            seq1pos -= 1
        else:
            string1.insert(0, "_")
            string2.insert(0, seq2[seq2pos])
            matches.insert(0, " ")
            seq2pos -= 1
        dirpos += 1


    print("".join(string1))
    print("".join(matches))
    print("".join(string2))

Smith_Waterman()
