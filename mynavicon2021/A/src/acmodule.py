t"""Main function for module"""
import pytest
from sys import argv
from sys import stdin


def data_input(file: str):
    if(file):
        stdin = open(file)
    a, b, c = [int(x) for x in stdin.readline().rstrip().split()]
    return a, b, c


def ap(a, b, c):
    return ((a-b) == (b-c) or
            (a-c) == (c-b) or
            (b-a) == (a-c))


def main():
    print(ap(data_input()))


data_set = ['data/data1.txt',
            'data/data2.txt',
            'data/data3.txt']


@pytest.mark.parametrize('file', data_set)
class Testmodule():
    def test_filetype(self, file):
        assert type(file) is str

    def test_input(self, file):
        print(file, type(file))
        a, b, c = data_input(file)
        assert ((type(a) is int) and
                (type(b) is int) and
                (type(c) is int))

    def test_ap(self, file):
        assert type(ap(1, 2, 3)) is bool


if __name__ == '__main__':
    main()
