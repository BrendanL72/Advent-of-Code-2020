import fileinput

def is_escapable(index):
    for x in range(len(num_times_visited)):
        num_times_visited[x] = 0
    accumulator = 0
    instruction_index = 0
    if instructions[index] == "jmp":
        instructions[index] = "nop"
    elif instructions[index] == "nop":
        instructions[index] = "jmp"
    while instruction_index < len(instructions) and instruction_index >= 0:
        #print(instruction_index, instructions[instruction_index], numbers[instruction_index])
        if num_times_visited[instruction_index] > 0:
            if instructions[index] == "jmp":
                instructions[index] = "nop"
            elif instructions[index] == "nop":
                instructions[index] = "jmp"
            return False
        else:
            num_times_visited[instruction_index] += 1
        if instructions[instruction_index] == "acc":
            accumulator += numbers[instruction_index]
        elif instructions[instruction_index] == "jmp":
            instruction_index += numbers[instruction_index]
            continue
        elif instructions[instruction_index] == "nop":
            pass
        else:
            print("Invalid Instruction")
        instruction_index += 1
    print(accumulator)
    return True

file_name = "advent8/advent8input.txt"
instructions = []
numbers = []
num_times_visited = []

#take in file and put it all into parallel arrays
for line in fileinput.input(files= file_name):
    line = line.rstrip().split()
    instructions.append(line[0])
    numbers.append(int(line[1]))
    num_times_visited.append(0)

instruction_index = 0
accumulator = 0
loop_instruction = 0

while instruction_index < len(instructions) and instruction_index >= 0:
    #print(instruction_index, instructions[instruction_index], numbers[instruction_index])
    if num_times_visited[instruction_index] > 0:
        loop_instruction = instruction_index
        break
    else:
        num_times_visited[instruction_index] += 1
    if instructions[instruction_index] == "acc":
        accumulator += numbers[instruction_index]
    elif instructions[instruction_index] == "jmp":
        instruction_index += numbers[instruction_index]
        continue
    elif instructions[instruction_index] == "nop":
        pass
    else:
        print("Invalid Instruction")
    instruction_index += 1

print(accumulator)

#part 2
#not really sure how to do this, just gonna brute force cahnge every nop and jump instruction and see if it works
instruction_index = 0

while instruction_index < len(instructions) and instruction_index >= 0:
    if is_escapable(instruction_index):
        break
    else:
        instruction_index += 1

