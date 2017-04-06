# Jean Tu
# ITP 115, Spring 2017
# Lab L3
# jeantu@usc.edu

lines = 0
numSpaces = 19
numSymbols = 1
while lines < 10:
    print(" " * numSpaces, "^ " * numSymbols)
    numSpaces = numSpaces - 2
    numSymbols  = numSymbols + 2
    lines = lines + 1
