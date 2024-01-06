# Sorting Module in Python

This Python module provides implementations of several sorting algorithms. The current version includes the following sorting algorithms:

- Bubble Sort
- Merge Sort
- Quick Sort
- Insertion Sort
- Heap Sort
- Shell Sort
- Partial Sort

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

Use Case: Simplicity and ease of understanding. Suitable for small data sets or educational purposes. Inefficient for large data sets due to quadratic complexity.

```python
from easiest_sort import bubble_sort

my_list = []
bubble_sort(my_list)
```

## Merge Sort

Use Case: Efficient sorting for large data sets. Relatively stable and well-suited for lists that do not fit entirely in memory

```python
from easiest_sort import merge_sort

my_list = []
merge_sort(my_list)
```

## Quick Sort

Use Case: High efficiency on average and large data sets. Demonstrates good practical performance. Used in various domains, including programming languages and databases.

```python
from easiest_sort import quick_sort

my_list = []
quick_sort(my_list)
```
## Insertion Sort

Use Case: Effective for small or partially ordered data. Convenient when adding new elements to an already sorted part of an array.

```python
from easiest_sort import insertion_sort

my_list = []
insertion_sort(my_list)
```

## Heap Sort

Use Case: Efficient for sorting large data sets. Utilizes the "heap" data structure. Possesses predictable worst-case performance.

```python
from easiest_sort import heap_sort

my_list = []
heap_sort(my_list)
```

## Shell Sort

Use Case: Balances implementation simplicity with good performance. Often applied in scenarios where a trade-off between efficiency and implementation simplicity is desired.

```python
from easiest_sort import shell_sort

my_list = []
shell_sort(my_list)
```


## Ascending and Descending order

If you want to use descending order sorting, you should use the second argument 'order' with a value of False. Its works with every sort algorithm


```python
from easiest_sort import *

my_list = []
bubble_sort(my_array, order=False)
```



# Partial Sort 

This module provides a partial_sort function, allowing you to perform partial sorting on a list. With this function, you can sort only the top or bottom k elements of the list, leaving the rest of the elements in their original order.

## Usage

```python
from easiest_sort import partial_sort

my_array = [5, 2, 8, 1, 9, 4, 7, 3, 6]

x1 = partial_sort(my_array, 3, top=True)

x2 = partial_sort(my_array, 3, top=False)
```

Also you can use Reverse Order for Partial Sort

```python
from easiest_sort import partial_sort

my_list = [5, 2, 8, 1, 9, 4, 7, 3, 6]

x = partial_sort(my_array, 3, top=True, reverse=True)
```



