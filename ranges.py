def parse_ranges(ranges_string):


    gen = (w.split("-") for w in ranges_string.split(","))
    return (i for i in (itr for itr in gen))

    # for permutation in itertools.permutations([0, 5, 6, 9]):


print(list(parse_ranges("1-2,4-4,8-10")))
