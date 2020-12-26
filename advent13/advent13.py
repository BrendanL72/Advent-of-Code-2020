import fileinput

#brute force finding inverse function, input is small enough to not matter
def find_inverse_mod(num, mod):
   for x in range(mod):
      if (num * x) % mod == 1:
         return x

buses = []

data = fileinput.input(files= "advent13/advent13input.txt")
time_stamp = int(data[0].rstrip())
buses = data[1].rstrip().split(",")

min_time = 0
fastest_bus = 0

#I am following the Chinese Remainder Theorum formula, so I don't have very good var names
big_time_stamp = 0
big_modulo = 1
big_n = 1
index = 0

for bus in buses:
   #part 1
   if bus != "x":
      bus = int(bus)
      wait_time = bus - time_stamp % bus
      if min_time == 0:
         min_time = wait_time
      elif min_time > wait_time:
         min_time = wait_time 
         fastest_bus = bus
      big_modulo *= bus

print(fastest_bus * min_time, min_time, fastest_bus) 

   #part 2: Chinese Remainder Theorem
for bus in buses:
   if bus != "x":
      bus = int(bus)
      big_n = int(big_modulo/bus)
      thingy = bus - index
      inversey = find_inverse_mod(big_n, bus)
      big_time_stamp += thingy * big_n * inversey
      #print(bus, big_n, thingy, inversey, big_time_stamp, (inversey * big_n) % bus)
   index += 1


print(big_time_stamp % big_modulo)