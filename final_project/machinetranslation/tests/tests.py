import unittest
from translator import *

class TestE2FTranslation(unittest.TestCase):
    def test_null_value(self):
        self.assertEqual(englishToFrench(None), "You need to send an input")

    
    def test_valid_arguement(self):
        self.assertEqual(englishToFrench("Hello"), "Bonjour")

class TestF2ETranslation(unittest.TestCase):
    def test_null_value(self):
        self.assertEqual(frenchToEnglish(None), "You need to send an input")
    
    def test_valid_arguement(self):
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello")

if __name__ == '__main__':
    unittest.main()