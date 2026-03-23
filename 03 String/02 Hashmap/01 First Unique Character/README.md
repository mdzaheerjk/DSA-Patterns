# 🔤 First Unique Character in a String — HashMap Approach

![Visualization](https://github.com/mdzaheerjk/DSA-Patterns/blob/main/03%20String/src/first%20unique%20character.png)

---

## 🧠 Explanation of Your Code

```python
class Solution(object):
    def firstUniqChar(self, s):
        hash_map={}
        for i in s:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for i in range(len(s)):
            if hash_map[s[i]]==1:
                return i
        return -1
```

---

## ⚡ Core Idea

* Count how many times each character appears
* Return the **first character with frequency = 1**

👉 This is a **two-pass approach**
👉 First pass = count
👉 Second pass = find answer ([AlgoMonster][1])

---

## 🔁 Step-by-Step Logic

### 1. Build frequency map

```python
hash_map = {}
for i in s:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1
```

👉 Stores frequency of each character

Example:

```python
s = "leetcode"

hash_map = {
    'l':1,
    'e':3,
    't':1,
    'c':1,
    'o':1,
    'd':1
}
```

---

### 2. Traverse string again

```python
for i in range(len(s)):
```

👉 Important:
You loop again because **order matters**

---

### 3. Check first unique character

```python
if hash_map[s[i]] == 1:
    return i
```

👉 First character with count = 1 → return index

---

### 4. If no unique character

```python
return -1
```

👉 All characters are repeating

---

## 🧩 Example Walkthrough

### Input

```python
s = "leetcode"
```

### Step 1: Frequency map

```
l:1, e:3, t:1, c:1, o:1, d:1
```

### Step 2: Scan

```
index 0 → l → count = 1 ✔ → return 0
```

---

### Another Example

```python
s = "aabb"
```

```
a:2, b:2
```

👉 No unique → return -1

---

## 🎯 Key Insight

> You **must count first**, then decide

Why?

Because:

* At index 0, you **don’t know yet** if it repeats later
* Example: `"aab"` → first `a` looks unique initially, but isn’t ([AlgoMonster][1])

---

## ⏱ Complexity

| Metric | Value                      |
| ------ | -------------------------- |
| Time   | O(n)                       |
| Space  | O(1) (only 26 letters max) |

---

## 🧠 One-line Summary

> Count all characters, then return the first index whose count is 1.

[1]: https://algo.monster/liteproblems/387?utm_source=chatgpt.com "387. First Unique Character in a String - In-Depth Explanation"
