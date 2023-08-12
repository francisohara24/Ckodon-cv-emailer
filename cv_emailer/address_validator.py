"""Validate email addresses in resume using extractor module"""
from os import listdir
import extractor

for cv in listdir("../data/current"):
    path_to_cv = "../data/current/" + cv
    address = extractor.extract_address(path_to_cv)
    print(address)
