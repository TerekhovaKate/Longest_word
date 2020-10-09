#!/usr/bin/env python3
# -*- mode: python -*-
# -*- coding: utf-8 -*-

import re
from pathlib import Path
import argparse
import logging
logging.basicConfig(level=logging.DEBUG)

THISDIR = Path(__file__).resolve().parent

class FindTheLargestWord():

    def __init__(self, file):
        self.raw_data = self._check_if_file(file)

    @staticmethod
    def _check_if_file(file):
        """

        :param file: user input-> path to the file
        :return: the list of spited words
        """
        try:
            logging.debug("Opening file {}".format(file))
            with open(file, encoding="utf-8") as file:
                words = file.read().split()
                return words
        except Exception as e:
            logging.error(e)
            exit(-1)

    def clean_raw_data(self):
        """

        :return: the longest word
        """
        if self.raw_data:
            new_list = []
            logging.debug("Cleaning the words and removing the special characters [!,*)@#%(&$_?.^=]")
            for i in self.raw_data:
                final = [re.sub('[!,*)@#%(&$_?.^=]', '', k) for k in i.split("\n")][0].split("\n")[0]
                if final not in new_list and final != '':
                    new_list.append(final)
            logging.debug("Found {} the original words in the text file ".format(len(new_list)))
            le = max(len(x) for x in new_list)
            logging.debug("The maximum characters length {}".format(le))
            return [x for x in new_list if len(x) == le]
        else:
            logging.error("The file is empty. No input data")
            exit(-1)

    def reverse_words(self):
        """

        :return: list of data
        """
        words = self.clean_raw_data()
        final = []
        logging.debug("Found {} the longest words in the text file".format(len(words)))
        for i in range(len(words)):
            final.extend([words[i], words[i][::-1]])
            print("Original word # {}: {}:".format(i, words[i]))
            print("Transpose word # {}: {}".format(i, words[i][::-1]))
        return final

if __name__ == "__main__":

    suffix = "example.txt"
    path = str(Path(THISDIR, suffix))
    parser = argparse.ArgumentParser()
    parser.add_argument('--file',  type=str, help="please enter the file path", default=path)
    args = parser.parse_args()
    FindTheLargestWord(args.file).reverse_words()


