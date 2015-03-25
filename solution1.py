#factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


#second factorial
def factorial1(n):
    if n < 2:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
   if n == 1:
      return 1
   elif n == 0:   
      return 0            
   else:                      
      return fib(n-1) + fib(n-2)


def sum_of_digits(n):
    result = 0
    while n != 0:
        result += n % 10
        n = n // 10
    return result


def to_digits(n):
    return [int(x) for x in str(n)]


def factorial_digits(n):
     return sum([factorial(x) for x in to_digits(n)])
  

def palindrome(n):
    return str(n) == str(n)[::-1]


def to_number(digits):
    result = 0
    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit
        return result


def fibonacci_number(n):
     return to_number(fibonacci(n))



def count_vowels(string):
    vowels = "aeiouyAEIOUY"
    count = 0
    for ch in string:
        if ch in vowels:
            count += 1
            return count


def count_consonants(string):
    consonants = "bcdfghjklmnoqrstBCDFGHJKLMNPQRSTVWX"
    count = 0
    for ch in string:
         if ch in consonants:
          count += 1
          return count


def char_histogram(string):
    result = {}

    for ch in string:
        if ch in result:
            result[ch] += 1
        else:
            result[ch] = 1

def p_score(n):
    if palindrome(n):
        return 1 
        s = n +int(str(n)[::-1])
        return 1 + p_score(s)
def even(n):
    return n % 2 == 0
def odd(n):
    return not even(n)


def is_hack(n):
    binary_n = bin(n)[2:]

     is_palndrome = palindrome(binary_n)
     has_odd_ones = odd(binary_n.count("1"))

        return palindrome(binary_n) and binary_n 