from functools import lru_cache

FIVE_NAMES = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

AGES = [24, 25, 26, 27, 28]

MAP_NAME_TO_AGE = {name: age for name, age in zip(FIVE_NAMES, AGES)}

def average_age():
    return sum(AGES) / len(AGES)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def fibonacci_memoized(n):
    @lru_cache(maxsize=None)
    def fib(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return fib(n - 1) + fib(n - 2)
    return fib(n)

@lru_cache(maxsize=None)
def fibonacci_memo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
