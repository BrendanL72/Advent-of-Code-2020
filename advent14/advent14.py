import fileinput
mask = ""
mem_location = 0
memory = {}
for line in fileinput.input(files= "advent14/advent14input.txt"):
   line = line.rstrip().split(" = ")
   if line[0] == "mask":
      mask = line[1]
   else:
      mem_location = line[0][4:-1]
      data = bin(int(line[1]))
      data = str(data)[2:].zfill(36)
      for index in range(len(mask)):
         if mask[index] != "X":
            data = data[:index] + mask[index] + data[index+1:]
      memory[mem_location] = data
   
#iterate through memory and add everything together
sum = 0
for key in memory:
   sum += int(memory[key], 2)

print(sum)