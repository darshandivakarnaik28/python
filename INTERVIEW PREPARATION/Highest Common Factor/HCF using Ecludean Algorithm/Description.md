# HCF Using Euclidean Algorithm 🔢

This Python program finds the **Highest Common Factor (HCF)** of two positive numbers using the **Euclidean Algorithm**.

## 📌 Description

The program uses the **subtraction method of the Euclidean Algorithm**.

The basic idea is:

* If `a` is greater than `b`, subtract `b` from `a`.
* Otherwise, subtract `a` from `b`.
* Continue this process until `a` and `b` become equal.
* The final value is the **HCF**.

## 💻 Program

```python
def get_hcf(a, b):

    while a != b:

        if a > b:
            a = a - b

        else:
            b = b - a

    return a


a = int(input("Enter a :"))
b = int(input("Enter b :"))

print(get_hcf(a, b))
```

## 🔍 Program Tracking

Let's take:

```text
a = 18
b = 12
```

Initially:

```text
a = 18
b = 12
```

### Step 1

Check:

```text
a != b
18 != 12 → True
```

Since:

```text
a > b
18 > 12 → True
```

Subtract:

```text
a = a - b
a = 18 - 12
a = 6
```

Now:

```text
a = 6
b = 12
```

---

### Step 2

Check:

```text
a != b
6 != 12 → True
```

Now `a` is smaller than `b`, so:

```text
b = b - a
b = 12 - 6
b = 6
```

Now:

```text
a = 6
b = 6
```

---

### Step 3

Check:

```text
a != b
6 != 6 → False
```

The loop stops.

The function returns:

```text
HCF = 6
```

### Output

```text
6
```

## 📊 Tracking Table

| Step    |  a |  b | Operation   |
| ------- | -: | -: | ----------- |
| Initial | 18 | 12 | —           |
| 1       |  6 | 12 | `a = a - b` |
| 2       |  6 |  6 | `b = b - a` |
| End     |  6 |  6 | `a == b`    |

Therefore:

```text
HCF = 6
```

## 🧠 How the Logic Works

The main loop is:

```python
while a != b:
```

It keeps running as long as the two numbers are different.

Then:

```python
if a > b:
    a = a - b
```

If `a` is larger, subtract `b` from `a`.

Otherwise:

```python
else:
    b = b - a
```

If `b` is larger, subtract `a` from `b`.

Eventually, both numbers become equal.

```text
a == b
```

That common value is the **HCF**.

## 📌 Why Is This the Euclidean Algorithm?

The Euclidean Algorithm is based on the idea that the HCF does not change when the smaller number is subtracted from the larger number.

For example:

```text
HCF(18, 12)
       ↓
HCF(6, 12)
       ↓
HCF(6, 6)
       ↓
     HCF = 6
```

So this program uses the **subtraction-based form of the Euclidean Algorithm**.

## 📊 Simple Flow

```text
             Start
               ↓
          Get a and b
               ↓
           a != b ?
          ↙       ↘
        No         Yes
        ↓           ↓
     Return a    Is a > b?
                    ↙    ↘
                  Yes     No
                   ↓       ↓
              a = a-b   b = b-a
                   ↘       ↙
                     ↓
                 Check again
                     ↓
                  a == b
                     ↓
                  Return a
```

## 📚 Concepts Practiced

* Python functions
* `while` loop
* `if-else` conditions
* Comparison operators
* Arithmetic subtraction
* Function return value
* Euclidean Algorithm
* Finding HCF/GCD

## ⏱️ Complexity

This subtraction-based version can take more iterations than the modulo-based Euclidean Algorithm, especially when the two numbers are very different.

* **Space Complexity:** `O(1)`
* **Time Complexity:** Depends on the number of subtraction steps.

## 🚀 Future Improvement

The Euclidean Algorithm can also be implemented using the **modulo operator `%`**:

```text
a, b → a % b → repeat
```

This version is generally much faster than repeatedly subtracting the smaller number.
