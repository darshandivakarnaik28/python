# Prime Number Checker 🔢

A simple Python program to check whether a given positive number is a **Prime Number** or **Not a Prime Number**.

## 📌 About the program

This program determines whether a number is prime by counting its factors.

### Approach Used

The program works in two phases:

1. **Find the factors**

   * Check every number from `1` to `n`.
   * If `n` is exactly divisible by `i`, then `i` is a factor of `n`.

2. **Count the factors**

   * Increase the factor count whenever a factor is found.
   * A number is considered **Prime** if it has exactly **2 factors**:

     * `1`
     * The number itself
   * Otherwise, it is **Not Prime**.

## 💻 Program

```python
def print_prime(n):

    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return count


n = int(input("Enter a positive number: "))

count = print_prime(n)

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")
```

## ▶️ Example

### Input

```text
Enter a positive number: 7
```

### Factors of 7

```text
1, 7
```

Number of factors = `2`

### Output

```text
Prime Number
```

---

### Another Example

### Input

```text
Enter a positive number: 12
```

### Factors of 12

```text
1, 2, 3, 4, 6, 12
```

Number of factors = `6`

### Output

```text
Not a Prime Number
```

## 🧠 Logic

The main condition used to find a factor is:

```python
n % i == 0
```

If the remainder is `0`, then `i` is a factor of `n`.

The final decision is:

```text
Number of factors = 2  → Prime Number
Number of factors ≠ 2  → Not a Prime Number
```

## ⏱️ Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

The program checks every number from `1` to `n` to find all possible factors.

## 📚 Concepts Practiced

* Python functions
* `for` loop
* `range()`
* Modulo operator `%`
* Counting using a variable
* Function return values
* User input
* Conditional statements (`if-else`)

## 🚀 Future Improvement

The program can be optimized by checking factors only up to `√n`, which can reduce the number of iterations for large numbers.

---

### Author

**Darshan Divakar Naik**

A simple Python practice project focused on understanding **loops, functions, factors, and conditional logic**.
