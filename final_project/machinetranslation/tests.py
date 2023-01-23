import unittest
from translator import frenchToEnglish,englishToFrench

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        
        self.assertIsNotNone(a)
        self.assertEqual('Hello','Bonjour')

    def test_frenchToEnglish(self):
        self.assertIsNotNone(a)
        self.assertEqual('Bonjour','Hello')

if __name__ =='__main__'
    unittest.main()