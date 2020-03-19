with open(r"capitals.txt") as file:
    single_line_gen = (line for line in file)
    capitals_and_cities = (i.replace("\n", "").split(",") for i in single_line_gen)
    capitals_dict = dict(capitals_and_cities)

print(capitals_dict)