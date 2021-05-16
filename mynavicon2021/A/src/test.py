# from sys import stdin
import pytest


data_set = ['data/data1.txt',
            'data/data2.txt',
            'data/data3.txt']

'''
def data_input():
    a, b, c = stdin.readline().rstrip().split()
    return a, b, c
'''


@pytest.mark.parametrize("file", data_set)
def test_parametrize():
    print(file)


#print(data_input())
