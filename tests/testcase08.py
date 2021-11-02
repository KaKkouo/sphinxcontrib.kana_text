#!/usr/bin/python
import sys
import unittest

from src import KanaText

class testKanaText(unittest.TestCase):
    def test01_empty(self):
        term = KanaText('')
        self.assertEqual(repr(term), "<#empty>")
        self.assertEqual(term['kana'], None)
        self.assertEqual(term['hier'], "")

    def test02_raise(self):
        term = KanaText('用語零弐')
        with self.assertRaises(KeyError):
            text = term[2]
        with self.assertRaises(TypeError):
            text = term[(1, 1)]
        with self.assertRaises(KeyError):
            term['kana'] = "よみ"
        with self.assertRaises(KeyError):
            term[3] = "よみ"
        with self.assertRaises(TypeError):
            term[(1, 1)] = "よみ"

def main():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
