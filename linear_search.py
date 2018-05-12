""" Linear Search
    Worst case runtime - O(n)
    Best case runtime - Omega(1)

    Pseudocode:
    Repeat, starting at the first element:
        If the first element is what you're looking for (the target), stop
"""


def linear_search(target, arr):
    for element in arr:
        if element == target:
            return True
    return False

if __name__ == '__main__':
    print(linear_search(9, [11, 23, 8, 14, 30, 9, 6, 17, 22, 28, 25, 15, 7, 10, 19]))
    assert linear_search(9, [11, 23, 8, 14, 30, 9, 6, 17, 22, 28, 25, 15, 7, 10, 19]) == True, "Assert #1"
    assert linear_search(1, [11, 23, 8, 14, 30, 9, 6, 17, 22, 28, 25, 15, 7, 10, 19]) == False, "Assert #2"
    assert linear_search(0, [1]) == False, "Assert #3"
    assert linear_search(1, [1]) == True, "Assert #4"
