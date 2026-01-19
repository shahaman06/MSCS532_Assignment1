"""
Insertion Sort (monotonically decreasing order)

This implements the insertion sort algorithm from CLRS, modified to sort
in decreasing order instead of increasing.
"""

from typing import List


def insertion_sort_desc(arr: List[int]) -> List[int]:
    """
    Sorts the list in place into monotonically decreasing order.
    Returns the same list for convenience.
    """
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1

        # For decreasing order, move elements that are smaller than key
        # one position ahead.
        while i >= 0 and arr[i] < key:
            arr[i + 1] = arr[i]
            i -= 1

        arr[i + 1] = key

    return arr


def main() -> None:

    # INPUT LINE ADDED HERE
    user_input = input("Enter numbers separated by spaces: ")
    data = list(map(int, user_input.split()))

    print("Original:", data)
    insertion_sort_desc(data)
    print("Sorted (decreasing):", data)


if __name__ == "__main__":
    main()