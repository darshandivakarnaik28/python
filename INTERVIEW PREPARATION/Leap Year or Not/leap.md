# Logic Behind Leap Year

Normally, we consider one year as:

```text
365 days
```

But the actual time required for the Earth to complete one revolution is slightly more than 365 days.

According to the approximation used in this explanation, the extra time is approximately:

```text
5 hours 55 minutes 40 seconds 22 milliseconds
```

This extra time accumulates every year.

### 1. Adding the Extra Hours and Minutes

The extra time from each year is accumulated.

After approximately 4 years, the accumulated extra time becomes close to **24 hours**, which is approximately **one extra day**.

Therefore, every 4 years, we add one extra day to the calendar.

So:

```text
Normal year = 365 days
Leap year   = 366 days
```

This is why a year divisible by 4 is generally considered a leap year.

---

### 2. Why Do We Exclude Every 100th Year?

The extra time does not accumulate to exactly one day every 4 years.

If we simply added one day every 4 years, we would add slightly too much time over a long period.

Therefore, after every 100 years, we skip the extra leap day.

For example:

```text
1700 → Not a leap year
1800 → Not a leap year
1900 → Not a leap year
```

Even though these years are divisible by 4, they are not leap years because they are century years.

This correction prevents the calendar from gaining an extra day over long periods.

---

### 3. Why Is Every 400th Year a Leap Year?

Even after removing the leap day at every 100th year, the remaining fractional time continues to accumulate.

Over approximately 400 years, this remaining difference becomes close to one complete day.

Therefore, the 400th year gets the leap day back.

For example:

```text
1600 → Leap year
2000 → Leap year
2400 → Leap year
```

So the final rule becomes:

```text
Divisible by 4
        ↓
   Usually Leap Year
        ↓
If divisible by 100
        ↓
   Not a Leap Year
        ↓
But if divisible by 400
        ↓
      Leap Year
```

---

## 🔑 Simple Understanding

The leap-year rule is basically a **calendar correction**.

```text
Extra time every year
        ↓
Accumulates over 4 years
        ↓
Approximately 1 extra day
        ↓
Add 1 day → Leap Year
        ↓
Small error accumulates over 100 years
        ↓
Remove one leap day
        ↓
Remaining error accumulates over 400 years
        ↓
Add the leap day back
```

Therefore, the program uses:

```python
if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0):
```

This condition represents the **calendar correction rule**:

- Divisible by `4` → generally leap year
- Divisible by `100` → remove the leap day
- Divisible by `400` → add the leap day back