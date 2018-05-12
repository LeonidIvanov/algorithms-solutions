""" Selection Sort
Repeat until no unsorted elements remain:
    Search the unsorted part of the data to find the smallest value
    Swap the smallest found value with the first element of the unsorted part
"""


def selection_sort(num_list_to_sort):
    i = len(num_list_to_sort)
    while i != 0:
        for j in range(len(num_list_to_sort) - 1):
            if num_list_to_sort[j] > num_list_to_sort[j + 1]:
                num_list_to_sort[j], num_list_to_sort[j + 1] = num_list_to_sort[j + 1], num_list_to_sort[j]
                i -= 1
    return num_list_to_sort

if __name__ == '__main__':
    print(selection_sort([5, 2, 1, 3, 6, 4]))
