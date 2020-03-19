zoo_lst = []


class Animals:
    """A class used to represent an animal"""

    # initialize zoo name
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        """initializes new instance of Animal class, default value for 'hunger' is 0.
        :param name: name of the new Animal instance
        :param hunger: how much is the new Animal instance hungry
        :type name: str
        :type hunger: int
        """
        self._name = name
        self._hunger = hunger

    def get_name(self):
        """returns name of the instance.
        :return: name of the Animal instance
        :rtype: str
        """
        return self._name

    def is_hungry(self):
        """returns boolean value, True if Animal instance is hungry, False if not.
        :return: If Animal instance is hungry (_hunger > 0) returns True, else returns False
        :rtype: bool
        """
        return self._hunger > 0

    def feed(self):
        """"This method "feeds" the Animal by reducing the _hunger value by one."""
        self._hunger -= 1

    def talk(self):
        """This method """
        print("")


class Dog(Animals):
    """Dog class, used to represent an animal of type Dog, inherited from Animal class"""
    def talk(self):
        return "woof woof"

    def fetch_stick(self):
        print("There you go, sir!")


class Cat(Animals):
    """Cat class, used to represent an animal of type Cat, inherited from Animal class"""
    def talk(self):
        return "meow"

    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animals):
    """Skunk class, used to represent an animal of type Skunk, inherited from Animal class"""

    def __init__(self, name, hunger, stink_count=6):
        """initializes new instance of Skunk, set values to variables name, 'hunger' and 'stink_count'
        :param stink_count: how much is the Skunk "stinky", defaulted to 6
        :param name: name of Skunk
        :param hunger: hunger value of the Skunk
        :type name: str
        :type hunger: int
        :type stink_count: int
        """

        # call base class's initialize method to set 'name', 'hunger' values
        # initialize sub class '_stink_count' value (defaulted to '6')

        super(Skunk, self).__init__(name, hunger)
        self._stink_count = stink_count

    def talk(self):
        return "tsssss"

    def stink(self):
        print("Dear lord!")


class Unicorn(Animals):
    """Unicorn class, used to represent an animal of type Unicorn, inherited from Animal class"""
    def talk(self):
        return "Good day, darling"

    def sing(self):
        print("I’m not your toy...")


class Dragon(Animals):
    """Dragon class, used to represent an animal of type Dragon, inherited from Animal class"""

    def __init__(self, name, hunger, color="Green"):
        """initializes new instance of Dragon, set values to variables 'name', 'hunger' and '_color'
        :param color: set color of the Dragon instance, defaulted to 'Green'
        :param name: name of Dragon
        :param hunger: hunger value of the Dragon
        :type name: str
        :type hunger: int
        """

        # call base class's initialize method to set 'name', 'hunger' values
        # initialize sub class 'color' value (defaulted to 'Green')

        super(Dragon, self).__init__(name, hunger)
        self._color = color

    def talk(self):
        return "Raaaawr"

    def breath_fire(self):
        print("$@#$#@$")


def main():
    # Create new instances of 'Dog' , 'Cat' , 'Skunk' , 'Unicorn' and 'Dragon'
    # and add the instance to 'zoo_lst' list

    Brownie_Dog = Dog("Brownie", 10)
    zoo_lst.append(Brownie_Dog)

    Zelda_Cat = Cat("Zelda", 3)
    zoo_lst.append(Zelda_Cat)

    Stinky_Skunk = Skunk("Stinky", 0)
    zoo_lst.append(Stinky_Skunk)

    Keith_Unicorn = Unicorn("Keith", 7)
    zoo_lst.append(Keith_Unicorn)

    Lizzy_Dragon = Dragon("Lizzy", 1450)
    zoo_lst.append(Lizzy_Dragon)

    ###

    Doggo_Dog = Dog("Doggo", 80)
    zoo_lst.append(Doggo_Dog)

    Kitty_Cat = Cat("Kitty", 80)
    zoo_lst.append(Kitty_Cat)

    Stinky_Stinky_Jr = Skunk("Stinky Jr.", 80)
    zoo_lst.append(Stinky_Stinky_Jr)

    Clair_Unicorn = Unicorn("Clair", 80)
    zoo_lst.append(Clair_Unicorn)

    McFly_Dragon = Dragon("McFly", 80)
    zoo_lst.append(McFly_Dragon)

    ###

    # Loop through zoo_list, "feed" Animal instance as long as instance is "hungry"
    # "feeding" an animal will reduce '_hungry' property by 1.
    # "hungry" animal will still be hungry until '_hungry' property is more than zero

    for animal in zoo_lst:
        while animal.is_hungry():
            animal.feed()

        # for each Animal instance, print Animal type and name
        # for each Animal instance, invoke 'talk' method
        # 'talk' method is defined at base class (Animal) and overridden in each subclass

        print(animal.__class__.__name__ + " " + animal.get_name())
        print(animal.talk())

        # for each Animal instance, check what is the type of this instance, by using 'isinstance'
        # and invoke the relevant method. Each Animal instance has its own method.

        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    # Print zoo name by using base class Animal property 'zoo_name'
    print("Zoo Name is : " + Animals.zoo_name)


if __name__ == "__main__":
    main()
