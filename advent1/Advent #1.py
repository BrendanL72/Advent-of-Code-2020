import fileinput
nums = []
for line in fileinput.input(files = "Advent_1.txt"):
    line = int(line)
    for num1 in nums:
        for num2 in nums:
            if (line + num1 + num2 == 2020) and (num1 != num2): 
                print(line * num1 * num2)
    nums.append(line)
