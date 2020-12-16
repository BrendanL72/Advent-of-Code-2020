import fileinput
file_name = "advent6/advent6input.txt"
def part1():
    sum_questions = 0
    #use a dictionary for hashing
    group_answers = {}
    for line in fileinput.input(files = file_name):
        line = line.rstrip()
        if line == "":
            #end of group
            sum_questions += len(group_answers.keys())
            #reset group
            print(group_answers)
            group_answers = {}
        else:
            for letter in line:
                group_answers[letter] = 0
    print(sum_questions)

def part2():
    sum_questions = 0
    #use a dictionary for hashing
    group_answers = {}
    first_line = {}
    for line in fileinput.input(files = file_name):
        line = line.rstrip()
        if line == "":
            #end of group
            sum_questions += len(group_answers.keys())
            print(group_answers)
            #reset group
            group_answers = {}
            first_line = {}
        else:
            #check if the first person in the group.
            
            if len(first_line.keys()) == 0:
                for letter in line:
                    first_line[letter] = group_answers[letter] = 0
            else:
                new_answers = {}
                for letter in group_answers:
                    if letter in line:
                        new_answers[letter] = 0
                group_answers = new_answers.copy()
                
    print(sum_questions)


def main():
    part1()
    part2()

main()
