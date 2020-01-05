# Given the below class:
class Cat:
    species = 'mammal'

    def __init__(self, name, age):
        self.name = name
        self.age = age


def find_oldest_cat(*args):
    return max(args)


# 1 Instantiate the Cat object with 3 cats
peanut = Cat('Peanut', 50)
garfield = Cat('Garfield', 4)
ambrose = Cat('Ambrose', 6)


# 2 Create a function that finds the oldest cat


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(
    f'The oldest cat is {find_oldest_cat(peanut.age,garfield.age,ambrose.age)} years old')
