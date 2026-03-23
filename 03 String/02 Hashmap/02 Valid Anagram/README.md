# 🔤 Valid Anagram — HashMap Frequency Matching

![Visualization](https://github.com/mdzaheerjk/DSA-Patterns/blob/main/03%20String/src/valid%20anagram.png)

---

## 🧠 Explanation of Your Code

```python
class Solution(object):
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
        hash_map={}
        for i in s:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for j in t:
            if j in hash_map:
                hash_map[j]-=1
            else:
                hash_map[j]=1
        for key,values in hash_map.items():
            if values!=0:
                return False
        return True
```

---

## ⚡ Core Idea

Two strings are anagrams if:

> They contain the **same characters with the same frequency**

---

## 🔁 Step-by-Step Logic

### 1. Length check

```python
if len(s) != len(t):
    return False
```

👉 If lengths differ → impossible to be anagram

---

### 2. Count characters in `s`

```python
hash_map = {}
for i in s:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1
```

👉 Build frequency map

Example:

```python
s = "anagram"
→ {a:3, n:1, g:1, r:1, m:1}
```

---

### 3. Subtract using `t`

```python
for j in t:
    if j in hash_map:
        hash_map[j] -= 1
    else:
        hash_map[j] = 1
```

👉 Reduce counts based on `t`

---

### 4. Check if all counts are zero

```python
for key, values in hash_map.items():
    if values != 0:
        return False
```

👉 If any value ≠ 0 → not anagram

---

### 5. Final result

```python
return True
```

---

## 🧩 Example Walkthrough

### Input

```python
s = "anagram"
t = "nagaram"
```

### After Step 2

```
{a:3, n:1, g:1, r:1, m:1}
```

### After Step 3

```
{a:0, n:0, g:0, r:0, m:0}
```

👉 All zero → True

---

### Failure Case

```python
s = "rat"
t = "car"
```

```
{r:0, a:0, t:1, c:-1}
```

👉 Not all zero → False

---

## 🎯 Key Insight

* You’re **balancing counts**
* Add from `s`, subtract from `t`
* Final map must be **all zeros**

---

## ⚠️ Small Issue in Your Code

```python
else:
    hash_map[j] = 1
```

👉 This is logically wrong

If char not in map → it should instantly fail
You’re silently adding it instead

---

## ✅ Correct Version

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c not in count:
                return False
            count[c] -= 1

        return all(v == 0 for v in count.values())
```

---

## ⏱ Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

---

## 🧠 One-line Summary

> Count characters in `s`, subtract using `t`, and ensure everything becomes zero.
