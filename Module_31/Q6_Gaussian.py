import numpy as np

def generate_gaussian_samples(mean, std_dev, num_samples):
    """
    Generate random samples from a Gaussian (normal) distribution and calculate their mean, variance, and standard deviation.

    :param mean: Mean of the Gaussian distribution.
    :param std_dev: Standard deviation of the Gaussian distribution.
    :param num_samples: Number of samples to generate.
    :return: Tuple containing the mean, variance, and standard deviation of the generated samples.
    """
    samples = np.random.normal(mean, std_dev, num_samples)
    
    sample_mean = np.mean(samples)
    sample_variance = np.var(samples)
    sample_std_dev = np.std(samples)
    
    return sample_mean, sample_variance, sample_std_dev

# Example usage
mean = 0  # Mean of the distribution
std_dev = 1  # Standard deviation of the distribution
num_samples = 1000  # Number of samples to generate

sample_mean, sample_variance, sample_std_dev = generate_gaussian_samples(mean, std_dev, num_samples)

print(f"Generated Gaussian Distribution: Mean = {sample_mean}, Variance = {sample_variance}, Standard Deviation = {sample_std_dev}")
