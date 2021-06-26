#!/usr/bin/env python3

from sys import argv, exit

def main():
    argc = len(argv)

    if argc < 1 or argc % 2 != 1: # This file counts as an argument too
        print('Use: <filename> input1 output1 input2 output2 etc.')
        exit(1)

    # Turn argv of [input1, output1, input2, output2, ...] into
    # [(input1, output1), (input2, output2), ...]
    for arg in list(zip(*[iter(argv[1:])] * 2)):
        with open(arg[0], 'r') as inputFile:
            with open(arg[1], 'w') as outputFile:
                convertToSub(inputFile, outputFile)

def convertToSub(inputFile, outputFile):
    counter = 1
    for line in inputFile:
        if line == '\n': # check if line is empty
            continue

        outputFile.write(str(counter) + '\n')
        outputFile.write('00:00:00,000 --> 00:00:00,000\n')
        outputFile.write(line)
        outputFile.write('\n')

        counter += 1

main()
