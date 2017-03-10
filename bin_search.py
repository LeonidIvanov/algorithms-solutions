def bin_search(s, lst, i=0):
    if not lst:
        return 0
    else:
        right = lst[int(len(lst) / 2):]
        left = lst[:int(len(lst) / 2)]
        if right[0] < s:
            i += 1
            return bin_search(s, right, i)
        if left[-1] > s:
            i += 1
            return bin_search(s, left, i)
        if right[0] == s or left[-1] == s:
            return '{} iteration(s)'.format(i)


def lin_search(s, lst):
    if not lst:
        return 0
    else:
        for i in range(len(lst)):
            if lst[i] == s:
                return '{} iteration(s)'.format(i)

if __name__ == '__main__':
    import timeit
    mass = [x for x in range(-1000000, 1000000)]
    s = 999999
    print(bin_search(s, mass))
    print(lin_search(s, mass))
