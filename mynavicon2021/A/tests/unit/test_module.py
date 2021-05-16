"""Test the module"""

import acmodule


def test_input():
    a, b, c = acmodule.input()
    assert ((type(a) is int) and
            (type(b) is int) and
            (type(c) is int))


def test_ap():
    assert type(acmodule.ap()) is bool
