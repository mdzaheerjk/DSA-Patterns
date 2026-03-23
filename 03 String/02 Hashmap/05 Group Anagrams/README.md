# 🔗 Group Anagrams — HashMap + Sorted Key

![Visualization](https://github.com/mdzaheerjk/DSA-Patterns/blob/main/03%20String/src/group%20anagrams.png)

---

## 🧠 Explanation of Your Code

```python
class Solution(object):
    def groupAnagrams(self, strs):
        hash_map={}
        for i in strs:
            sorted_i="".join(sorted(i))
            if sorted_i in hash_map:
                hash_map[sorted_i].append(i)
            else:
                hash_map[sorted_i]=[i]
        return hash_map.values()
```

---

## ⚡ Core Idea

👉 Group words that have **same characters**

Key trick:

> If two strings are anagrams → their **sorted form is identical** ([neetcode.io][1])

Example:

```text
"eat" → "aet"
"tea" → "aet"
"ate" → "aet"
```

---

## 🔁 Step-by-Step Logic

### 1. Initialize hashmap

```python
hash_map = {}
```

👉 Stores:

```
key   → sorted string  
value → list of anagrams
```

---

### 2. Process each word

```python
for i in strs:
```

---

### 3. Create key using sorting

```python
sorted_i = "".join(sorted(i))
```

👉 Converts:

```
"tea" → ['a','e','t'] → "aet"
```

👉 Same key for all anagrams ([GeeksforGeeks][2])

---

### 4. Group words

```python
if sorted_i in hash_map:
    hash_map[sorted_i].append(i)
else:
    hash_map[sorted_i] = [i]
```

👉 Same key → same group

---

### 5. Return result

```python
return hash_map.values()
```

👉 Returns all grouped lists

---

## 🧩 Example Walkthrough

### Input

```python
strs = ["eat","tea","tan","ate","nat","bat"]
```

### Process

```
"eat" → "aet" → ["eat"]
"tea" → "aet" → ["eat","tea"]
"tan" → "ant" → ["tan"]
"ate" → "aet" → ["eat","tea","ate"]
"nat" → "ant" → ["tan","nat"]
"bat" → "abt" → ["bat"]
```

---

### Final Output

```python
[
 ["eat","tea","ate"],
 ["tan","nat"],
 ["bat"]
]
```

---

## 🎯 Key Insight

> You’re not comparing strings — you’re **normalizing them**

* Sorting creates a **signature**
* Same signature → same group

---

## ⏱ Complexity

| Metric | Value          |
| ------ | -------------- |
| Time   | O(n * k log k) |
| Space  | O(n * k)       |

* `n` = number of strings
* `k` = max length of string

---

## 🚨 Brutal Feedback

### ❌ Minor Issue

```python
return hash_map.values()
```

👉 In Python 3, this returns a **view**, not a list

---

### ✅ Better Version

```python
return list(hash_map.values())
```

---

## 🧠 One-line Summary

> Sort each word, use it as a key, and group all matching words together.

[1]: https://neetcode.io/solutions/group-anagrams?utm_source=chatgpt.com "49. Group Anagrams - Solution & Explanation"
[2]: https://www.geeksforgeeks.org/dsa/given-a-sequence-of-words-print-all-anagrams-together/?utm_source=chatgpt.com "Group Anagrams Together"
