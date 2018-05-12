""" Selection Sort
    Worst case runtime - O(n**2)
    Best case runtime - Omega(n**2)

    Pseudocode:
    Repeat until no unsorted elements remain:
        Search the unsorted part of the data to find the smallest value
        Swap the smallest found value with the first element of the unsorted part
"""


def selection_sort(num_list_to_sort):
    for i in range(len(num_list_to_sort)):
        for j in range(len(num_list_to_sort) - 1):
            if num_list_to_sort[j] > num_list_to_sort[j + 1]:
                num_list_to_sort[j], num_list_to_sort[j + 1] = num_list_to_sort[j + 1], num_list_to_sort[j]
    return num_list_to_sort

if __name__ == '__main__':
    assert selection_sort([5, 2, 1, 3, 6, 4]) == [1, 2, 3, 4, 5, 6], "Assert #1"
    assert selection_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6], "Assert #2"
    assert selection_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6], "Assert #3"
    assert selection_sort([1]) == [1], "Assert #4"
