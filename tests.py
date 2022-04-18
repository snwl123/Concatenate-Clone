import unittest
import main

class testCatClone(unittest.TestCase):

    def testCatCloneSuccess(self):
        listOfWords = ['1', '2', '3']
        self.assertIsInstance(main.catClone(listOfWords), str)
        self.assertEqual(main.catClone(listOfWords), '123')

    def testCatCloneFailure(self):
        listOfNumbers = [1, 2, 3]
        self.assertRaises(TypeError, main.catClone, listOfNumbers)