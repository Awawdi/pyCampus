

def parse_ranges(ranges_string):
    str1 = ranges_string.split(",")
    str2 = str1.split("-")
    print(str2)



    gen3 = (i.replace("-",",") for i in str1)
    print(list(next(gen3)))
    gen1 = (i.split(",") for i in ranges_string)
    gen2 = (i.replace("-",",") for i in ranges_string)
    print(list(next(gen1)))
    print(list(gen2))
    #1-2,4-4,8-10

parse_ranges("1-2,4-4,8-10")
#print(list(parse_ranges("1-2,4-4,8-10")))
#print(list(parse_ranges("0-0,4-8,20-21,43-45")))
