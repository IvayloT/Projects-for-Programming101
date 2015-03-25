def count_words(words):
    return {key:words.count(key) for key in words}


def unique_words(words):
    return len([key for key in count_words(words)])


def unique_words(words):
    return len(set(words))


#при списък с дъжлина n ,търся с О(n)
# при множество с дължина n,търся с O(n);


#dedup - фунция за уникални думи
#set  не пази подредба!
def dedup(items):
    found = set()
    resutl = []
for item in items:
    if item not in found:
        result.append(item)
        found.add(item)

    return result

def nan_expand(times):
     

def iteration_of_nan_expand(expanded):
    #n = len(expanded)
    """ Искаме да генерираме всички nan_expand
    с дължина <= n Ако expanded е сред тях -> return броя?
    Ако не е ,false""" 

def is_prime(n):  
  prime = True
    while prime < n:
    if n % start == 0:
        return False 
        start 
    start = 2
def prime_factorization(n):
    result = []

    current_prime = 2 

    while n != 1:
        times = divide_count(n, next_prime)
    if times != 0:
        result.append((current_prime,times))
        n = n // current_prime ** times
    current_prime = next_prime(current_prime)
    return result

def divide_prime(n,k):
    times = 0
    while n != 1:
        if n % k == 0



# редюс път
def reduce_file(path):
    result = []
    parts = [ parts for parts in path.split("/")] if part not in [".",""] ]
    while len(parts) !=0:
        part = parts.pop()
        if part == "..":
            parts.pop()
    print (parts)
    return "/" + "/".join(parts)

    this is promqnata vuv faila oshte dsadas