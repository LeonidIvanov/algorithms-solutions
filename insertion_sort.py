""" Insertion Sort
    Worst case runtime - O(n**2)
    Best case runtime - Omega(n)

    Pseudocode:
    Call the first element of the array "sorted"
    Repeat until all elements are sorted:
        Look at the next unsorted element.
        Insert into the "sorted" portion by shifting the requisite number of elements.
"""


def insertion_sort(num_list_to_sort):
    for i in range(1, len(num_list_to_sort)):
        for j in range(len(num_list_to_sort[:i])):
            if num_list_to_sort[i] < num_list_to_sort[j]:
                for k in range(len(num_list_to_sort[j:i]))[::-1]:
                    num_list_to_sort[j + k], num_list_to_sort[j + k + 1] = num_list_to_sort[j + k + 1], num_list_to_sort[j + k]
    return num_list_to_sort

if __name__ == '__main__':
    print(insertion_sort([5, 2, 1, 3, 6, 4]))
    assert insertion_sort([5, 2, 1, 3, 6, 4]) == [1, 2, 3, 4, 5, 6], "Assert #1"
    assert insertion_sort([6, 5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5, 6], "Assert #2"
    assert insertion_sort([1, 2, 3, 4, 5, 6]) == [1, 2, 3, 4, 5, 6], "Assert #3"
    assert insertion_sort([1]) == [1], "Assert #4"
