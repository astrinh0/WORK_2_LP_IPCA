# main.py

from Parser import Parser

with open("ex1.logo", mode="r") as fh:
    contents = fh.read()

parser = Parser()
parser.Parse(contents)
