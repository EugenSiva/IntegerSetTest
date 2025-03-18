class IntegerSet:
    def __init__(self, numbers):
        self.numbers = set(numbers)

    def sum_elements(self):
        return sum(self.numbers)

    def arithmetic_mean(self):
        return sum(self.numbers) / len(self.numbers) if self.numbers else 0

    def max_element(self):
        return max(self.numbers) if self.numbers else None

    def min_element(self):
        return min(self.numbers) if self.numbers else None


import pytest


def test_integer_set():
    num_set = IntegerSet([1, 2, 3, 4, 5])

    assert num_set.sum_elements() == 15
    assert num_set.arithmetic_mean() == 3.0
    assert num_set.max_element() == 5
    assert num_set.min_element() == 1

    empty_set = IntegerSet([])
    assert empty_set.sum_elements() == 0
    assert empty_set.arithmetic_mean() == 0
    assert empty_set.max_element() is None
    assert empty_set.min_element() is None