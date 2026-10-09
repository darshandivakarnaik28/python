# Sort an Array Using XOR Swapping 🔢

## 📌 Description

This Python program sorts an array in **ascending order** using nested `for` loops and the bitwise XOR (`^`) operator.

It swaps elements without using a temporary variable.

### How the Program Works

1. The outer loop selects an element using index `i`.
2. The inner loop compares it with the elements after it using index `j`.
3. If `a[i]` is greater than `a[j]`, the two elements are swapped using XOR.
4. The process continues until the loops finish.
5. The sorted array is printed.

## 💻 Program

```python
a = [10, 5, 98, 60, 32, 40, 100]

for i in range(0, len(a)-1, 1):
    for j in range(i+1, len(a)-1, 1):
        if a[i] > a[j]:
            a[i] = a[i] ^ a[j]
            a[j] = a[i] ^ a[j]
            a[i] = a[i] ^ a[j]

print(a)
```

## 🔍 Program Tracking

Initial array:

```text
[10, 5, 98, 60, 32, 40, 100]
```

The array contains 7 elements, with indices from `0` to `6`.

### Step 1: `i = 0`

The outer loop selects `a[0] = 10`.

The inner loop compares `10` with the elements at indices `1` through `5`.

| `j` | Comparison | Action | Array after comparison |
|---:|---|---|---|
| 1 | `10 > 5` | Swap | `[5, 10, 98, 60, 32, 40, 100]` |
| 2 | `5 > 98` | No swap | `[5, 10, 98, 60, 32, 40, 100]` |
| 3 | `5 > 60` | No swap | `[5, 10, 98, 60, 32, 40, 100]` |
| 4 | `5 > 32` | No swap | `[5, 10, 98, 60, 32, 40, 100]` |
| 5 | `5 > 40` | No swap | `[5, 10, 98, 60, 32, 40, 100]` |

After this iteration, the smallest value, `5`, is at index `0`.

### Step 2: `i = 1`

Now `a[1] = 10`.

| `j` | Comparison | Action | Array after comparison |
|---:|---|---|---|
| 2 | `10 > 98` | No swap | `[5, 10, 98, 60, 32, 40, 100]` |
| 3 | `10 > 60` | No swap | `[5, 10, 98, 60, 32, 40, 100]` |
| 4 | `10 > 32` | No swap | `[5, 10, 98, 60, 32, 40, 100]` |
| 5 | `10 > 40` | No swap | `[5, 10, 98, 60, 32, 40, 100]` |

The value `10` remains at index `1`.

### Step 3: `i = 2`

Now `a[2] = 98`.

| `j` | Comparison | Action | Array after comparison |
|---:|---|---|---|
| 3 | `98 > 60` | Swap | `[5, 10, 60, 98, 32, 40, 100]` |
| 4 | `60 > 32` | Swap | `[5, 10, 32, 98, 60, 40, 100]` |
| 5 | `32 > 40` | No swap | `[5, 10, 32, 98, 60, 40, 100]` |

After these comparisons, the value at index `2` is `32`.

### Step 4: `i = 3`

Now `a[3] = 98`.

| `j` | Comparison | Action | Array after comparison |
|---:|---|---|---|
| 4 | `98 > 60` | Swap | `[5, 10, 32, 60, 98, 40, 100]` |
| 5 | `60 > 40` | Swap | `[5, 10, 32, 40, 98, 60, 100]` |

### Step 5: `i = 4`

Now `a[4] = 98`.

| `j` | Comparison | Action | Array after comparison |
|---:|---|---|---|
| 5 | `98 > 60` | Swap | `[5, 10, 32, 40, 60, 98, 100]` |

### Step 6: `i = 5`

The inner loop starts at index `6`, but its stopping value is also `6`.

Therefore, it performs no comparisons.

The loops finish.

## 📊 Complete Tracking Summary

| Outer index `i` | Array after the inner loop |
|---:|---|
| 0 | `[5, 10, 98, 60, 32, 40, 100]` |
| 1 | `[5, 10, 98, 60, 32, 40, 100]` |
| 2 | `[5, 10, 32, 98, 60, 40, 100]` |
| 3 | `[5, 10, 32, 40, 98, 60, 100]` |
| 4 | `[5, 10, 32, 40, 60, 98, 100]` |
| 5 | `[5, 10, 32, 40, 60, 98, 100]` |

## 🖨️ Output

```text
[5, 10, 32, 40, 60, 98, 100]
```

## 🧠 Understanding XOR Swapping

The following three statements swap two values without a third variable:

```python
a[i] = a[i] ^ a[j]
a[j] = a[i] ^ a[j]
a[i] = a[i] ^ a[j]
```

For example, to swap `10` and `5`:

```text
Initially:
a[i] = 10
a[j] = 5

After XOR swapping:
a[i] = 5
a[j] = 10
```

## 📚 Concepts Practiced

- Python lists and indexing
- Nested `for` loops
- Comparison operators
- Bitwise XOR operator
- Swapping without a temporary variable
- Ascending order sorting
- In-place modification of a list

## ⏱️ Complexity

- **Time Complexity:** `O(n²)` in the general case.
- **Auxiliary Space Complexity:** `O(1)`.

## 💡 Important Note

Both loops exclude the last index because `range()` does not include its stopping value. Your current input is sorted correctly because `100` is already the largest value.

To correctly sort arrays when the last element may be smaller than other elements, change the inner loop to:

```python
for j in range(i+1, len(a), 1):
```

This allows the inner loop to compare against the last element too.
