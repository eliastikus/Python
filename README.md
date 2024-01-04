# Sorting Module in Python

This Python module provides implementations of several sorting algorithms. The current version includes the following sorting algorithms:

- Bubble Sort
- Merge Sort
- Quick Sort
- Insertion Sort
- Heap Sort
- Shell Sort

# How to install and import module 

To install the module, you need to write in the terminal.

```
pip install easiest_sort
```

To import the module, you need to write in your Python file

```
from easiest_sort import *
```


## Bubble Sort

Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

```
from easiest_sort import bubble_sort

my_list = []
bubble_sort(my_list)

```

## Merge Sort

Merge Sort is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts them, and then merges the sorted halves.

```
from easiest_sort import merge_sort

my_list = []
merge_sort(my_list)
```

## Quick Sort

Quick Sort is another divide-and-conquer algorithm that partitions the array into smaller parts and then recursively sorts them.

```
from easiest_sort import quick_sort

my_list = []
quick_sort(my_list)
```

## Insertion Sort

Heap Sort uses a binary heap data structure to build a heap and then sorts the heap.

```
from sorting_module import heap_sort

my_list = []
heap_sort(my_list)
```

## Shell Sort

Shell Sort is an optimization over insertion sort that compares elements that are far apart and gradually reduces the gap between them.

```
from sorting_module import shell_sort

my_list = []
shell_sort(my_list)
```

In the future, I will be adding more sorting algorithms.
I hope this module will be helpful to you.
