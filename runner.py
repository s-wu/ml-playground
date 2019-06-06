"""This file runs the code in solver.py. You shouldn't need to change anything here"""

import sys
import solver

if __name__ == '__main__':
    if len(sys.argv) < 2 or sys.argv[1] not in ['easy', 'medium', 'hard', 'challenge']:
        print("Sample usage: python runner.py easy")
        exit()

    dataset = sys.argv[1]
    file = 'input-{}.txt'.format(dataset)
    answer = 'output-{}.txt'.format(dataset)

    inp = ""

    with open(file, 'r') as file:
        for line in file:
            inp = line.strip()

    res = solver.answer(inp)

    outp = ""

    with open (answer, 'r') as answer:
        for line in answer:
            outp = line.strip()

    if len(res) != len(outp):
        print("Formatting error. Result has length {} instead of {}.".format(len(res), len(outp)))
    else:
        ntot = len(res)
        ncorrect = 0
        for i in range(len(res)):
            if res[i] == outp[i]:
                ncorrect += 1

        print("{:.2f}% correct".format(100 * ncorrect / ntot))