def fact(n):
    x = 1
    for i in range(1, n+1):
        x *= i
    return x

def rec_fact(n):
    if n == 1:
        return 1
    else:
        return n * rec_fact(n - 1)


if __name__ == '__main__':
    print(fact(5))
    print(rec_fact(5))