# Double Recursion Example 🔁🔁

This Python program demonstrates **double recursion**, also called **binary recursion**.

In normal recursion, a function usually makes **one recursive call** to itself.

In double recursion, a function makes **two recursive calls**.

## 📌 Program

```python
def hello(n):
    if n > 0:
        print(n)
        n -= 1
        hello(n)
        hello(n)

hello(3)
```

## 🧠 How the Program Works

The function first checks:

```python
if n > 0:
```

If the condition is true:

1. Print `n`.
2. Decrease `n` by `1`.
3. Call `hello(n)` for the first time.
4. After the first recursive call completely finishes, call `hello(n)` again.

The important part is:

```python
hello(n)
hello(n)
```

There are **two recursive calls**.

The recursion stops when:

```text
n = 0
```

because:

```text
0 > 0 → False
```

---

# 🔍 Complete Program Trace

The program starts with:

```text
hello(3)
```

### Step 1 — `hello(3)`

```text
n = 3
3 > 0 → True
```

Print:

```text
3
```

Decrease:

```text
n = 2
```

Now there are two calls:

```text
hello(2)   ← First call
hello(2)   ← Second call
```

The **first call must finish completely** before the second call starts.

---

# 🌳 Complete Recursion Tree

The easiest way to understand double recursion is using a recursion tree:

```text
                         hello(3)
                         print 3
                        /       \
                       /         \
                 hello(2)       hello(2)
                 print 2        print 2
                /      \       /      \
           hello(1)  hello(1) hello(1) hello(1)
           print 1   print 1  print 1  print 1
            / \       / \      / \      / \
           0   0     0   0    0   0    0   0
```

Each node with `n > 0` creates **two more recursive calls**.

---

# 📊 Step-by-Step Execution

## 1. `hello(3)`

Prints:

```text
3
```

Then:

```text
hello(2)
hello(2)
```

---

## 2. First `hello(2)`

Prints:

```text
2
```

Then:

```text
hello(1)
hello(1)
```

---

## 3. First `hello(1)`

Prints:

```text
1
```

Then:

```text
hello(0)
hello(0)
```

For both calls:

```text
0 > 0 → False
```

So they stop.

The first `hello(1)` is now completely finished.

---

## 4. Second `hello(1)`

The second `hello(1)` now starts.

Prints:

```text
1
```

Then:

```text
hello(0)
hello(0)
```

Both stop because:

```text
0 > 0 → False
```

The first `hello(2)` is now completely finished.

---

## 5. Second `hello(2)`

Now the second `hello(2)` from the original `hello(3)` starts.

It prints:

```text
2
```

Then:

```text
hello(1)
hello(1)
```

Each `hello(1)` prints `1` and makes two `hello(0)` calls.

---

# 🖨️ Complete Output

The output is:

```text
3
2
1
1
2
1
1
```

So the number of printed values is:

```text
3 → 1 time
2 → 2 times
1 → 4 times
```

Total:

```text
1 + 2 + 4 = 7
```

---

# 📊 Complete Tracking Table

| Call | Prints | Recursive Calls |
|---|---:|---|
| `hello(3)` | 3 | `hello(2)`, `hello(2)` |
| First `hello(2)` | 2 | `hello(1)`, `hello(1)` |
| First `hello(1)` | 1 | `hello(0)`, `hello(0)` |
| `hello(0)` | Nothing | Stop |
| `hello(0)` | Nothing | Stop |
| Second `hello(1)` | 1 | `hello(0)`, `hello(0)` |
| `hello(0)` | Nothing | Stop |
| `hello(0)` | Nothing | Stop |
| Second `hello(2)` | 2 | `hello(1)`, `hello(1)` |
| First `hello(1)` | 1 | `hello(0)`, `hello(0)` |
| `hello(0)` | Nothing | Stop |
| `hello(0)` | Nothing | Stop |
| Second `hello(1)` | 1 | `hello(0)`, `hello(0)` |
| `hello(0)` | Nothing | Stop |
| `hello(0)` | Nothing | Stop |

---

# 🔄 Call Order

It is important to understand that Python executes the calls **one after another**.

The execution order is:

```text
hello(3)
   ↓
hello(2)          ← First
   ↓
hello(1)          ← First
   ↓
hello(0)
   ↓
hello(0)
   ↓
hello(1)          ← Second
   ↓
hello(0)
   ↓
hello(0)
   ↓
hello(2)          ← Second
   ↓
hello(1)
   ↓
hello(0)
   ↓
hello(0)
   ↓
hello(1)
   ↓
hello(0)
   ↓
hello(0)
```

---

# 🧱 Why Is It Called Double Recursion?

Normal recursion:

```text
Function
   ↓
Function
   ↓
Function
   ↓
Function
```

One call creates **one** new recursive call.

Double recursion:

```text
              Function
             /        \
        Function      Function
        /     \       /     \
   Function Function Function Function
```

One call creates **two** new recursive calls.

Therefore, your program is a good example of **double/binary recursion**.

---

# 🛑 Termination Condition

The recursion stops at:

```python
if n > 0:
```

When:

```text
n = 0
```

the condition becomes:

```text
0 > 0 → False
```

Therefore, no more recursive calls are made.

This prevents the recursion from continuing indefinitely.

---

# 📊 Simple Flow

```text
             hello(3)
             print 3
             /      \
            ↓        ↓
        hello(2)  hello(2)
        print 2   print 2
         /  \      /  \
        ↓    ↓    ↓    ↓
       1     1    1     1
       ↓     ↓    ↓     ↓
       0     0    0     0
```

## 📚 Concepts Practiced

- Python functions
- Recursion
- Double recursion
- Binary recursion
- Recursive call tree
- Call stack
- Base/termination condition
- Execution order

## 💡 Key Idea

The most important part of this program is:

```python
hello(n)
hello(n)
```

Each function call creates **two more recursive calls**.

For `hello(3)`:

```text
hello(3)
    ↓
2 calls
    ↓
4 calls
    ↓
8 calls
```

The recursion grows like a **binary tree**.

### In One Line

**Print `n` → decrease `n` → make the first recursive call → finish it → make the second recursive call → stop when `n` becomes `0`.**