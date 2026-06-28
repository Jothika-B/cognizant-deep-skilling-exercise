test_calculator.py
import pytest
from calculator import *

# Test 1
def test_add(sample_numbers):
    a, b = sample_numbers
    assert add(a, b) == 25

# Test 2
def test_subtract(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 15

# Test 3
def test_multiply(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 100

# Test 4
def test_divide(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 4

# Test 5
def test_add_negative():
    assert add(-5, -5) == -10

# Test 6
def test_subtract_negative():
    assert subtract(-10, -5) == -5

# Test 7
def test_multiply_zero():
    assert multiply(10, 0) == 0

# Test 8
def test_divide_float():
    assert divide(10, 4) == 2.5

# Test 9
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

# Test 10
def test_large_numbers():
    assert multiply(1000, 1000) == 1000000

# Test 11
def test_add_decimal():
    assert add(2.5, 3.5) == 6
