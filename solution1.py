def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    numbers = []
    a = 1
    b = 1
    while len(numbers) < n:
        numbers.append(a)
        next_fib = a + b
        a = b
        b = next_fib
    return numbers


def sum_of_digits(n):
    return sum([int(x) for x in str(n)])


def to_digits(n):
    return [int(x) for x in str(n)]


def fact_digits(n):
    return sum([factorial(x) for x in to_digits(n)])


def palindrome(obj):
    return str(obj)[::-1] == str(obj)


def to_number(n):
    return int(''.join(str(i) for i in n))


def fib_number(n):
    return int(''.join(str(i) for i in fibonacci(n)))


def count_vowels(string):
    vowels = "aeiouyAEIOUY"
    count = 0

    for i in string:
        if i in vowels:
            count += 1
    return count


def count_consonants(string):
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"
    count = 0

    for i in string:
        if i in consonants:
            count += 1
    return count


def char(string):
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


def p_score(n):
    if palindrome(n):
        return 1

    s = n + int(str(n)[::-1])

    return 1 + p_score


def is_increasing(L):
    return all(x < y for x, y in zip(L, L[1:]))


def is_decreasing(L):
    return all(x > y for x, y in zip(L, L[1:]))


def even(n):
    return n % 2 == 0


def odd(n):
    return not even(n)


def is_hack(n):
    binary_n = bin(n)[2:]

    is_palindrome = palindrome(binary_n)
    has_odd_ones = odd(binary_n.count("1"))

    return is_palindrome and has_odd_ones


def next_hack(n):
    n += 1

    while not is_hack(n):
        n += 1

    return n
