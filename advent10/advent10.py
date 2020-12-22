import fileinput

num_one_jumps = 0
num_three_jumps = 0
current_joltage = 0

for line in fileinput.input(files = "advent10/advent10eaxmple.txt"):
    line = int(line.rstrip())

print(num_one_jumps*num_three_jumps)