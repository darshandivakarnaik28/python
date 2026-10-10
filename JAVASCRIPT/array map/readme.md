# JavaScript Map Function – Square of Numbers 🔢

## 📌 Description

This JavaScript program uses the **`map()` function** to calculate the square of every number in an array.

The `map()` method processes each element of an array, applies a function to it, and returns a **new array** containing the results.

The original array remains unchanged.

## 💻 Program

```javascript
const numbers = [1,2,3,4,5,6,7,8,9,10];

const square_numbers = numbers.map(n => n**2);

console.log("Numbers:", numbers);
console.log("Squared Numbers:", square_numbers);
```

## 🧠 How the Program Works

The program follows three steps:

1. Create an array named `numbers` containing numbers from `1` to `10`.
2. Use `map()` to calculate the square of each number.
3. Print the original array and the new array of squared numbers.

### Understanding `map()`

```javascript
numbers.map(n => n**2);
```

- `numbers` is the original array.
- `map()` visits every element in the array.
- `n` represents the current element.
- `n => n**2` is an arrow function that returns the square of `n`.
- `**2` means raising a number to the power of `2`.
- `map()` returns a new array containing the squared values.

## 🔍 Program Tracking

Original array:

```text
numbers = [1,2,3,4,5,6,7,8,9,10]
```

The `map()` function processes each element one by one.

| Step | `n` | Calculation (`n ** 2`) | Result |
|---:|---:|---|---:|
| 1 | 1 | `1 ** 2` | 1 |
| 2 | 2 | `2 ** 2` | 4 |
| 3 | 3 | `3 ** 2` | 9 |
| 4 | 4 | `4 ** 2` | 16 |
| 5 | 5 | `5 ** 2` | 25 |
| 6 | 6 | `6 ** 2` | 36 |
| 7 | 7 | `7 ** 2` | 49 |
| 8 | 8 | `8 ** 2` | 64 |
| 9 | 9 | `9 ** 2` | 81 |
| 10 | 10 | `10 ** 2` | 100 |

Each calculated value is added to the new array.

### Array Transformation

```text
Original Array:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

            ↓ map(n => n ** 2)

Squared Array:
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

## 🖨️ Output

```text
Numbers: [1,2,3,4,5,6,7,8,9,10]

Squared Numbers: [1,4,9,16,25,36,49,64,81,100]
```

## 📊 Difference Between the Original and New Arrays

| Original Array | Squared Array |
|---:|---:|
| 1 | 1 |
| 2 | 4 |
| 3 | 9 |
| 4 | 16 |
| 5 | 25 |
| 6 | 36 |
| 7 | 49 |
| 8 | 64 |
| 9 | 81 |
| 10 | 100 |

The original array is not modified because `map()` creates and returns a new array.

## 📚 Concepts Practiced

- JavaScript arrays
- `const` variable declaration
- `map()` method
- Arrow functions (`=>`)
- Exponentiation operator (`**`)
- Array transformation
- `console.log()`

## 💡 Key Takeaways

- `map()` transforms every element of an array.
- It returns a new array containing the transformed values.
- The original array remains unchanged.
- The callback function determines how each element is transformed.

**In one line:** `map()` takes each number, squares it, and stores the result in a new array.
