
import numpy


def buildDirectionalString(matrix, N, M, gap):

    dstring = ""
    currentRow = N
    currentCol = M
    #if a cell in the first row
    while currentRow != 0 or currentCol != 0:
        if currentRow == 0:
            dstring += "H"
            currentCol -= 1
            #if a cell in the first column
        elif currentCol == 0:
            dstring += "V"
            currentRow -= 1
            #insertion of horizontal gap in matrix
        elif (matrix[currentRow][currentCol - 1] + gap) == matrix[currentRow][currentCol]:
            dstring += "H"
            currentCol -= 1
            #insertion of vertical gap in matrix
        elif (matrix[currentRow - 1][currentCol] + gap) == matrix[currentRow][currentCol]:
            dstring += "V"
            currentRow -= 1
            #if there is a match/mismatch
        else:
            dstring += "D"
            currentRow -= 1
            currentCol -= 1
    return dstring


def main():
    #retrieves arguements from user
    seq1 = (input("Please enter sequence 1:")).upper()
    seq2 = (input("Please enter sequence 2:")).upper()
    gap = int(input("Please enter a value for gap"))
    mismatch = int(input("Please enter a value for mismatch"))
    match = int(input("Please enter a value for match"))
    N = len(seq1)
    M = len(seq2)


    #creates matrix
    matrix = numpy.zeros((N + 1, M + 1))
    #sets first item at (0,0) to 0
    matrix[0][0] = 0

    #fills in first row and column with x or y coordinate times gap
    for i in range(1, N + 1):
        matrix[i][0] = matrix[i - 1][0] + gap
    for j in range(1, M + 1):
        matrix[0][j] = matrix[0][j - 1] + gap

    #sees if inserting a gap, creating a mismatch or finding a match will result in the highest total score for a cell
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if seq1[i - 1] == seq2[j - 1]:
                score1 = matrix[i - 1][j - 1] + match
            else:
                score1 = matrix[i - 1][j - 1] + mismatch
            score2 = matrix[i][j - 1] + gap
            score3 = matrix[i - 1][j] + gap
            matrix[i][j] = max(score1, score2, score3)
    #scored matrix is inputed into function and outputed is a string of letters where each letter means
    #either a match, mismatch or insertion of a gap
    dstring = buildDirectionalString(matrix, N, M, gap)
    seq1pos = N-1
    seq2pos = M-1
    dirpos = 0
    string1=[]
    string2=[]
    matches=[]
    #if there is a D, that means letters from both strings matched, or a mismatch yielded a higher score than a gap and the
    #letters at index position dirpos of both strings can be aligned
    #append is used since traceback starts in the bottom right hand corner of the matrix
    while dirpos < len(dstring):
        if dstring[dirpos] == "D":
            string1.insert(0, seq1[seq1pos])
            string2.insert(0, seq2[seq2pos])
            #if there is an actual match
            if seq1[seq1pos]==seq2[seq2pos]:
                matches.insert(0, "|")
            else:
                matches.insert(0," ")
            seq1pos -= 1
            seq2pos -= 1
        #verticall shift
        elif dstring[dirpos] == "V":
            string1.insert(0, seq1[seq1pos])
            string2.insert(0, "-")
            matches.insert(0, " ")
            seq1pos -= 1
            #horizontal shift
        else:
            string1.insert(0, "_")
            string2.insert(0, seq2[seq2pos])
            matches.insert(0, " ")
            seq2pos -= 1
        dirpos += 1


    print("".join(string1))
    print("".join(matches))
    print("".join(string2))
main()

