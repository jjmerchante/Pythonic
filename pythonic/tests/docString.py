"""
Module for subtracting and summing two variables,
the docString in the functions, class and methods aren't the best
but are for testing
"""

def subtraction(num_1, num_2):
    """ Returns the subtraction of the two variables """
    return num_1 - num_2

def sum(num_1, num_2):
    """ Returns the sum of the two variables """
    return num_1 + num_2


class UniqueNumber():
    """
    stupid class that store a number and you can add and
    subtract numbers from it
    """
    def __init__(self, number=0):
        """ UniqueNumber constructor """
        self.number = number

    def add(self, number):
        """ Add a number and returns the result"""
        self.number += number
        return self.number

    def subtract(self, number):
        """ subtract a number and returns the result"""
        self.number -= number
        return self.number

    def getNumber(self):
        """ get the number stored """
        return self.number

    def setNumber(self, number):
        """ change the number stored and return the previous """
        prevNumber = self.number
        self.number = number
        return prevNumber
