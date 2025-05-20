## Coding Problems Asked in Infosys Interview

### 1. With given input build expected output using Python?
- Given: str1 = "abc", str2 = "pqrst"
- Expected: str3 = "apbqcr s t"

**Solution:**
```python
class StringWeaver:
    def __init__(self, str1, str2):
        self.str1 = str1
        self.str2 = str2
        
    def weave(self):
        n1, n2 = len(self.str1), len(self.str2)
        min_len = min(n1, n2)
        
        interleaved_parts = []
        for i in range(min_len):
            interleaved_parts.append(str1[i])
            interleaved_parts.append(str2[i])
        
        interleaved = ''.join(interleaved_parts)
        
        if n1 > n2:
            leftover = str1[min_len:]
        else:
            leftover = str2[min_len:]
            
        if leftover:
            return interleaved + ' '+ ' '.join(leftover)
        else:
            return interleaved
        
        
if __name__ == "__main__":
    str1 = "abc"
    str2 = "pqrst"
    weaver = StringWeaver(str1, str2)
    result = weaver.weave()
    print(result)
```

### 2. With given input build expected output using Python?
- Given: l1 = ['a', 'k', 'a', 'b', 'j', 'k', 'k']
- Expected: d1 = {'a': 2, 'k': 3, 'b': 1, 'j': 1}

**Solution:**
```python
def count_occurance(l1):
    d1 = {}
    for i in l1:
        d1[i] = d1.get(i, 0) + 1
    return d1
```
