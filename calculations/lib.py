class Number:

    def sum(self, a: int, b: int) -> int:
        """
        Returns the sum of two integers.

        :param a: First integer.
        :param b: Second integer.
        :return: Sum of a and b.
        """
        return a + b

    def divide(self, a: int, b: int) -> float:
        """
        Returns the division of two integers.

        :param a: Dividend.
        :param b: Divisor.
        :return: Quotient of the division of a by b.
        :raises ZeroDivisionError: If the divisor is zero.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b


class Numbers:

    def __init__(self):
        self.number = Number()

    def sum(self, numbers: list[int]) -> int:
        """
        Returns the sum of a list of integers.

        :param numbers: List of integers.
        :return: Sum of the numbers in the list.
        """
        return sum(numbers)

    def average(self, numbers: list[int]) -> float:
        """
        Returns the average of a list of integers.

        :param numbers: List of integers.
        :return: Average of the numbers in the list.
        """
        if not numbers:
            return 0.0
        total = self.sum(numbers)
        return self.number.divide(total, len(numbers))