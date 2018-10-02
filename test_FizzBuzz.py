import unittest
from main import *

class FizzBuzzTests(unittest.TestCase):

	def testReturnsTheValueOfEachMultipleOfThree(self):
        response = fizz_buzz()
        FizzCount = 3
        for index in range(len(response)):
            if FizzCount % 15 != 0:
                self.assertEquals(response[FizzCount-1], 'Fizz')
                FizzCount = FizzCount + 3
