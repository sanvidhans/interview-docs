## Most Asked Coding Question

### 1. Write a Python function that will reverse a string without using the slicing operator or reverse() function?
```python
def reverse_string(data):
    result = ""
    for char in data:
        result = char + result
    return result

reverse_string(data = 'python')
```
**Output**
```
nohtyp
```

### 2. Write a program to delete all consonants from a given string. 'Python and Data Science'
```python
def del_consonants(data):
    vowels = 'aeiouAEIOU'
    result = ''.join([char for char in data if not char.isalpha() or char in vowels])
    return result

del_consonants(data = 'Python and Data Science')
```

### 3. Write a program that will find the sum of all the prime numbers between 1 and N
```python
def is_prime(number):
    for z in range(2, number):
        if(number%z == 0):
            reutrn False
    return True

def add(number):
    total = 0
    for z in range(2, number+1):
        if(is_prime(z)):
            total = total + z
    return total

add(number = 10)
```
