# Highest Common Factor (HCF) 🔢

This Python program finds the **Highest Common Factor (HCF)** of two positive numbers.

## 📌 Description

The program takes two numbers as input and finds their common factors.

It works by:

1. Taking two numbers `a` and `b`.
2. Finding the smaller number using `min(a, b)`.
3. Checking every number from `1` up to the smaller number.
4. Checking whether the number divides both `a` and `b`.
5. If it is a common factor, storing it in `hcf`.
6. Since the factors are checked in increasing order, the last common factor stored is the **Highest Common Factor**.

## 💻 Program

```python
def get_hcf(a, b):
    hcf = 0

    for i in range(1, min(a, b)):
        if a % i == 0 and b % i == 0:
            hcf = i

    return hcf


a = int(input("Enter a a :"))
b = int(input("Enter a b :"))

print(get_hcf(a, b))
```

## 🔍 Program Tracking

Let's take:

```text
a = 12
b = 18
```

First:

```text
hcf = 0
```

The smaller number is:

```text
min(12, 18) = 12
```

So the loop checks:

```text
i = 1 to 11
```

### Step-by-Step Tracking

|  i | `12 % i` | `18 % i` | Common Factor? | hcf |
| -: | -------: | -------: | :------------: | --: |
|  1 |        0 |        0 |       Yes      |   1 |
|  2 |        0 |        0 |       Yes      |   2 |
|  3 |        0 |        0 |       Yes      |   3 |
|  4 |        0 |        2 |       No       |   3 |
|  5 |        2 |        3 |       No       |   3 |
|  6 |        0 |        0 |       Yes      |   6 |
|  7 |        5 |        4 |       No       |   6 |
|  8 |        4 |        2 |       No       |   6 |
|  9 |        3 |        0 |       No       |   6 |
| 10 |        2 |        8 |       No       |   6 |
| 11 |        1 |        7 |       No       |   6 |

The common factors are:

```text
1, 2, 3, 6
```

The last and highest common factor is:

```text
HCF = 6
```

Therefore, the output is:

```text
6
```

## 🧠 How the Condition Works

The following condition checks whether `i` is a factor of **both** numbers:

```python
if a % i == 0 and b % i == 0:
```

* `a % i == 0` → `i` is a factor of `a`
* `b % i == 0` → `i` is a factor of `b`
* `and` → both conditions must be true

If both are true:

```python
hcf = i
```

The current common factor is stored as the HCF.

Because the loop checks factors from **small to large**, every new common factor replaces the previous one. Therefore, after the loop finishes, `hcf` contains the highest common factor.

## 📊 Simple Flow

```text
           Start
             ↓
        Get a and b
             ↓
       hcf = 0
             ↓
    Find min(a, b)
             ↓
     Check i from 1
     to min(a,b)-1
             ↓
   Is i a factor of
      both a and b?
        ↙       ↘
      Yes        No
       ↓          ↓
   hcf = i     Continue
       ↓          ↓
       └──→ Next i
             ↓
       Return hcf
             ↓
            End
```

## 📚 Concepts Practiced

* Python functions
* `for` loop
* `min()` function
* Modulo operator `%`
* `and` operator
* Variables
* Function return value
* Finding common factors

## ⏱️ Complexity

* **Time Complexity:** `O(min(a, b))`
* **Space Complexity:** `O(1)`

The program checks possible factors up to the smaller of the two numbers.

## 🚀 Future Improvement

This program can be optimized using the **Euclidean Algorithm**, which can find the HCF much faster for large numbers.
