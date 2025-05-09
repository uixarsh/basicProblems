import sys
sys.setrecursionlimit(100000)
sys.set_int_max_str_digits(1000000)


def factorial(n : int) -> int:
    assert n>=0 and int(n) == n , 'Then number must be positive integer only !'
    if n in [0,1]:
        return 1
    return n * factorial(n-1)

val = factorial(100)
print(val)