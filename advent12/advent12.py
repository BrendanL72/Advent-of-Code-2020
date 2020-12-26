import fileinput

#the initial direction is East
directions = ["N", "E", "S", "W"]
current_direction = 'E'
east_steps = 0
north_steps = 0

waypoint_north_pos = 1
waypoint_east_pos = 10


for line in fileinput.input(files= "advent12/advent12input.txt"):
    line = line.rstrip()
    command = line[0]
    magnitude = int(line[1:])
    if command == 'F':
        east_steps += waypoint_east_pos * magnitude
        north_steps += waypoint_north_pos * magnitude
    elif command == 'L':
        command = "R"
        magnitude = 360 - magnitude

    if command == 'R':
        for x in range(int(magnitude/90)):
            storage = waypoint_north_pos
            waypoint_north_pos = -1 * waypoint_east_pos
            waypoint_east_pos = storage
    elif command == 'N':
        waypoint_north_pos += magnitude
    elif command == 'S':
        waypoint_north_pos -= magnitude
    elif command == 'E':
        waypoint_east_pos += magnitude
    elif command == 'W':
        waypoint_east_pos -= magnitude

print(abs(east_steps) + abs(north_steps), east_steps, north_steps)