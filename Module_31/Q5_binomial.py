import numpy as np

def generate_samples(distribution, params, num_samples=1000):
    """
    Generate random samples from a specified probability distribution and calculate their mean and variance.

    :param distribution: The name of the distribution (e.g., 'binomial', 'poisson').
    :param params: Parameters of the distribution (e.g., for 'binomial' provide 'n' and 'p').
    :param num_samples: The number of samples to generate.
    :return: Tuple containing the mean and variance of the generated samples.
    """
    if distribution == 'binomial':
        n, p = params
        samples = np.random.binomial(n, p, num_samples)
    elif distribution == 'poisson':
        lam = params[0]
        samples = np.random.poisson(lam, num_samples)
    else:
        raise ValueError("Unsupported distribution type")

    mean = np.mean(samples)
    variance = np.var(samples)
    
    return mean, variance

# Example usage:
# Generating samples from a binomial distribution with n=10, p=0.5
binomial_mean, binomial_variance = generate_samples('binomial', (10, 0.5))
print(f"Binomial Distribution: Mean = {binomial_mean}, Variance = {binomial_variance}")

# Generating samples from a Poisson distribution with lambda=3
poisson_mean, poisson_variance = generate_samples('poisson', (3,))
print(f"Poisson Distribution: Mean = {poisson_mean}, Variance = {poisson_variance}")
