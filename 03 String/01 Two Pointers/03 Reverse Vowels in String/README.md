Here’s your **README-style breakdown** — sharp, no nonsense, and actually interview-level.

---

# 🔁 Reverse Vowels of a String — Two Pointer Pattern

![Visualization](https://github.com/mdzaheerjk/DSA-Patterns/blob/main/03%20String/src/reverse%20vowels.png)

---

## 🧠 Problem Understanding

You’re given a string `s`.
Your job:

👉 Reverse **only the vowels** in the string
👉 Keep everything else in the same position

### Example

```python
Input:  "hello"
Output: "holle"

Input:  "leetcode"
Output: "leotcede"
```

---

## ⚡ Core Idea

You don’t need fancy logic. This is straight **Two Pointer swapping**:

* Start from both ends
* Find vowels on both sides
* Swap them
* Move inward

---

## 🔍 Your Code

```python
class Solution(object):
    def reverseVowels(self, s):
        vowels=["A",'E','I','O','U','a','e','i','o','u']
        i=0
        j=len(s)-1
        lst=list(s)
        while i<j:
            if not lst[i] in vowels:
                i+=1
            elif not lst[j] in vowels:
                j-=1
            elif lst[i] in vowels and lst[j] in vowels:
                lst[i],lst[j]=lst[j],lst[i]
                i+=1
                j-=1
        return "".join(lst)
```

---

## 🧩 Step-by-Step Logic

### 1. Convert string → list

```python
lst = list(s)
```

Strings are immutable.
If you try swapping directly → you’re dead.

---

### 2. Two pointers

```python
i = 0
j = len(s) - 1
```

---

### 3. Traverse inward

```python
while i < j:
```

---

### 4. Skip non-vowels

```python
if lst[i] not in vowels:
    i += 1
```

```python
elif lst[j] not in vowels:
    j -= 1
```

---

### 5. Swap vowels

```python
elif lst[i] in vowels and lst[j] in vowels:
    lst[i], lst[j] = lst[j], lst[i]
```

Then move both:

```python
i += 1
j -= 1
```

---

### 6. Convert back to string

```python
return "".join(lst)
```

---

## 🔥 Dry Run

Input:

```python
"hello"
```

Process:

```
i → h ❌ → move
i → e ✔

j → o ✔

swap → holle
```

---

## 🚨 Brutal Feedback (Read This Carefully)

Your code **works**, but it’s not clean.

### ❌ Problem 1: List for vowels

```python
vowels = ["A", "E", ...]
```

👉 This is **slow lookup (O(n))**
👉 You’re checking membership every iteration

### ✅ Fix:

```python
vowels = set("aeiouAEIOU")
```

Now lookup is **O(1)**

---

### ❌ Problem 2: Redundant condition

```python
elif lst[i] in vowels and lst[j] in vowels:
```

This is unnecessary.

Why?

Because you already filtered:

* `if not vowel` → skip
* `elif not vowel` → skip

So by the time you reach `else`, both are vowels.

---

### ✅ Clean Version (What interviewer expects)

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        lst = list(s)

        i, j = 0, len(s) - 1

        while i < j:
            if lst[i] not in vowels:
                i += 1
            elif lst[j] not in vowels:
                j -= 1
            else:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1

        return "".join(lst)
```

---

## ⏱ Complexity

| Metric | Value                             |
| ------ | --------------------------------- |
| Time   | O(n)                              |
| Space  | O(n) (because of list conversion) |

---

## 🧠 Pattern Recognition

This is **Two Pointer Filtering + Swap**

Use this when:

* You selectively reverse elements
* You don’t care about non-target elements
* You want in-place logic

---

## 🎯 Key Takeaway

> Skip → Find → Swap → Repeat

If you’re writing extra conditions, you’re probably doing it wrong.

---

## 🚀 Upgrade Thinking

If you want to level up:

* Try solving **without converting to list** (harder)
* Try doing this for:

  * only digits
  * only uppercase
  * custom condition

That’s how you actually master patterns—not by copying.

---

If you want next level:
I can turn this into your **365-day infographic post** (that actually gets traction).
