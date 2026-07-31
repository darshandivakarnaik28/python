Your learning goal is to **learn an optimized Python program to check whether a number is prime**, not just copy the code.

## Approach (Before the Code)

A simple method checks divisibility from **2 to n-1**, but this is inefficient.

### Optimization 1: Check only up to √n

If a number `n` has a factor larger than √n, then it must also have a corresponding factor smaller than √n.

**Example:**

* `36 = 4 × 9`
* `36 = 6 × 6`
* `36 = 9 × 4`

So, if no factor is found up to √36 = 6, there won't be any factor after 6.

### Optimization 2: Skip even numbers

* `2` is the only even prime number.
* Any other even number is not prime.
* After checking `2`, check only odd numbers.

---

## Optimized Python Program

```python
import math

n = int(input("Enter a number: "))

if n <= 1:
    print("Not Prime")

elif n == 2:
    print("Prime")

elif n % 2 == 0:
    print("Not Prime")

else:
    prime = True

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime")
    else:
        print("Not Prime")
```

---

## How It Works

1. Numbers less than or equal to **1** are not prime.
2. If the number is **2**, it is prime.
3. If the number is even (`n % 2 == 0`), it is not prime.
4. Check only odd divisors from **3** to **√n**.
5. If any divisor divides the number exactly, it is not prime.
6. Otherwise, it is prime.

---

## Practical Example

**Input:**

```
Enter a number: 29
```

**Checking:**

* √29 ≈ 5.38
* Check only `3` and `5`
* Neither divides 29

**Output:**

```
Prime
```

---

## Time and Space Complexity

* **Naive approach:** Check from `2` to `n-1`

  * **Time Complexity:** `O(n)`
  * **Space Complexity:** `O(1)`

* **Optimized approach (above):**

  * **Time Complexity:** `O(√n)`
  * **Space Complexity:** `O(1)`

---

## Common Mistakes

* Checking all numbers up to `n-1` instead of `√n`.
* Forgetting that `0` and `1` are **not** prime numbers.
* Not handling the special case for `2`.
* Checking even numbers after already ruling them out.

---

## Quick Summary

* A prime number has exactly **two factors: 1 and itself**.
* You only need to check divisors up to **√n**.
* Skip even numbers after checking for `2`.
* This reduces the time complexity from **O(n)** to **O(√n)**.

---

## 3 Revision Questions

1. Why do we only check divisors up to **√n**?
2. Why is `2` handled as a special case?
3. What are the time complexities of the naive and optimized approaches?

Would you like:

1. a **deeper explanation** of why checking up to √n works,
2. **coding examples** (e.g., printing all prime numbers in a range),
3. **interview questions** on prime numbers,
4. or a **quiz** on this topic?
