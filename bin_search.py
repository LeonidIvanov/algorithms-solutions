def bin_search(s, lst):
    right = lst[int(len(lst) / 2):]
    left = lst[:int(len(lst) / 2)]
    print(left, right)
    if right[0] == s:
        print('Found it!!! Right!')
        result = right[0]
    elif left[-1] == s:
        print('Found it!!! Left!')
        result = left[-1]
    elif right[0] < s:
        bin_search(s, right)
    elif left[-1] > s:
        bin_search(s, left)
    else:
        print('Something went wrong!')
    return result

if __name__ == '__main__':
    mass = [x for x in range(0, 1000000)]
    s = 2
    print(bin_search(s, mass))
