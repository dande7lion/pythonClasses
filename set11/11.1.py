import random
from numpy import random as numpy_random

# funkcja pomocnicza

def swap_some_numbers(list_of_numbers):
    for i in range(len(list_of_numbers)-1):
        if i%4 == 0:
            list_of_numbers[i], list_of_numbers[i+1] = list_of_numbers[i+1], list_of_numbers[i]
        i = i+1
    return list_of_numbers

# (a) różne liczby int od 0 do N-1 w kolejności losowej

def unique_random_numbers(n):
    if n < 0:
        raise Exception("Size can not be less than zero!")
    return random.sample(range(0, n), n)

# (b) różne liczby int od 0 do N-1 prawie posortowane (liczby są blisko swojej prawidłowej pozycji)

def nearly_sorted_numbers(n):
    list_of_numbers = unique_random_numbers(n)
    list_of_numbers.sort()
    return swap_some_numbers(list_of_numbers)

# (c) różne liczby int od 0 do N-1 prawie posortowane w odwrotnej kolejności

def reverse_nearly_sorrted_numbers(n):
    list_of_numbers = unique_random_numbers(n)
    list_of_numbers.sort(reverse=True)
    return swap_some_numbers(list_of_numbers)

# (d) N liczb float w kolejności losowej o rozkładzie gaussowskim

def gaussian_distribution(n):
    list_of_numbers = []
    for i in range (0,n):
        list_of_numbers.append(float(numpy_random.normal(size=1)))
    return list_of_numbers


# (e) N liczb int w kolejności losowej, o wartościach powtarzających się, należących do zbioru k elementowego (k < N, np. k*k = N)

def repeating_numbers(n, k):
    list_of_numbers = []
    if n <= k:
        raise Exception("There will be no repeating numbers, because k is larger (or equal) than (to) n")
    for i in range(n):
        list_of_numbers.append(random.randint(0, k))
    return list_of_numbers

print(repeating_numbers(6, 5))