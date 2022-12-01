from itertools import groupby

input_list = 'input2'

with open(input_list) as f:
    lines = [line.rstrip('\n') for line in f]


# group lists into nested list based on the empty element gaps
group_list = [list(g) for k, g in groupby(lines, key=bool) if k]

# make sure everything is an int just in case 
new_list = [list(map(int, x)) for x in group_list]

# sum each element in that list so we can do things to it
sum_list = list(map(sum, new_list))

#######
# part 1
highest = max(sum_list) 
print("part 1 " + str(highest))

#######
# part 2
sum_list.sort(reverse=True)
top_three = sum_list[0:3]
print("part 2 " + sum(top_three))

