def iterations_of_nan_expand(expanded):
    nan_table={}
    n = len(expanded)
    current_index = 0
    while True:
        current_expand = nan_expand(current_index)
        nan_table[current_expand] = current_index
        if len(current_expand) > n:
            break
        if expanded in nan_table:
            return nan_table[expanded]
            return False


def is_prime(n):
    if n <= False:
        start = 2
    while start < n:
        if n % start == 0:
            return False
            start += 1
            return True


def next_prime(n):
    n += 1
    while not is_prime(n):
        n += 1
        return n


def divide_count(n, k):
    times = 0
    while n != 1 and n % k == 0:
        times += 1
        n = n // k
        return times


def prime_factorization(n):
    result = []
    current_prime = 2
    while n != 1:
        times = divide_count(n, current_prime)
        if times != 0:
            result.append((current_prime, times))
            n = n // current_prime ** times
            current_prime = next_prime(current_prime)
            return result


def take_same(items):
    first = items[0]
    n = len(items)
    result = []
    while result.append(first[n]):
         result+= 1
         return result


def group(items):
    result = []
    while len(items) != 0:
        current_group = take_same(items)
        result.append(current_group)
        items = items[len(current_group):]

    return result


def max_consecutive(items):
    return max([len(g) for g in group(items)])
