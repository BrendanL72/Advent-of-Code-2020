import fileinput

def is_valid(number):
    for number1 in preamble_numbers:
        for number2 in preamble_numbers:
            if number1 == number2:
                continue
            else:
                if number1 + number2 == number:
                    return True
    return False

def find_range(number):
    for lowest_index in range(len(numbers)):
        for highest_index in range(len(numbers)):
            if (sum(numbers[lowest_index:(len(numbers)-highest_index-1)]) == number):
                return min(numbers[lowest_index:(len(numbers)-highest_index-1)]), max(numbers[lowest_index:(len(numbers)-highest_index-1)])
    return 0,0
    

preamble_length = 25
preamble_numbers = []
numbers = []
invalid_number = 0
for line in fileinput.input(files = "advent9/advent9input.txt"):
    line = int(line.rstrip())
    if len(preamble_numbers) < preamble_length:
        pass
    else:
        if not is_valid(line):
            invalid_number = line
        preamble_numbers.pop(0)
    preamble_numbers.append(line)
    numbers.append(line)
print(invalid_number)

#part 2: find the range of numbers before the invalid number whose sum equals the invalid
ranged = find_range(invalid_number)
print(ranged[0] + ranged[1])