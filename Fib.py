#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:18:03 2023

@author: nebiyousamuel
"""

def generate_fibonacci(n):
    fibonacci_numbers = [1, 1]

    while len(fibonacci_numbers) < n:
        next_number = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_number)

    return fibonacci_numbers

# Generate the first 100 Fibonacci numbers
first_100_fibonacci = generate_fibonacci(100)
print(first_100_fibonacci)


def calculate_ratio(fibonacci_numbers):
    ratio_sequence = [fibonacci_numbers[i+1] / fibonacci_numbers[i] for i in range(len(fibonacci_numbers) - 1)]
    return ratio_sequence

# Using the previously generated first_100_fibonacci list
ratios = calculate_ratio(first_100_fibonacci)
print(ratios)


import matplotlib.pyplot as plt

# Using the previously calculated ratios list
plt.plot(ratios)
plt.xlabel('n')
plt.ylabel('d[n]')
plt.title('Ratio of consecutive Fibonacci numbers')
plt.grid(True)
plt.show()
