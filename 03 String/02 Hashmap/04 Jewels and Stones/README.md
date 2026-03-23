# 💎 Jewels and Stones — HashMap Lookup

![Visualization](https://github.com/mdzaheerjk/DSA-Patterns/blob/main/03%20String/src/jewels%20and%20stones.png)

---

## 🧠 Explanation of Your Code

```python id="p2k9r8"
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        counter=0
        hash_map={}
        for i in jewels:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1
        for j in stones:
            if j in hash_map:
                counter+=hash_map[j]

        return counter
```

---

## ⚡ Core Idea

👉 Count how many characters in `stones` are present in `jewels`

* `jewels` → allowed/valuable characters
* `stones` → what you have
* Count how many stones are jewels

---

## 🔁 Step-by-Step Logic

### 1. Store jewels in a map

```python id="3avj0r"
hash_map = {}
for i in jewels:
    if i in hash_map:
        hash_map[i] += 1
    else:
        hash_map[i] = 1
```

👉 Marks which characters are jewels

---

### 2. Traverse stones

```python id="9m8s4g"
for j in stones:
```

---

### 3. Count matches

```python id="z5g2xq"
if j in hash_map:
    counter += hash_map[j]
```

👉 If stone is a jewel → increase count

---

### 4. Return result

```python id="o6x9lm"
return counter
```

---

## 🧩 Example Walkthrough

### Input

```python id="k7w1yt"
jewels = "aA"
stones = "aAAbbbb"
```

### Map

```text id="v7p2qf"
{'a':1, 'A':1}
```

### Count

```text id="c8n4zd"
a → +1  
A → +1  
A → +1  
```

👉 Total = **3**

---

## 🚨 Brutal Feedback

Your code works — but it’s **overkill**.

### ❌ Problem

```python id="m9x2vd"
hash_map[i] += 1
```

👉 You don’t need frequency for jewels
👉 Jewels are just a **set of allowed chars**

---

## ✅ Better Approach

```python id="2c7kq9"
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        count = 0

        for s in stones:
            if s in jewel_set:
                count += 1

        return count
```

---

### Why this is better:

* Cleaner
* Faster lookup (O(1))
* No unnecessary counting

---

## ⏱ Complexity

| Metric | Value    |
| ------ | -------- |
| Time   | O(n + m) |
| Space  | O(1)     |

---

## 🎯 Key Insight

> You only need **membership check**, not frequency tracking

---

## 🧠 One-line Summary

> Put jewels in a set and count how many stones belong to it.
