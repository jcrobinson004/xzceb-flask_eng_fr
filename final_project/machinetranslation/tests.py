import unittest
from translator import __french_to_english__, __english_to_french__

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):

        self.assertIsNotNone(self)
        self.assertEqual(__english_to_french__('Hello'),([{'translation' :  'Bonjour'}]))

    def test_french_to_english(self):
        self.assertIsNotNone(self)
        self.assertEqual(__french_to_english__('Bonjour'),([{'translation' :  'Hello'}] ))

unittest.main()
