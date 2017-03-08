def fib(n, lst=[0, 1]):
    for i in range(1, n):
       lst.append(lst[i-1] + lst[i])
    return lst

if __name__ == '__main__':
    print(fib(10))