import fileinput
#read through each line


def find_gold(bag):
   if "shiny gold" in bag_list[bag]:
      return True
   elif len(bag_list[bag]) == 0:
      return False
   else:
      for big_bag in bag_list[bag]:
         if find_gold(big_bag):
            return True

def find_nested_bags(bag):
   sum = 0
   if len(bag_list[bag]) == 0:
      return 1
   else:
      for key in bag_list[bag]:
         thing = int(bag_list[bag][key]) * find_nested_bags(key)
         sum += thing
   return sum

def find_unnested_bags(bag):
   sum = 0
   if len(bag_list[bag]) == 0:
      return 0
   else:
      for key in bag_list[bag]:
         if len(bag_list[key]) > 0:
            sum += int(bag_list[bag][key])
         sum += int(bag_list[bag][key]) * find_unnested_bags(key)
   return sum

bag_list = {}
for line in fileinput.input(files= "advent7/advent7input.txt"):
   line = line.rstrip()
   bags = line.split(" contain ")
   big_bag = bags[0]
   big_bag_attr = big_bag.split()
   big_bag_name = big_bag_attr[0] + " " + big_bag_attr[1]
   small_bags = bags[1].split(",")
   #print(big_bag, small_bags)
   nested_bags = {}
   for bag in small_bags:
      bag_attr = bag.split()
      if (bag_attr[0] != "no"):
         nested_bags[bag_attr[1] + " " +bag_attr[2]] = bag_attr[0]
   bag_list[big_bag_name] = nested_bags

num_bags = 0

#print(bag_list)

#part 1
for big_bag in bag_list:
   if find_gold(big_bag):
      num_bags += 1

print(num_bags)

#part 2: find the number of bags inside the shiny gold one
print(find_nested_bags("shiny gold")+find_unnested_bags("shiny gold"))

