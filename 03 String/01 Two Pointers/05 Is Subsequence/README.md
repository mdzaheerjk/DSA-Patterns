# 🔗 Is Subsequence — Two Pointer Approach

![Visualization](https://github.com/mdzaheerjk/DSA-Patterns/blob/main/03%20String/src/is%20subsequence.png)

---

## 🧠 Explanation of Your Code

```python
class Solution(object):
    def isSubsequence(self, s, t):
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i==len(s)
```

---

## ⚡ Core Idea

You are checking whether string `s` appears inside `t` **in the same order**, not necessarily continuously.

* `i` → pointer for `s` (what you want to match)
* `j` → pointer for `t` (where you search)

---

## 🔁 How It Works

### 1. Initialize pointers

```python
i = 0
j = 0
```

---

### 2. Traverse both strings

```python
while i < len(s) and j < len(t):
```

* Continue until:

  * All characters of `s` are matched
  * OR `t` is fully scanned

---

### 3. Compare characters

```python
if s[i] == t[j]:
    i += 1
```

* If match → move `i` forward
* Meaning: you found current character of `s` in `t`

---

### 4. Always move `j`

```python
j += 1
```

* Because you are scanning through `t` regardless

---

## 🎯 Key Idea

* Skip unwanted characters in `t`
* Only move in `s` when a match occurs
* Maintain order — that’s the only rule

---

## 🧩 Example Walkthrough

### Input

```python
s = "abc"
t = "ahbgdc"
```

### Execution

```
i → a, j → a → match → i++
i → b, j → h → skip
i → b, j → b → match → i++
i → c, j → g → skip
i → c, j → d → skip
i → c, j → c → match → i++
```

Now:

```python
i == len(s) → True
```

---

## ❌ Failure Case

```python
s = "axc"
t = "ahbgdc"
```

* `a` matches
* `x` not found

👉 `i` doesn’t reach end → False

---

## ✅ Final Condition

```python
return i == len(s)
```

* If all characters of `s` matched → True
* Else → False

---

## 🧠 One-line Summary

> Scan `t` and try to consume `s` in order. If fully consumed → subsequence.
