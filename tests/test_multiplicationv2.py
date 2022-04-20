import numpy as np
import pytest

from multiply_package import Multiplication

TESTDATA = [(0, 0), (5, 10), (-7, -14), (6 / 17, (6 / 17) * 2), (np.pi, 2 * np.pi)]


class TestMultiplication:
    @pytest.mark.parametrize(["input", "expected"], TESTDATA)
    def test_multiplication(self, input, expected):
        m = Multiplication(2)

        actual = m.multiply(input)
        assert actual == expected
