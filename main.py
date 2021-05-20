# coding=utf-8

import argparse
import numpy as np
from scipy.signal import fftconvolve


def find_bugs(bug_path, landscape_path):
    # Load files
    landscape_file = open(landscape_path, "r")
    landscape = [bytearray(line[:-1]) for line in landscape_file]
    if len(landscape[-1]) is 0:
        landscape = landscape[:-1]
    # Check if landscape is valid
    for line in landscape:
        if len(line) != len(landscape[0]):
            raise Exception('Invalid landscape, all lines must be same length')
    landscape = np.array(landscape)

    bug_file = open(bug_path, "r")
    bug = [line[:-1] for line in bug_file]
    if len(bug) is 0:
        raise Exception('Bug must not be empty')
    bug_size = [len(bug), len(max(bug, key=len))]

    # Load bug matrix, interpret spaces as values that can be ignored
    bug_matrix = np.zeros(bug_size)
    for y, line in enumerate(bug):
        for x, letter in enumerate(bytearray(line, "utf8")):
            bug_matrix[y, x] = letter if letter != 32 else 0

    # Compute correlation
    reversed_bug = np.flipud(np.fliplr(bug_matrix))
    correlation = fftconvolve(landscape, reversed_bug.conj(), mode='valid')

    # Compute perfect match value
    match_sum = np.sum(np.square(bug_matrix))

    # Find all perfect matches
    correlation = np.round(correlation, decimals=1)
    matches = np.where(correlation == match_sum)
    return len(matches[0])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Find bugs in a landscape. See README.md.')
    parser.add_argument('bug_path', help='Path to bug file')
    parser.add_argument('landscape_path', help='Path to landscape file')

    args = parser.parse_args()
    print find_bugs(args.bug_path, args.landscape_path)