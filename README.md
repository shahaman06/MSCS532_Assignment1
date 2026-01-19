# MSCS532 Assignment 1: Insertion Sort (Decreasing Order)

## Description
This project implements the **Insertion Sort** algorithm in Python, modified to sort a list of integers into **monotonically decreasing order**.  
The program accepts user input from the command line, performs the sort, and displays both the original and sorted lists.

## Algorithm Used
- Insertion Sort
- Modified comparison logic to sort from largest to smallest

## Requirements
- Python 3.8 or higher

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/MSCS532_Assignment1.git
cd MSCS532_Assignment1
```

2. Run the program:
```bash
python insertion_sort_desc.py
```

3. When prompted, enter integers separated by spaces.

## Example

Enter numbers separated by spaces: 5 2 4 6 1 3
Original: [5, 2, 4, 6, 1, 3]
Sorted (decreasing): [6, 5, 4, 3, 2, 1]

## Notes

- The algorithm sorts the list in place
- Time complexity: O(n²)
- Space complexity: O(1)