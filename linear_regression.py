# Uses linear regression to solve a problem
import numpy as np
import re


def numbers_from_wrong_answers():
    file = open('wrong_answers.txt', 'r').read()
    file_matches = re.sub('\nIt should work for random inputs too: -1', '', file).split('\n')
    isolate_digits = '\n'.join([' '.join(re.findall('\d+', match)) for match in file_matches])
    return isolate_digits


def tests_from_numbers():
    filesplit = open('regression_values.txt', 'r').read().split('\n')
    restring_digits = []
    for digits in filesplit:
        dit = digits.split(' ')
        restring_digits.append(f'test.assert_equals(psion_power_points({dit[0]},{dit[1]}), {dit[2]})')
    return '\n'.join(restring_digits)


def wrong_answers_from_numbers():
    filesplit = open('regression_values.txt', 'r').read().split('\n')
    restring_digits = []
    for digits in filesplit:
        dit = digits.split(' ')
        restring_digits.append(f'Testing for {dit[0]} and {dit[1]}\n'
                               f'It should work for random inputs too: -1 should equal {dit[2]}')
    return '\n'.join(restring_digits)


def numbers_from_tests():
    filesplit = open('tests.txt', 'r').read().split('\n')
    isolate_digits = '\n'.join([' '.join(re.findall('\d+', match)) for match in filesplit])
    return isolate_digits


def psion_power_point_regression():
    filesplit = open('regression_values.txt', 'r').read().split('\n')
    levels, score, results = [], [], []
    for value in filesplit:
        values = [int(x) for x in value.split(' ')]
        levels.append(values[0])
        score.append(values[1])
        results.append(values[2])
    levels, score, results = np.array(levels), np.array(score), np.array(results)
    return levels


if __name__ == '__main__':
    # print(numbers_from_wrong_answers())
    print(psion_power_point_regression())
