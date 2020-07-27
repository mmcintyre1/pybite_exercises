from functools import lru_cache


def memoize(func):
    cache = dict()

    def memoized_func(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return memoized_func


@memoize
def fib_1(n):
    if n in (0, 1):
        return n

    return fib_1(n-1) + fib_1(n-2)


@lru_cache(maxsize=1000)
def fib_2(n):

    if n in (0, 1):
        return n

    return fib_2(n-1) + fib_2(n-2)


for num in range(5000):
    print(f"fibonacci index: {num} value: {fib_1(num)}")

for num in range(5000):
    print(f"fibonacci index: {num} value: {fib_2(num)}")
