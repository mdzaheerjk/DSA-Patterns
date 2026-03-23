# 🔗 Isomorphic Strings — Bidirectional HashMap

![Visualization](https://github.com/mdzaheerjk/DSA-Patterns/blob/main/03%20String/src/isomorphic%20string.png)

---

## 🧠 Explanation of Your Code

```python id="l9r2xk"
class Solution(object):
    def isIsomorphic(self, s, t):
        map1={}
        map2={}
        for i in range(len(s)):
            c1=s[i]
            c2=t[i]
            if c1 in map1:
                if map1[c1]!=c2:
                    return False
            else:
                map1[c1]=c2
            if c2 in map2:
                if map2[c2]!=c1:
                    return False
            else:
                map2[c2]=c1
        return True
```

---

## ⚡ Core Idea

Two strings are **isomorphic** if:

> Each character in `s` maps to exactly one character in `t`
> AND no two characters map to the same character

👉 One-to-one mapping (bijection)

---

## 🔁 Step-by-Step Logic

### 1. Use two hash maps

```python id="y0m3bz"
map1 → s → t
map2 → t → s
```

👉 Why two maps?

* Prevent conflicts in both directions
* Ensures **unique mapping**

---

### 2. Traverse both strings

```python id="3t6zlp"
for i in range(len(s)):
```

---

### 3. Extract characters

```python id="h5o2v1"
c1 = s[i]
c2 = t[i]
```

---

### 4. Check mapping s → t

```python id="9z1xqe"
if c1 in map1:
    if map1[c1] != c2:
        return False
else:
    map1[c1] = c2
```

👉 If already mapped → must match
👉 Else → create mapping

---

### 5. Check reverse mapping t → s

```python id="p4k2dn"
if c2 in map2:
    if map2[c2] != c1:
        return False
else:
    map2[c2] = c1
```

👉 Prevents multiple characters mapping to same value

---

### 6. If no conflicts

```python id="1q7xnm"
return True
```

---

## 🧩 Example Walkthrough

### Input

```python id="u6k9f3"
s = "egg"
t = "add"
```

### Mapping

```text id="j9p2vh"
e → a
g → d
g → d ✔ consistent
```

👉 Valid → True

---

### Failure Case

```python id="6p2xot"
s = "foo"
t = "bar"
```

```text id="2n4kxm"
f → b
o → a
o → r ❌ conflict
```

👉 Return False

---

## 🎯 Key Insight

> One-direction mapping is NOT enough

Example:

```text id="c0y8nt"
s = "ab"
t = "aa"
```

* a → a
* b → a ❌ (two map to same)

👉 Only `map1` would miss this
👉 `map2` catches it

---

## ⏱ Complexity

| Metric | Value |
| ------ | ----- |
| Time   | O(n)  |
| Space  | O(1)  |

---

## 🧠 One-line Summary

> Maintain two maps to ensure a strict one-to-one character mapping between both strings.
