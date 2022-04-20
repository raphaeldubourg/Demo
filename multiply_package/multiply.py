import numpy as np


class Multiplication:
    """
    Instantiate a multiplication operation.
    Numbers will be multiplied by the given multiplier.

    :param multiplier: The multiplier.
    :type multiplier: int
    """

    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, number):

        return np.dot(number, self.multiplier)


# Instantiate a Multiplication object
multiplication = Multiplication(2)

# Call the multiply method
print(multiplication.multiply(5))
