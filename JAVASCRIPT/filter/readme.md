# JavaScript Filter Function – Find Even Numbers 🔍

## 📌 Description

This JavaScript program uses the **`filter()` method** to find all even numbers from an array.

The `filter()` method checks each element against a condition and returns a **new array containing only the elements that satisfy the condition**.

The original array remains unchanged.

## 💻 Program

```javascript
const numbers = [1,2,3,4,5,7,8,9,10];

const even_numbers = numbers.filter(n => n % 2 == 0);

console.log("even numbers", even_numbers);
console.log("Numbers:", numbers);
```

## 🧠 How the Program Works

The program follows three steps:

1. Create an array named `numbers`.
2. Use `filter()` to check whether each number is even.
3. Store the even numbers in a new array and print both arrays.

### Understanding `filter()`

```javascript
numbers.filter(n => n % 2 == 0);
```

- `numbers` is the original array.
- `filter()` checks every element.
- `n` represents the current element.
- `%` is the modulo operator, which returns the remainder.
- `n % 2 == 0` checks whether the number is divisible by `2` without a remainder.
- If the condition is `true`, the element is included in the new array.
- If the condition is `false`, the element is excluded.

## 🔍 Program Tracking

Original array:

```text
numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]
```

The `filter()` method checks each number one by one.

| Step | `n` | `n % 2` | Condition | Action |
|---:|---:|---:|---|---|
| 1 | 1 | 1 | False | Exclude |
| 2 | 2 | 0 | True | Include |
| 3 | 3 | 1 | False | Exclude |
| 4 | 4 | 0 | True | Include |
| 5 | 5 | 1 | False | Exclude |
| 6 | 7 | 1 | False | Exclude |
| 7 | 8 | 0 | True | Include |
| 8 | 9 | 1 | False | Exclude |
| 9 | 10 | 0 | True | Include |

### Array Transformation

```text
Original Array:
[1, 2, 3, 4, 5, 7, 8, 9, 10]

              ↓ filter(n => n % 2 == 0)

Even Numbers:
[2, 4, 8, 10]
```

Only the elements satisfying the condition are included in the new array.

## 🖨️ Output

```text
even numbers [ 2, 4, 8, 10 ]
Numbers: [ 1, 2, 3, 4, 5, 7, 8, 9, 10 ]
```

*Note: The exact spacing in the console output may vary.*

## 📚 Concepts Practiced

- JavaScript arrays
- `const` variable declaration
- `filter()` method
- Arrow functions (`=>`)
- Modulo operator (`%`)
- Conditional expressions
- Array filtering
- `console.log()`

## 💡 Key Takeaways

- `filter()` selects elements based on a condition.
- It returns a new array containing only matching elements.
- The original array remains unchanged.
- An even number gives a remainder of `0` when divided by `2`.

**In one line:** `filter()` checks every number and keeps only the even numbers in a new array.
