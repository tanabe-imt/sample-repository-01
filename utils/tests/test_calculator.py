from unittest import TestCase

import numpy as np

from utils import calculator


class TestCalculator(TestCase):
  def test_add_01(_):
    a = np.array([1, 2])
    b = np.array([3, 4])

    actual = calculator.add(a, b)
    expected = np.array([4, 6])
    np.testing.assert_array_equal(actual, expected)

  def test_multiply_01(_):
    a = np.array([1, 2])
    b = np.array([3, 4])

    actual = calculator.multiply(a, b)
    expected = np.array([3, 8])
    np.testing.assert_array_equal(actual, expected)

  def test_divide_01(_):
    a = np.array([6, 12])
    b = np.array([3, 4])

    actual = calculator.divide(a, b)
    expected = np.array([2, 3])
    np.testing.assert_array_equal(actual, expected)

  def test_mod_01(self):
    a = np.array([7, 14])
    b = np.array([3, 4])

    actual = calculator.mod(a, b)
    expected = np.array([1, 2])
    np.testing.assert_array_equal(actual, expected)
