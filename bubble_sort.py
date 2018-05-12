""" Bubble Sort
    Worst case runtime - O(n**2)
    Best case runtime - Omega(n)

    Pseudocode:
    Set swap counter to a non-zero value
    Repeat until the swap counter is 0:
        Reset swap counter to 0
        Look at each adjacent pair
            If two adjacent elements are not in order, swap them and add one to the swap counter
"""


def bubble_sort(num_list_to_sort):
    i = -1
    while i != 0:
        i = 0
        for j in range(len(num_list_to_sort) - 1):
            if num_list_to_sort[j] > num_list_to_sort[j + 1]:
                num_list_to_sort[j], num_list_to_sort[j + 1] = num_list_to_sort[j + 1], num_list_to_sort[j]
                i += 1
    return num_list_to_sort

if __name__ == '__main__':
    print(bubble_sort([5, 2, 1, 3, 6, 4]))
    assert bubble_sort([5, 2, 1, 3, 6, 4]) == [1, 2, 3, 4, 5, 6], "Assert #1"
    assert bubble_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6], "Assert #2"
    assert bubble_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6], "Assert #3"
    assert bubble_sort([1]) == [1], "Assert #4"
