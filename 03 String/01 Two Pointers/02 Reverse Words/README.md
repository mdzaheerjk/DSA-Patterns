# 🔁 Reverse Words in a String — Two Pointer Swap

![Visualization](https://github.com/mdzaheerjk/DSA-Patterns/blob/main/03%20String/src/reverse%20words.png)

---

## 🧠 Explanation of Your Code

```python
class Solution(object):
    def reverseWords(self, s):
        s=s.split()
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
        return " ".join(s)
```

---

## ⚡ Core Idea

* Break string into words
* Reverse the order of words
* Join them back with single space

---

## 🔁 Step-by-Step Logic

### 1. Split string into words

```python
s = s.split()
```

👉 Important:

* Removes **extra spaces**
* Handles:

  * leading spaces
  * trailing spaces
  * multiple spaces

Example:

```python
"  hello   world  " → ["hello", "world"]
```

---

### 2. Initialize two pointers

```python
i = 0
j = len(s) - 1
```

* `i` → start
* `j` → end

---

### 3. Reverse the list (in-place)

```python
while i < j:
    s[i], s[j] = s[j], s[i]
    i += 1
    j -= 1
```

👉 Swap words from both ends
👉 Move inward

---

### 4. Join back into string

```python
return " ".join(s)
```

👉 Ensures:

* Only **one space** between words
* No extra spaces at start/end

---

## 🧩 Example Walkthrough

### Input

```python
s = "the sky is blue"
```

### Step 1: Split

```python
["the", "sky", "is", "blue"]
```

### Step 2–3: Reverse

```python
["blue", "is", "sky", "the"]
```

### Step 4: Join

```python
"blue is sky the"
```

---

## 🎯 Key Idea

> Reverse **words**, not characters

* You’re not touching letters inside words
* Only changing **word positions**

---

## 🧠 One-line Summary

> Split → reverse list → join back with single space
