import random

# 1. Gerate list of random integer
# Generate a list of 500 integers containing values between 200 and 300
int_list2 = [random.randint(200, 300) for _ in range(500)]
print(int_list2)

# 2. Visualization

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Frequency & Gaussian distribution
plt.figure(figsize=(10, 6))
sns.histplot(int_list2, bins=30, kde=False, color='blue', stat="density", label='Frequency')
mean = np.mean(int_list2)
std = np.std(int_list2)
x = np.linspace(200, 300, 1000)
plt.plot(x, 1/(std * np.sqrt(2 * np.pi)) * np.exp(- (x - mean)**2 / (2 * std**2)), color='red', label='Gaussian distribution')
plt.legend()
plt.title('Frequency & Gaussian distribution')
plt.show()

# Frequency smoothened KDE plot
plt.figure(figsize=(10, 6))
sns.histplot(int_list2, bins=30, kde=True, color='green', label='Frequency with KDE')
plt.legend()
plt.title('Frequency smoothened KDE plot')
plt.show()

# Gaussian distribution & smoothened KDE plot
plt.figure(figsize=(10, 6))
sns.kdeplot(int_list2, color='blue', label='KDE plot')
plt.plot(x, 1/(std * np.sqrt(2 * np.pi)) * np.exp(- (x - mean)**2 / (2 * std**2)), color='red', label='Gaussian distribution')
plt.legend()
plt.title('Gaussian distribution & smoothened KDE plot')
plt.show()

# 3. Calculating the range
def calculate_range(numbers):
    return max(numbers) - min(numbers)

# Example usage
range_value = calculate_range(int_list2)
print("Range:", range_value)


# 4. Variance and standard deviation
def calculate_variance(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return variance

def calculate_standard_deviation(numbers):
    variance = calculate_variance(numbers)
    return variance ** 0.5

# Example usage
variance = calculate_variance(int_list2)
std_deviation = calculate_standard_deviation(int_list2)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)

# 5. Computing IQR
def calculate_iqr(numbers):
    sorted_numbers = sorted(numbers)
    q1 = np.percentile(sorted_numbers, 25)
    q3 = np.percentile(sorted_numbers, 75)
    return q3 - q1

# Example usage
iqr = calculate_iqr(int_list2)
print("Interquartile Range (IQR):", iqr)

# 7. Calculating the coefficient of variance 
def calculate_coefficient_of_variation(numbers):
    mean = sum(numbers) / len(numbers)
    std_dev = calculate_standard_deviation(numbers)
    return std_dev / mean

# Example usage
coefficient_of_variation = calculate_coefficient_of_variation(int_list2)
print("Coefficient of Variation:", coefficient_of_variation)

# 7. MAD
def calculate_mad(numbers):
    mean = sum(numbers) / len(numbers)
    mad = sum(abs(x - mean) for x in numbers) / len(numbers)
    return mad

# Example usage
mad = calculate_mad(int_list2)
print("Mean Absolute Deviation (MAD):", mad)

# 8. Quartile Deviation
def calculate_quartile_deviation(numbers):
    iqr = calculate_iqr(numbers)
    return iqr / 2

# Example usage
quartile_deviation = calculate_quartile_deviation(int_list2)
print("Quartile Deviation:", quartile_deviation)

# 9. Range based coefficient dispersion
def calculate_range_based_coefficient_of_dispersion(numbers):
    range_value = calculate_range(numbers)
    mean = sum(numbers) / len(numbers)
    return range_value / mean

# Example usage
range_based_coefficient_of_dispersion = calculate_range_based_coefficient_of_dispersion(int_list2)
print("Range-based Coefficient of Dispersion:", range_based_coefficient_of_dispersion)
