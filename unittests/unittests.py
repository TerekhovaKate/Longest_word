#!/usr/bin/env python3
# -*- mode: python -*-
# -*- coding: utf-8 -*-

"""
Unittests for FindTheLargestWord object
"""

import unittest
from pathlib import Path
from file_parser import FindTheLargestWord

THISDIR = Path(__file__).resolve().parent

SUFFIX_FILE = "test_file.txt"
PATH = str(Path(THISDIR, SUFFIX_FILE))

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.file = FindTheLargestWord(PATH)

    def test_raw_data(self):
        data = ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcde', 'edcba']
        self.assertTrue(self.file.raw_data == data)

    def test_clean_raw_data(self):
        expected = ['abcde', 'edcba']
        data_test = self.file.clean_raw_data()
        self.assertTrue(expected == data_test)

    def test_reverse(self):
        data_test = self.file.reverse_words()
        expected  = ['abcde', 'edcba', 'edcba', 'abcde']
        self.assertTrue(data_test == expected)

    def test_clean_raw_data_with_symbols_1(self):
        self.file.raw_data = ['Saint-Petersburg']
        clean_word = self.file.clean_raw_data()[0]
        self.assertTrue(clean_word == "Saint-Petersburg")

    def test_clean_raw_data_with_symbols_2(self):
        self.file.raw_data = ["asjbdsa=?,"]
        clean_word = self.file.clean_raw_data()[0]
        self.assertTrue(clean_word == "asjbdsa")

    def tearDown(self):
        pass


class TestStringMethodsNegative(unittest.TestCase):

    def test_1(self):
        file = "test_negative.txt"
        with self.assertRaises(SystemExit):
            FindTheLargestWord(file)

    def  test_2(self):
        file = "test_file_empty.txt"
        with self.assertRaises(SystemExit):
            FindTheLargestWord(file).clean_raw_data()


def suite():
    """
    Creating the test suite for positive and negative test classes
    :return: unittest suite
    """
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethodsNegative())
    suite.addTest(TestStringMethods())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())