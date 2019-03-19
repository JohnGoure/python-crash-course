"""Module for exercise 9-14."""
from random import randint


class Die():
    """This model creates dice"""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        print(
            "Your " + str(self.sides) +
            " die rolled a " +
            str(randint(1, self.sides)) + "!"
            )

firstDie = Die()
secondDie = Die(10)
thirdDie = Die(20)

for x in range(10):
    firstDie.roll_dice()

for x in range(10):
    secondDie.roll_dice()

for x in range(10):
    thirdDie.roll_dice()
