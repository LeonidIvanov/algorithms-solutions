""" The Collatz conjecture is applies to positive integers
    and speculates that it is always possible to get "back to 1" if you follow these steps:

    Pseudocode:
    If n is 1, stop.
    Otherwise, if n is even, repeat this process on n / 2.
    Otherwise, if n is odd, repeat this process on 3n + 1.
"""


def collatz(n, i=0):
    if n == 1:
        return i
    elif n % 2 == 0:
        i += 1
        return collatz(n/2, i)
    elif n % 2 == 1:
        i += 1
        return collatz(3 * n + 1, i)


if __name__ == '__main__':
    print(collatz(27))
    assert collatz(1) == 0, "Assert #1"
    assert collatz(2) == 1, "Assert #2"
    assert collatz(3) == 7, "Assert #3"
    assert collatz(4) == 2, "Assert #4"
    assert collatz(5) == 5, "Assert #5"
    assert collatz(6) == 8, "Assert #6"
    assert collatz(27) == 111, "Assert #7"

