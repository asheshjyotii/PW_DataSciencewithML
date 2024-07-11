import random
from collections import Counter
import math

# 1. Generating the list
# Generate a list of 100 integers containing values between 90 and 130
int_list = [random.randint(90, 130) for _ in range(100)]
print(int_list)

# 2. Calculating mean
def calculate_mean(numbers):
    return sum(numbers) / len(numbers)

# Example usage
mean = calculate_mean(int_list)
print("Mean:", mean)

# 3. Calculating median
def calculate_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    
    if n % 2 == 0:
        median = (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        median = sorted_numbers[mid]
        
    return median

# Example usage
median = calculate_median(int_list)
print("Median:", median)


# 4. Calculate mode
def calculate_mode(numbers):
    count = Counter(numbers)
    max_count = max(count.values())
    mode = [k for k, v in count.items() if v == max_count]
    
    return mode

# Example usage
mode = calculate_mode(int_list)
print("Mode:", mode)


# 5. Calculating weighted mean
def calculate_weighted_mean(values, weights):
    weighted_sum = sum(v * w for v, w in zip(values, weights))
    total_weight = sum(weights)
    
    return weighted_sum / total_weight

# Example usage with example weights
weights = [random.randint(1, 10) for _ in range(100)]
weighted_mean = calculate_weighted_mean(int_list, weights)
print("Weighted Mean:", weighted_mean)


# 6. Calculating geometric mean 
def calculate_geometric_mean(numbers):
    product = 1
    for number in numbers:
        product *= number
        
    return product ** (1 / len(numbers))

# Example usage
geometric_mean = calculate_geometric_mean(int_list)
print("Geometric Mean:", geometric_mean)

# 7. Calculting harmonic mean
def calculate_harmonic_mean(numbers):
    reciprocal_sum = sum(1 / number for number in numbers)
    
    return len(numbers) / reciprocal_sum

# Example usage
harmonic_mean = calculate_harmonic_mean(int_list)
print("Harmonic Mean:", harmonic_mean)


# 8. Calculating midrange
def calculate_midrange(numbers):
    return (min(numbers) + max(numbers)) / 2

# Example usage
midrange = calculate_midrange(int_list)
print("Midrange:", midrange)

# 9. Calculate trimmed mean
def calculate_trimmed_mean(numbers, percentage):
    n = len(numbers)
    trim_count = int(n * percentage / 100)
    trimmed_numbers = sorted(numbers)[trim_count:-trim_count]
    
    return sum(trimmed_numbers) / len(trimmed_numbers)

# Example usage with a 10% trim
trimmed_mean = calculate_trimmed_mean(int_list, 10)
print("Trimmed Mean:", trimmed_mean)

