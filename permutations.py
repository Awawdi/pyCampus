import itertools
counter = 0
list_of_bank_notes = [1, 1, 1, 1, 1, 5, 5, 10, 10, 10, 10, 10, 20, 20, 20]

for i in range(1, len(list_of_bank_notes)):
    options = set(itertools.combinations(list_of_bank_notes, i))
    for itr in options:
        list_of_current_option = list(itr)

        if sum(list_of_current_option) == 100:
            counter += 1
            print(list_of_current_option)

print("number of possible options is :" + str(counter))
