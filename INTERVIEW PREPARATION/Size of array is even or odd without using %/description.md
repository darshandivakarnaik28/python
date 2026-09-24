# Check Array Size Even or Odd Without `%` 🔢

This Python program checks whether the **size of an array is even or odd without using the modulo (`%`) operator**.

## 📌 Description

Normally, we can check whether a number is even or odd using:

```text
number % 2
```

But this program does **not** use the `%` operator.

Instead, it uses two variables:

* `i` starts from `0`
* `j` starts from the length of the array
* In every loop:

  * `i` is increased by `1`
  * `j` is decreased by `1`

If `i` and `j` become equal, the array size is **even**.

If they cross each other, the array size is **odd**.

## 💻 Program

```python
a = [1, 2, 3, 4, 6, 5]

i = 0
j = len(a)

while (i < j):
    i += 1
    j -= 1

if i == j:
    print("even")
else:
    print("odd")
```

## 🔍 Program Tracking

Let's take:

```text
a = [1, 2, 3, 4, 6, 5]
```

The array contains:

```text
6 elements
```

So:

```text
i = 0
j = len(a)
j = 6
```

### Step-by-Step Tracking

| Step    | `i` | `j` | Condition `i < j` |
| ------- | --: | --: | ----------------- |
| Initial |   0 |   6 | True              |
| 1       |   1 |   5 | True              |
| 2       |   2 |   4 | True              |
| 3       |   3 |   3 | False             |

The loop stops when:

```text
i = 3
j = 3
```

Now:

```python
if i == j:
```

is `True`.

Therefore:

```text
even
```

### Final Result

```text
Array size = 6
6 is even
```

So the output is:

```text
even
```

## 📊 Visual Tracking

```text
Array size = 6

Start:
i → 0  1  2  3  4  5
j → 6

Move i forward and j backward:

i = 1
j = 5

i = 2
j = 4

i = 3
j = 3
       ↑
    They meet

       ↓

     EVEN
```

## 🔍 Odd Number Example

Let's consider an array with 5 elements:

```python
a = [1, 2, 3, 4, 5]
```

Initially:

```text
i = 0
j = 5
```

Tracking:

| Step    | `i` | `j` |
| ------- | --: | --: |
| Initial |   0 |   5 |
| 1       |   1 |   4 |
| 2       |   2 |   3 |
| 3       |   3 |   2 |

Now:

```text
i = 3
j = 2
```

They have crossed, so:

```text
i != j
```

Therefore:

```text
odd
```

## 🧠 Main Logic

The program repeatedly removes **two positions/elements worth of size** from consideration:

```text
6 → 4 → 2 → 0
```

For an even-sized array, the two sides meet exactly:

```text
6 → 4 → 2 → 0
```

For an odd-sized array, one position remains between them before they cross:

```text
5 → 3 → 1
```

The program detects this using the relationship between `i` and `j`, rather than using `%`.

## 📊 Simple Flow

```text
              Start
                ↓
          Create array
                ↓
          i = 0, j = len(a)
                ↓
             i < j?
            ↙     ↘
          Yes      No
           ↓        ↓
       i += 1    Check i == j
       j -= 1       ↙    ↘
           ↓      Yes     No
           └────→ ↓       ↓
                Even     Odd
```

## 📚 Concepts Practiced

* Python lists
* `len()` function
* `while` loop
* Increment operator
* Decrement operation
* Comparison operators
* Array/list size
* Finding even or odd without `%`

## ⏱️ Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The loop runs approximately half as many iterations as the size of the array.

## 💡 Key Idea

```text
Find array length
       ↓
Start i from 0
Start j from length
       ↓
Move i forward
Move j backward
       ↓
Do they meet?
   ↙       ↘
 Yes       No
  ↓         ↓
Even       Odd
```

The main purpose of this program is to demonstrate how **even/odd checking can be performed without directly using the modulo (`%`) operator**.
