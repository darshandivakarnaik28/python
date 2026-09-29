# Basic Recursion Example 🔁

This Python program demonstrates the basic concept of **recursion**.

A function is called recursively when it **calls itself** until a particular condition becomes false.

## 📌 Program

```python
def num(n):
    if n < 5:
        print(n)
        n += 1
        num(n)

num(1)
```

## 🧠 How the Program Works

The function `num(n)` performs three steps:

1. Check whether `n < 5`.
2. If true, print `n`.
3. Increase `n` by `1` and call the function again.

The recursive call continues until:

```text
n < 5
```

becomes false.

When `n = 5`:

```text
5 < 5 → False
```

So the function stops calling itself.

---

# 🔍 Complete Program Trace

The program starts with:

```text
num(1)
```

### Step 1

Function receives:

```text
n = 1
```

Check:

```text
1 < 5 → True
```

Print:

```text
1
```

Increment:

```text
n = 1 + 1
n = 2
```

Recursive call:

```text
num(2)
```

---

### Step 2

Function receives:

```text
n = 2
```

Check:

```text
2 < 5 → True
```

Print:

```text
2
```

Increment:

```text
n = 2 + 1
n = 3
```

Recursive call:

```text
num(3)
```

---

### Step 3

Function receives:

```text
n = 3
```

Check:

```text
3 < 5 → True
```

Print:

```text
3
```

Increment:

```text
n = 3 + 1
n = 4
```

Recursive call:

```text
num(4)
```

---

### Step 4

Function receives:

```text
n = 4
```

Check:

```text
4 < 5 → True
```

Print:

```text
4
```

Increment:

```text
n = 4 + 1
n = 5
```

Recursive call:

```text
num(5)
```

---

### Step 5

Function receives:

```text
n = 5
```

Check:

```text
5 < 5 → False
```

Therefore, the `if` block is not executed.

No print occurs.

No further recursive call occurs.

The recursion stops.

---

# 📊 Complete Trace Table

| Function Call | `n` | Condition `n < 5` | Action | Next Call |
|---|---:|---|---|---|
| `num(1)` | 1 | True | Print `1`, increment | `num(2)` |
| `num(2)` | 2 | True | Print `2`, increment | `num(3)` |
| `num(3)` | 3 | True | Print `3`, increment | `num(4)` |
| `num(4)` | 4 | True | Print `4`, increment | `num(5)` |
| `num(5)` | 5 | False | Stop | None |

## 🖨️ Output

```text
1
2
3
4
```

---

# 🔄 Recursion Call Flow

The function calls itself like this:

```text
num(1)
   ↓
num(2)
   ↓
num(3)
   ↓
num(4)
   ↓
num(5)
   ↓
condition false
   ↓
Stop
```

---

# 🧱 Understanding the Call Stack

When recursive calls are made, each function call is kept in the **call stack**.

During the execution, the stack grows like this:

```text
num(1)
   ↓
num(2)
   ↓
num(3)
   ↓
num(4)
   ↓
num(5)
```

At `num(5)`, the condition is false, so no new function is called.

The program then finishes.

In this particular program, there is **no code after the recursive call**, so there is no visible action during the return/unwinding phase.

---

# 🛑 Where Does Recursion Stop?

The stopping condition is:

```python
if n < 5:
```

When:

```text
n = 5
```

we get:

```text
5 < 5 → False
```

Therefore, the function does not call itself again.

This condition acts as the **termination condition** for the recursion.

---

# 📊 Simple Flow

```text
              Start
                ↓
             num(1)
                ↓
             n < 5?
            ↙      ↘
          Yes       No
           ↓         ↓
        Print n     Stop
           ↓
        n = n + 1
           ↓
       num(n)
           ↓
      Check again
```

## 📚 Concepts Practiced

- Python functions
- Recursion
- Recursive function calls
- `if` condition
- Increment operation
- Call stack
- Termination condition

## 💡 Key Idea

**Recursion means a function calling itself.**

In this program:

```text
num(1)
 → num(2)
   → num(3)
     → num(4)
       → num(5)
```

When `n` becomes `5`, the condition becomes false and the recursion stops.

### In One Line

**Check condition → Print number → Increase number → Call the same function → Stop when condition becomes false.**