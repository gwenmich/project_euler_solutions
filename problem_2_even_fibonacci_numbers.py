# Even Fibonacci Numbers
# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
# the first terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.

# https://projecteuler.net/problem=2

def even_fibonacci():
    fib_num = [1, 2]
    while fib_num[-1] < 4_000_000:
        x = fib_num[-1] + fib_num[-2]
        fib_num.append(x)

    even_fib_sum = sum([i for i in fib_num if i % 2 == 0])
    return even_fib_sum


print(even_fibonacci())