#for this one i couldn't figure out part 2, go to advent10internet.py for the answer
import fileinput

def find_num_paths(number):
    #print(number)
    if number not in jolts:
        return 0
    if number <= 1:
        return 0
    elif number == 2:
        return 1
    else:
        return find_num_paths(number - 1) + find_num_paths(number - 2) + find_num_paths(number - 3)

num_one_jumps = 0
num_three_jumps = 1
current_joltage = 0

jolts = {}
for line in fileinput.input(files = "advent10/advent10input.txt"):
    line = int(line.rstrip())
    jolts[line] = True

#print(jolts.keys())

for x in range(len(jolts.keys())):
    if current_joltage + 1 in jolts:
        num_one_jumps += 1
        current_joltage += 1
    elif current_joltage + 2 in jolts:
        current_joltage += 2
    elif current_joltage + 3 in jolts:
        num_three_jumps += 1
        current_joltage += 3

print(num_one_jumps*num_three_jumps, num_one_jumps, num_three_jumps)

#part 2
path = sorted(jolts)
print(find_num_paths(path[-1]))

