import math
import sqlite3
import pytest
import calculator


def power(num, power1):
    return num ** power1
print(power(4,2))

def sqrt(num):
    return math.sqrt(num)
print(sqrt(9))

def factorial(num):
    if num < 0:
        raise ValueError('cant do factorial with negative num')
    return math.factorial(num)
print(factorial(3))
print(factorial(5))

def power(num, power1):
    return num ** power1
def test_power():
    res = (2, 4)
    assert res == 16, f"Test failed: expected 16, got{res}"
test_power()

def sqrt(num):
    return math.sqrt(num)
def test_sqrt():
    result = (3, 2)
    assert result == 9, f"Test failed: expected 16, got{result}"
test_sqrt()

def test_sqrt_positive():
    result = math.sqrt(25)
    assert result == 5, f"Test failed: expected 5, got {result}"
test_sqrt_positive()

def test_sqrt_negative():
    with pytest.raises(ValueError):
        math.sqrt(-5)
test_sqrt_negative()

def test_factorial_4():
    result = math.factorial(4)
    assert result == 24, f"Test failed: expected 24, got {result}"
test_factorial_4()

def test_factorial_5():
    result = math.factorial(5)
    assert result == 120, f"Test failed: expected 120, got {result}"
test_factorial_5()

def test_factorial_negative():
    with pytest.raises(ValueError):
        math.factorial(-3)
test_factorial_negative()