from fractions import gcd
from functools import reduce


# 1.Multiples of 3 and 5
def multiples(n):
    return sum([x for x in range(n) if x % 3 == 0 or x % 5 == 0])


# 2.Fibonacci numbers
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibb(n):
    sum = 0
    i = 1
    while fibonacci(i) < n:
        if fibonacci(i) % 2 == 0:
            sum += fibonacci(i)
        i += 1
    return sum


# 3.Prime Number
def prime_number(n):
    i = 2
    while i * i < n:
        while n % i == 0:
            n //= i
        i += 1
    return n


# 4.Palindrome Number
def palindrome(n):
    return str(n)[::-1] == str(n)


def palindrome1(n):
    return max([x * y for x in range(100, 1000) for y in range(100, 1000) if p(x * y)])


# 5.Smallest Multiple
def smallestM(n):
    m = reduce(lambda x, y: x * y // gcd(x, y), range(1, 20 + 1))
    print(m)


# 6.SumSquare
def sumSquare(n):
    return sum([x * x for x in range(n + 1)])


def squareSum(n):
    k = sum([x for x in range(n + 1)])
    return (k * k) - SumSquare(n)


# 7.10001Prime
def n_prime(n):
    res = 0
    for num in range(2, n):
        if all(num % X != 0 for X in range(2, num)):
            res += 1
            if res == 10001:
                print([res, num])
                break


# 8.Largest Product
def product(n):
    digits = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
    m = 0
    for i in range(len(digits) - 13):
        p = reduce(lambda x, y: int(x) * int(y), digits[i: i + 13])
        if p > m:
            m = p
    print(m)


# 9.SpecialTriples
def triplet(n):
    for a in range(1, 501):
        for b in range(a + 1, 501):
            c = n - a - b
            if (a ** 2 + b ** 2 == c ** 2):
                return a * b * c


# 10.SumOfPrimes
def SumPrimes(n):
    marked = [0] * n
    value = 3
    s = 2
    while value < n:
        if marked[value] == 0:
            s += value
            i = value
            while i < n:
                marked[i] = 1
                i += value
        value += 2
    print (s)
