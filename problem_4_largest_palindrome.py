# https://projecteuler.net/problem=4

# Largest Palindrome Product
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 * 99
# Find the largest palindrome made from the product of two 3-digit numbers

def largest_palindrome():
    palindromes = []
    for i in range(900, 1000):
        for x in range(900, 1000):
            y = str(i * x)

            if y[0] == y[-1] and y[1] == y[-2] and y[2] == y[-3]:
                palindromes.append(int(y))
    return max(palindromes)


print(largest_palindrome())
