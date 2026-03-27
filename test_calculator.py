# test_calculator.py
import pytest
from calculator import add, subtract, multiply, divide, factorial, is_even

# ── Unit Tests ──────────────────────────────────────────────

class TestAdd:
    def test_positive_numbers(self):
        assert add(2, 3) == 5

    def test_negative_numbers(self):
        assert add(-1, -1) == -2

    def test_zero(self):
        assert add(0, 0) == 0

    def test_float(self):
        assert add(1.5, 2.5) == 4.0


class TestSubtract:
    def test_basic(self):
        assert subtract(10, 4) == 6

    def test_negative_result(self):
        assert subtract(3, 10) == -7


class TestMultiply:
    def test_positive(self):
        assert multiply(3, 4) == 12

    def test_by_zero(self):
        assert multiply(5, 0) == 0

    def test_negative(self):
        assert multiply(-2, 3) == -6


# ── Boundary / Edge Case Tests ────────────────────────────

class TestDivide:
    def test_normal_division(self):
        assert divide(10, 2) == 5.0

    def test_divide_by_zero_raises_error(self):
        with pytest.raises(ValueError):
            divide(10, 0)

    def test_float_result(self):
        assert divide(7, 2) == 3.5


class TestFactorial:
    def test_zero(self):          # boundary: 0! = 1
        assert factorial(0) == 1

    def test_one(self):
        assert factorial(1) == 1

    def test_positive(self):
        assert factorial(5) == 120

    def test_negative_raises_error(self):   # boundary: invalid input
        with pytest.raises(ValueError):
            factorial(-1)


# ── Black-Box Tests (only care about output) ─────────────

class TestIsEven:
    def test_even_number(self):
        assert is_even(4) == True

    def test_odd_number(self):
        assert is_even(3) == False

    def test_zero_is_even(self):
        assert is_even(0) == True

    def test_negative_even(self):
        assert is_even(-2) == True