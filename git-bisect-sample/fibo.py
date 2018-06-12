import functools

def memoize(obj):
    """Memoizer implementation from
    https://wiki.python.org/moin/PythonDecoratorLibrary#Memoize
    """
    cache = obj.cache = {}

    @functools.wraps(obj)
    def wrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]
    return wrapper

@memoize
def fibo(n):
    """Compute the nth Fibonacci number.
    Raises if n is negative
    :param n: the index of the Fibonacci number we want to compute
    :type n: int
    :returns: int
    :raises: ValueError
    """
    if n < 0:
        raise ValueError("n must be positive.")
    result = 0
    if n <= 2 :
        result = n
    else:
        result = fibo(n-1) + fibo(n-2)
    return result
