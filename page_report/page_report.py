import sys
import re
# retrieving file name from argv
filename = sys.argv[1]
# opening file to read
file = open(filename, "r")
my_dict = {}
my_list = []
errors = 0

# reading each line in file and saving urls in dict, counting them

for line in file:
    result = re.search('([a-z0-9.-]+\.[a-z]{2,4}(\s|/(\w+)))', line)
    try:
        if result.group(1) not in my_dict:
            my_dict[result.group(1)] = 1
        else:
            my_dict[result.group(1)] += 1
    except AttributeError:  # in case of invalid line
        errors += 1

# generate list of lists with the elements ordered by dict values and then
# by the keys alphabetically

for element in sorted(my_dict.items(), key=lambda kv: (-kv[1], kv[0])):
    my_list.append(element)

# showing results

for number in range(0, len(my_list)):
    print('"' + my_list[number][0] + '",' + str(my_list[number][1]))

# info about invalid lines

sys.stderr.write("Invalid log lines: {}\n".format(errors))
