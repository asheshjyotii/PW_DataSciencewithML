class DiscreteRandomVariable:
    def __init__(self, values, probabilities):
        """
        Initialize the DiscreteRandomVariable with values and their corresponding probabilities.

        :param values: List of possible values of the random variable.
        :param probabilities: List of probabilities associated with each value.
        """
        if len(values) != len(probabilities):
            raise ValueError("The length of values and probabilities must be the same.")
        
        if not abs(sum(probabilities) - 1.0) < 1e-6:
            raise ValueError("The sum of probabilities must be 1.")
        
        self.values = values
        self.probabilities = probabilities

    def expected_value(self):
        """
        Calculate the expected value (mean) of the random variable.

        :return: The expected value.
        """
        return sum(value * prob for value, prob in zip(self.values, self.probabilities))

    def variance(self):
        """
        Calculate the variance of the random variable.

        :return: The variance.
        """
        mean = self.expected_value()
        return sum(prob * (value - mean) ** 2 for value, prob in zip(self.values, self.probabilities))

# Example usage
values = [1, 2, 3, 4, 5]
probabilities = [0.1, 0.2, 0.3, 0.2, 0.2]

drv = DiscreteRandomVariable(values, probabilities)
print("Expected Value:", drv.expected_value())
print("Variance:", drv.variance())
