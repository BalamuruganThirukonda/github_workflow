# Removed unnecessary import since pytest is not used directly
# import pytest

def test_calc_addition():
    # Function to test the output of 2+4
    output = 2 + 4
    assert output == 6


def test_calc_subtraction():
    # Function to test the output of 2-4
    output = 2 - 4
    assert output == -2


def test_calc_multiply():
    # Function to test the output of 2*4
    output = 2 * 4
    assert output == 8


def test_coucou():
    # Function to test if the output return 'hello'
    output = 'hello'
    assert output == 'hello'
