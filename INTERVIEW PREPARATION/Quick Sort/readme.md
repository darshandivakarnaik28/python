# Quick Sort Using Recursion and XOR Swapping 🧮

## 📌 Description

This Python program sorts an array in **ascending order using the Quick Sort algorithm**.

It uses:
- **Recursion** to sort smaller subarrays.
- **Partitioning** to place the pivot element in its correct position.
- **XOR swapping** to exchange two elements without using a temporary variable.

## 💻 Program

```python
a = [10, -5, 6, -4, 11, -20, 7, -12, 0]

def swap(i, j):
    if i != j:
        a[i] = a[i] ^ a[j]
        a[j] = a[i] ^ a[j]
        a[i] = a[i] ^ a[j]

def partition(a, l, r):
    i = l - 1
    j = l

    while j <= r:
        if a[j] < a[r]:
            i += 1
            swap(i, j)
        j += 1

    j -= 1
    i += 1
    swap(i, j)

    return i

def quicksort(a, l, r):
    if l < r:
        i = partition(a, l, r)
        quicksort(a, l, i - 1)
        quicksort(a, i + 1, r)

print("Array before sort: ", a)
quicksort(a, 0, len(a) - 1)
print("Array after sort: ", a)
```

## 🧠 Logic of the Program

### 1. `swap(i, j)`

Swaps the elements at indices `i` and `j` using XOR.

```python
a[i] = a[i] ^ a[j]
a[j] = a[i] ^ a[j]
a[i] = a[i] ^ a[j]
```

The condition `i != j` prevents an element from being XOR-swapped with itself.

### 2. `partition(a, l, r)`

This function selects the **last element as the pivot**.

- `l` is the starting index.
- `r` is the ending index.
- `i` tracks the boundary of elements smaller than the pivot.
- `j` scans the subarray from left to right.
- If `a[j]` is smaller than the pivot, `i` is incremented and the elements are swapped.
- Finally, the pivot is swapped into its correct position.

The function returns the pivot's final index.

### 3. `quicksort(a, l, r)`

This function recursively sorts the array.

1. Call `partition()` to place the pivot.
2. Sort the left subarray using `quicksort(a, l, i-1)`.
3. Sort the right subarray using `quicksort(a, i+1, r)`.
4. Stop when `l < r` becomes false.

## 🔍 Complete Partition Tracking

Initial array:

```text
[10, -5, 6, -4, 11, -20, 7, -12, 0]
```

### Partition 1: Pivot = 0

Initial values:

```text
l = 0
r = 8
i = -1
j = 0
pivot = a[8] = 0
```

The loop checks each element against `0`.

| `j` | Element | Condition `a[j] < 0` | Action |
|---:|---:|---|---|
| 0 | 10 | False | No swap |
| 1 | -5 | True | Swap indices 0 and 1 |
| 2 | 6 | False | No swap |
| 3 | -4 | True | Swap indices 1 and 3 |
| 4 | 11 | False | No swap |
| 5 | -20 | True | Swap indices 2 and 5 |
| 6 | 7 | False | No swap |
| 7 | -12 | True | Swap indices 3 and 7 |
| 8 | 0 | False | No swap |

After the loop, the pivot is swapped into index `4`.

Array after partition:

```text
[-5, -4, -20, -12, 0, 6, 7, 10, 11]
```

The pivot `0` is now at index `4`.

The recursive calls are:

```text
quicksort(a, 0, 3)
quicksort(a, 5, 8)
```

Everything to the left of the pivot is smaller than `0`, and everything to the right is greater than `0`.

### Partition 2: Left Subarray

Subarray:

```text
[-5, -4, -20, -12]
```

Pivot:

```text
-12
```

Compare each element with `-12`:

| Element | Comparison | Action |
|---:|---|---|
| -5 | `-5 < -12` → False | No swap |
| -4 | `-4 < -12` → False | No swap |
| -20 | `-20 < -12` → True | Move -20 to the left |
| -12 | `-12 < -12` → False | No swap |

The pivot `-12` is placed at index `1`.

Array:

```text
[-20, -12, -5, -4, 0, 6, 7, 10, 11]
```

The next recursive calls are:

```text
quicksort(a, 0, 0)
quicksort(a, 2, 3)
```

The first call contains only one element, so it stops.

### Partition 3: Subarray `[-5, -4]`

Pivot:

```text
-4
```

Comparison:

```text
-5 < -4 → True
```

The pivot is already in the correct position. The subarray remains:

```text
[-5, -4]
```

The recursive calls now contain single elements, so this branch finishes.

The complete left side is sorted:

```text
[-20, -12, -5, -4]
```

### Partition 4: Right Subarray

Subarray:

```text
[6, 7, 10, 11]
```

Pivot:

```text
11
```

All other elements are smaller than `11`, so the pivot remains at the end.

```text
[6, 7, 10, 11]
```

Next, Quick Sort processes:

```text
[6, 7, 10]
```

### Partition 5: Subarray `[6, 7, 10]`

Pivot:

```text
10
```

Both `6` and `7` are smaller than `10`, so no effective changes are needed.

```text
[6, 7, 10]
```

### Partition 6: Subarray `[6, 7]`

Pivot:

```text
7
```

Since `6 < 7`, the pivot is already correctly positioned.

```text
[6, 7]
```

All remaining recursive calls contain one element or no elements. Therefore, recursion stops.

## 📊 Summary of Partition Results

| Partition | Subarray | Pivot | Final Pivot Index |
|---|---|---:|---:|
| 1 | Entire array | 0 | 4 |
| 2 | Left side | -12 | 1 |
| 3 | `[-5, -4]` | -4 | 3 |
| 4 | Right side | 11 | 8 |
| 5 | `[6, 7, 10]` | 10 | 7 |
| 6 | `[6, 7]` | 7 | 6 |

## 🖨️ Output

```text
Array before sort:  [10, -5, 6, -4, 11, -20, 7, -12, 0]
Array after sort:   [-20, -12, -5, -4, 0, 6, 7, 10, 11]
```

## 🌳 Recursion Flow

```text
                 quicksort(0, 8)
                       |
                  partition: 0
                   /       \
            quicksort      quicksort
               (0, 3)        (5, 8)
                 |              |
            pivot: -12       pivot: 11
              /    \          /    \
          (0, 0)  (2, 3)    (5, 7) (9, 8)
                    |          |
                 pivot: -4  pivot: 10
                              |
                           pivot: 7
```

Calls where the left index is greater than or equal to the right index stop without further partitioning.

## 📚 Concepts Practiced

- Python functions and parameters
- Quick Sort algorithm
- Recursion
- Partitioning
- Bitwise XOR operator
- Swapping without a temporary variable
- Array indexing
- Sorting negative and positive integers
- Base condition in recursion

## ⏱️ Complexity

- **Average time complexity:** `O(n log n)`
- **Worst-case time complexity:** `O(n²)`
- **Auxiliary space complexity:** `O(log n)` on average for the recursion stack; worst case `O(n)`.

## 💡 Key Takeaway

Quick Sort repeatedly partitions the array around a pivot, then recursively sorts the two sides. XOR swapping exchanges elements without a temporary variable.

**In one line:** Select pivot → partition the array → recursively sort the left and right subarrays → obtain ascending order.
