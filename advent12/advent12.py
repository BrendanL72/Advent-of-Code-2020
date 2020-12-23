import fileinput

#the initial direction is East
directions = ["N", "E", "S", "W"]
current_direction = 'E'
east_steps = 0
north_steps = 0
sign = 1

for line in fileinput.input(files= "advent12/advent12input.txt"):
    line = line.rstrip()
    command = line[0]
    magnitude = int(line[1:])
    if command == 'F':
        command = current_direction
    elif command == 'R':
        current_direction = directions[(directions.index(current_direction) + int(magnitude/90))% len(directions)]
    elif command == 'L':
        current_direction = directions[(directions.index(current_direction) - int(magnitude/90))% len(directions)]

    if command == 'N':
        north_steps += magnitude
    elif command == 'S':
        north_steps -= magnitude
    elif command == 'E':
        east_steps += magnitude
    elif command == 'W':
        east_steps -= magnitude

print(abs(east_steps) + abs(north_steps), east_steps, north_steps)