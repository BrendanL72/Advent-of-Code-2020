import fileinput
splitLine = []
validPasswords = 0
for line in fileinput.input(files = "advent2input.txt"):
    splitLine = line.split()
    minMax = splitLine[0].split('-')
    char = splitLine[1][0]
    #part1
##    count = splitLine[2].count(char);
##    if (count >= int(minMax[0])) and (count <= int(minMax[1])):
##        validPasswords += 1
    if (splitLine[2][int(minMax[0])-1] == char) ^ (splitLine[2][int(minMax[1])-1] == char):
        validPasswords += 1
print(validPasswords)
    
