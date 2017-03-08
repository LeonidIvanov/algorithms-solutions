def rev(s):
    new = ''
    for i in range(len(s)):
        new += s[len(s)-i-1]
    return new


if __name__ == '__main__':
    print(rev('Hello, world!'))