""" Binary Search
    Worst case runtime - O(log n)
    Best case runtime - Omega(1)

    Pseudocode:
    Repeat until the (sub)array is of size 0:
        Calculate the middle point of the current (sub)array.
        If the target is at the middle, stop.
        Otherwise, if the target is less than what's at the middle, repeat,
        changing the end point to be just to the left of the middle.
        Otherwise, if the target is greater than what's at the middle,
        repeat, changing the start point to be just to the right of the middle.
"""


def binary_search(target, sorted_arr):
    middle = len(sorted_arr) // 2
    try:
        middle_num = sorted_arr[middle]
        if target == middle_num:
            return True
        elif target > middle_num:
            return binary_search(target, sorted_arr[middle + 1:])
        elif target < middle_num:
            return binary_search(target, sorted_arr[:middle])
    except IndexError:
        return False

if __name__ == '__main__':
    print(binary_search(9, list(range(1000))))
    assert binary_search(9, list(range(1000))) == True, "Assert #1"
    assert binary_search(9, list(range(1001))) == True, "Assert #2"
    assert binary_search(-1, list(range(1000))) == False, "Assert #3"
    assert binary_search(1, list(range(1000))) == True, "Assert #4"
    assert binary_search(999, list(range(1000))) == True, "Assert #5"
    assert binary_search(500, list(range(1000))) == True, "Assert #5"
    assert binary_search(499, list(range(1000))) == True, "Assert #5"
