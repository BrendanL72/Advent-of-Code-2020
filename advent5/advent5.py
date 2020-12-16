import fileinput
max_seat_num = 0
min_seat_num = 24902940
#use a dictionary for hashing, O(1) instead of O(n)
seats = {}
for line in fileinput.input(files = "advent5input.txt"):
    line = line.rstrip()
    rows = line[:7]
    cols = line[-3:]
    #print(rows, cols)
    row_num = 0
    col_num = 0
    for index in range(len(rows)):
        if rows[len(rows) - index - 1] == 'B':
            row_num += 2 ** index
    for index in range(len(cols)):
        if cols[len(cols) - index - 1] == 'R':
            col_num += 2 ** index
    seat_num = row_num * 8 + col_num
    #print(row_num, col_num, seat_num)
    seats[seat_num] = row_num
    max_seat_num = seat_num if seat_num > max_seat_num else max_seat_num
    min_seat_num = seat_num if seat_num < min_seat_num else min_seat_num
print(min_seat_num, max_seat_num)
for x in range(min_seat_num, max_seat_num):
    if x not in seats.keys():
        if x-1 in seats.keys() and x+1 in seats.keys():
            print(x)
