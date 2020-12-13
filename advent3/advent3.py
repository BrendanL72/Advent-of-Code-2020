#advent calendar day 3
import fileinput
def treeTraj(rightOffset, downOffset):
    offset = 0
    numTrees= 0
    lineNum = 0
    for line in fileinput.input(files = "advent3input.txt"):
        if (lineNum % downOffset > 0):
            lineNum += 1
            continue
        width = len(line.rstrip())
        char = line[offset % width]
        if (char == '#'):
            numTrees += 1
        offset += rightOffset
        lineNum += 1
        #print(width)
    print(numTrees)

def main():    
    treeTraj(1,1)
    treeTraj(3,1)
    treeTraj(5,1)
    treeTraj(7,1)
    treeTraj(1,2)

main()
