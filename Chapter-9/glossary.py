"""
This module is my solution to exercise 9-13.
"""
from collections import OrderedDict


class Glossary():
    """
    A collection of words with their defenition.
    """
    def __init__(self):
        """Intialize the glossary"""
        self.glossary = OrderedDict()
        self.glossary["Variable"] = (
            "A named object that represents a statement.")
        self.glossary["Statement"] = "A value."
        self.glossary["Class"] = (
            "A model that represents" + "a real world object."
            )

    def print_glossary(self):
        """Print the glossary"""
        for word, definition in self.glossary.items():
            print(word.title() + ": " + definition)


dictionary = Glossary()
dictionary.print_glossary()
