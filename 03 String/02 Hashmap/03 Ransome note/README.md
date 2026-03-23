# 🧾 Ransom Note — HashMap Frequency Matching

![Visualization](https://github.com/mdzaheerjk/DSA-Patterns/blob/main/03%20String/src/Ransome%20Note.png)

---

## 🧠 Explanation of Your Code

```python
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hash_map={}
        for i in ransomNote:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for j in magazine:
            if j in hash_map:
                hash_map[j]-=1
                if hash_map[j]==0:
                    del hash_map[j]
        return len(hash_map)==0
```

---

## ⚡ Core Idea

👉 You need to check if `magazine` has enough characters to build `ransomNote`

* Count required characters from `ransomNote`
* Try to satisfy them using `magazine`
* If all requirements met → True

---

## 🔁 Step-by-Step Logic

### 1. Count required characters

```python
hash_map = {}
for i in ransomNote:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1
```

👉 This stores how many times each character is needed

Example:

```python
ransomNote = "aa"
→ {'a': 2}
```

---

### 2. Traverse magazine

```python
for j in magazine:
```

👉 Try to fulfill requirements

---

### 3. Reduce counts when match found

```python
if j in hash_map:
    hash_map[j] -= 1
```

👉 One required character satisfied

---

### 4. Remove fulfilled characters

```python
if hash_map[j] == 0:
    del hash_map[j]
```

👉 Clean map when requirement becomes zero

---

### 5. Final check

```python
return len(hash_map) == 0
```

👉 If map is empty → all requirements met → True
👉 Else → missing characters → False

---

## 🧩 Example Walkthrough

### Input

```python
ransomNote = "aa"
magazine = "aab"
```

### Step 1

```text
{'a': 2}
```

### Step 2–3

```text
'a' → {'a':1}
'a' → {'a':0} → removed
```

### Final

```text
{}
→ True
```

---

### Failure Case

```python
ransomNote = "aa"
magazine = "ab"
```

```text
{'a':2}
→ 'a' → {'a':1}
→ 'b' → no effect
```

👉 Map not empty → False

---

## 🎯 Key Insight

> You are not matching strings — you are matching **frequencies**

* `ransomNote` = requirement
* `magazine` = supply

---

## ⏱ Complexity

| Metric | Value    |
| ------ | -------- |
| Time   | O(n + m) |
| Space  | O(1)     |

---

## 🧠 One-line Summary

> Count required characters, subtract using magazine, and check if nothing is left.
