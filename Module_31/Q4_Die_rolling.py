import random

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


def simulate_die_rolls(num_rolls):
    """
    Simulate rolling a six-sided die a specified number of times.

    :param num_rolls: Number of times to roll the die.
    :return: List of outcomes.
    """
    outcomes = [random.randint(1, 6) for _ in range(num_rolls)]
    return outcomes


def calculate_probabilities(outcomes):
    """
    Calculate the probabilities of each outcome from the list of outcomes.

    :param outcomes: List of outcomes from die rolls.
    :return: List of probabilities for each possible outcome (1 to 6).
    """
    total_rolls = len(outcomes)
    probabilities = [outcomes.count(i) / total_rolls for i in range(1, 7)]
    return probabilities


# Simulate rolling a fair six-sided die 1000 times
num_rolls = 1000
outcomes = simulate_die_rolls(num_rolls)

# Calculate probabilities based on the simulated outcomes
values = [1, 2, 3, 4, 5, 6]
probabilities = calculate_probabilities(outcomes)

# Create a DiscreteRandomVariable instance for the die
die = DiscreteRandomVariable(values, probabilities)

# Calculate expected value and variance
expected_value = die.expected_value()
variance = die.variance()

print("Expected Value:", expected_value)
print("Variance:", variance)
