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
	
	def testReturnsTheValueOfEachMultipleOfFive(self):
        response = fizz_buzz()
        BuzzCount = 5
        for index in range(len(response)):
            if BuzzCount % 15 != 0:
                self.assertEquals(response[BuzzCount-1], 'Buzz')
                BuzzCount = BuzzCount + 5
				
	def testReturnsTheValueOfEachMultipleOfBothThreeAndFive(self):
        response = fizz_buzz()
        FizzBuzzCount = 15
        for index in range(len(response)/15):
            self.assertEquals(response[FizzBuzzCount-1], 'FizzBuzz')
            FizzBuzzCount = FizzBuzzCount + 15
			
	def testReturnsTheValue(self):
        response = fizz_buzz()
        for index in range(len(response)):
            if index % 3 != 0 and index % 5 != 0 and index % 15 != 0:
                self.assertEquals(response[index-1], index)
