# https://projecteuler.net/problem=3

# Largest prime factor
# The prime factors of 13195 are 5, 7, 13 and 29
# What is the largest prime factor of the number 600851475143?

def largest_prime_num(num):
    prime_factors = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            prime_factors.append(divisor)
            num //= divisor
        divisor += 1

    return max(prime_factors)



print(largest_prime_num(600851475143))
