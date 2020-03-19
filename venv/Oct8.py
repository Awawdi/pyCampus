class Animals:
    count_animals = 0

    def __init__(self, name="Octavio"):
        self.name = name
        self._age = 19
        Animals.count_animals+=1

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def birthday(self):
        self._age+=1

    def get_age(self):
        return self._age

def main():
        Oct1 = Animals("Octavia")
        Oct2 = Animals()

        print(Oct1.get_name())
        print(Oct2.get_name())

        Oct1.set_name("The Maestro")
        print(Oct1.get_name())

        Oct1.birthday()
        print(Oct1.get_age())
        print(Oct2.get_age())

        print(Animals.count_animals)
main()