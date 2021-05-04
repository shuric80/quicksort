from copy import copy
from typing import List


def partition_first_elem(array: List[int], low: int, high: int) -> int:
    pivot = array[low]
    i = low + 1
    for j in range(low + 1, high):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[low], array[i - 1] = array[i - 1], array[low]
    return i - 1


def partition_last_elem(array: List[int], low: int, high: int) -> int:
    pivot = array[high - 1]
    i = low
    for j in range(low, high - 1):
        if array[j] < pivot:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[high - 1], array[i] = array[i], array[high - 1]
    return i


def partition_median(array: List[int], low: int, high: int) -> int:
    median = (low + high - 1) // 2
    idx, pivot = sorted(((low, array[low]),
                         (median, array[median]),
                         (high - 1, array[high - 1])),
                        key=lambda x: x[1])[1]
    array[low], array[idx] = array[idx], array[low]
    i = low + 1
    for j in range(low + 1, high, 1):
        if array[j] < pivot:
            array[i], array[j] = array[j], array[i]
            i += 1
    array[low], array[i - 1] = array[i - 1], array[low]
    return i - 1


def quick_sort(array: List[int], low: int, high: int, mode: str = '', cnt: int = 0) -> List[int]:
    if len(array) == 1:
        return 0
    num = high - low
    if low < high:
        if mode in 'first':
            pi = partition_first_elem(array, low, high)
        elif mode in 'last':
            pi = partition_last_elem(array, low, high)
        elif mode in 'median':
            pi = partition_median(array, low, high)
        else:
            raise Exception('Incorrect mode')
        cnt += + num - 1
        cnt += quick_sort(array, low, pi, mode)
        cnt += quick_sort(array, pi + 1, high, mode)
    return cnt


if __name__ == '__main__':
    array_test = [2, 1, 12, 13, 16, 10, 9, 5, 18, 8, 17, 20, 19, 3, 4, 11, 14, 6, 7, 15]  # 69 65 56
    cnt = quick_sort(copy(array_test), 0, len(array_test), 'first')
    assert cnt == 69
    cnt = quick_sort(copy(array_test), 0, len(array_test), 'last')
    assert cnt == 65
    cnt = quick_sort(copy(array_test), 0, len(array_test), 'median')
    assert cnt == 56
