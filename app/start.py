import requests


class MyClass:
    """ My first class
    And it's so great
    """

    def __init__(self, my_list):
        self.my_list = my_list

    def __len__(self):
        return len(self.my_list)

    def __repr__(self):
        return f"My List: {self.my_list}"

    def print_my_list(self):
        print(self.my_list)

    def append_list(self, addition: int) -> list:
        """ Adds values to a list

        Args:
            addition: value to be added to list

        Returns:
            A list with the appended value
        """
        self.my_list.append(addition)
        return self.my_list


class Car:
    """
    Bellow example is taken from "Python Trickss The Book" By Dan Bader
    Great book, get your own copy
    """

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __repr__(self):
        return f"Car({self.color!r}, {self.mileage!r})"

    # def __repr__(self):
    """The benefit is you won’t have to modify the __repr__ implementation
        when the class name changes.
        But less readable
    """
    #    return (f'{self.__class__.__name__}('f'{self.color!r}, {self.mileage!r})')


mylist = [1, 2, 3]

# Create our class
myclass = MyClass(mylist)
myclass.print_my_list()

# Add a value to our list
myclass.append_list(4)
myclass.print_my_list()

# Comment out __len__ and see what happens
print(len(myclass))

# Comment out __repr__ and see what happens
print(myclass)

my_car = Car("Red", 200)
print(my_car)
