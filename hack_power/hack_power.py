# def hack_calculator(hack, letters, phrases):
def hack_calculator(hack: str):
    letters = {'a': 1, 'b': 2, 'c': 3}
    phrases = {'ba': 10, 'baa': 20}
    points = 0
    single_points = 0

# checking if every letter in string is in dict letters

    def check_letters():
        for letter in hack:
            if letter not in letters:
                return False
        return True

# counting points from phrases

    def count_phrase_bonus(string_to_hack):
        bonus = 0
        my_list = []

        # adding existing phrases from string_to_hack to my_list array

        for phrase in phrases:
            if phrase in string_to_hack:
                my_list.append([phrases[phrase], phrase])
        my_list.sort(reverse=True)  # reverse sorting by points

        for array_item in my_list:
            bonus += string_to_hack.count(array_item[1]) * phrases[array_item[1]]

            # removing counted phrases from string_to_hack to provide overlapping

            string_to_hack = string_to_hack.replace(array_item[1], "")
        return bonus

# counting points from letters

    if check_letters():
        for element in letters:
            if element in hack:
                amount = hack.count(element)
                for item in range(1, amount+1):
                    single_points += item * letters[element]
                points += single_points
                single_points = 0
        return print(points + count_phrase_bonus(hack))
    else:
        return print(0)


hack_calculator('baaca')

# Optional (extra credit):

# I could change necessary parameters in function hack_calculator so it could take phrases and
# letters dictionaries, and later use them in my program to calculate power of hacks.
# Function hack_calculator would look like this def hack_calculator(hack, letters, phrases): and
# calling function would look like this hack_calculator(hack='advantage', letters={'a': 1,
# 'd': 2, 'e': 5, 'g': 2, 'n': 1, 't': 4, 'v': 7}, phrases={'ad': 10, 'ant': 13, 'age': 24,
# 'van': 13, 'tag': 5})


# hack_calculator(hack='advantage',
# letters={'a': 1, 'd': 2, 'e': 5, 'g': 2, 'n': 1, 't': 4, 'v': 7},
# phrases={'ad': 10, 'ant': 13, 'age': 24, 'van': 13, 'tag': 5})
