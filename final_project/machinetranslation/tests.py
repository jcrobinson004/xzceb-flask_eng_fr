import unittest
from translator import frenchToEnglish,englishToFrench

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        
        self.assertIsNotNone(self)
        self.assertEqual(englishToFrench('Hello'),'Bonjour')

    def test_frenchToEnglish(self):
        self.assertIsNotNone(self)
        self.assertEqual(frenchToEnglish('Bonjour'),'Hello')

unittest.main()
