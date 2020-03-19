"""with open(r"c:\python\names.txt") as f:
    print(max(f.read().splitlines()))"""
""""------------------------------------------------------------------"""
"""with open(r"c:\python\names.txt") as f:
    print(sum(map(lambda x: len(x), f.read().splitlines())))"""
"""-----------------------------------------------------------------------"""
"""with open(r"c:\python\names.txt") as f:
    names = f.read().splitlines()
names.sort(key=lambda y: len(y))
print("\n".join(list(filter(lambda xy: len(xy) == len(names[0]), names))))"""
"""-----------------------------------------------------------------------"""
with open(r"c:\python\names.txt") as f: names = f.read().splitlines()
with open(r"c:\python\names_length2.txt", 'w') as write_to_file:
    write_to_file.write("\n".join((list(map(lambda xy: str(len(xy)), names)))))
