## Most Asked Questions

### 1. What is difference between a module and package?
- A module is just one Python file that has code, such as functions, classes, or variables.
- A package is a folder with multiple Python files (modules) and a special file called __init__.py. It helps organize many modules together.
- Example: Think of a module as a single book and a package as a bookshelf with many books.


### 2. Is python is a compiled language or an interpreted language?
- Python is an interpreted language. This means it runs your code line by line directly, without needing to turn it into separate file first(like compiled language do)
- Its like reading a recipe and cooking step-by-step, instead of preparing everything is advance.


### 3. What are the benefits of using Python language as a tool in the present scenario?
- It's easy to learn and write, so anyone can start quickly.
- It has lots of libraries (like tools in a toolbox) for things like data analysis, web development, or AI.
- It works for many tasks - from small scripts to big projects.
- There is a huge community to help you out with problems.

### 4. What are the global, protected and private attributes in Python?
- Global atributes: Variables made outside any function or class, usable anywhere in the file.
- Protected attributes: Start with one underscore like (like _name). Meant for use inside a class and its children, but not strict.
- Private attributes: Start with two underscores (like __name). Meant only for the class they're in - Python makes them harder to access from outside.


### 5. Is python case-sensitive?
- Yes, Python cases about uppercase and lowercase. For example, Name and name are two different things.

### 6. What is Pandas?
- Pandas is a Python library that makes working with data easy.
- It gives you tools like DataFrames (like tables) and Series (like lists and labels) to organize and analyze data.
- It is super popular for data science and number-crunching tasks.

### 7. How is Exceptional hanling done in Python?
- We use try-except blocks:
    - Put risky code in try.
    - If something goes wrong (an error), except catches it and handle it.
- Example:
```python
try:
    print(5/0) # This will fail
except:
    print("Oops, can't divide by zero!")
```

### 8. Difference between for loop and while loop in python?
- For loop: Goes through a list or range one by one. Use it when you know how many times to repeat.
- While loop: Keeps running as long as a condition is true. Use it when you don't know how many loops you'll need.
- Example: for is like counting 1 to 10, while is like waiting until the rain stops.


### 9. Is Indentation Required in Python?
- Yes, Indentation is a must in Python!. It shows which lines belong together (like in look or functions).
- Other language use {} braces, but Python uses spaces or tabs.

### 10. What is the use of self in Python?
- Self is used in classes to point the object you're working with.
- It lets you use the object's own variables and functions inside the class.
- Example: If a car has a color, self.color means "this car's color"


### 11. How does Python manage memory? Explain the role of reference counting and garbage collection.
- Python handles memory automatically:
- Reference counting: Counts how many times an object used. If it hits zero (no one needs it), the memory is freed.
- Garbage Collection: Finds and cleans up objects that reference each other in a loop, so they don't stick around forever.


### 12. Does Python support multiple Inheritance?
- Yes, Python lets a class inherit from more than one parent class. This means it can mix features.

### 13. How is memory management done in Python?
- Python uses a memory manager to:
    - Store everything in a private heap (like a storage room).
    - Free up space with refereence counting (when something's not used) and garbase collection (for tricky leftovers)


### 14. How to delete file using python?
- Use the `os` module
```
import os
os.remove('file.txt')
```

### 15. Which sorting technique is used by sort() and sorted() functions of python?
- The Timsort, a fast and smart method that mixes merge sort and insertion sort. It works well for all kinds of data.

### 16. Difference between List and Tuple?
- List: Changeable (mutable), uses [], Example: [1,2,3]
- Tuple: Unchangeable (immutable), uses (), Example: (1, 2, 3)
- Use lists when you'll update things; use tuples when you won't.

### 17. What is slicing in Python?
- Slicing cuts out a piece of a list, string, or tuple using [start:stop:step].
- Example: my_list[1:4] grabs items from index 1 to 3

### 18. How is multithreading achieved in Python?
- Use the threading module to run multiple tasks at once.
- Example: One thread downloads a file while another plays music.
- Python's GIL can slow it down for heavy tasks, though.

### 19. Which is faster, Python list or Numpy Arrays?
- NumPy arrays are faster for math and big data because they are built in C and optimized.
- List are slower but more flexible for general use.


### 20. Explain Inheritance in Python?
- Inheritance lets one class copy features (methods and variables) from another class.
- Example: A Dog class can inherit from Animal to get things like eat()

### 21. How are classes created in Python?
- Use the class keyword
```python
class MyClass:
    def say_hi(self):
        print("Hi")
```

### 22. Write a program to produce the Fibonacci series in Python?
```python
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series

num_terms = 10
print(f"Fibonacci series with {num_terms} terms:")
print(fibonacci(num_terms))
```

### 23. What is the difference between shallow copy and deep copy in Python?
- Shallow Copy: It creates a new object, but copies references to the objects contained in the original object.
- Deep Copy: It creates a new object and recursively copies all objects found in the original, creating fully independent copies.
- Example: Shallow copy shares a suitcase's contents; deep copy makes a new suitcase.


### 24. What is the process of compilation and linking in Python?
- Compilation: The process of compilation in Python involves converting the source code written by the programmer into a form that can be executed by the Python interpreter.

- Linking: In Python, the process of linking is not as explicit and complex as in compiled languages like C or C++. However, it involves serveral steps related to the import and usage of modules and packages.


### 25. What is break, continue, and pass in Python?
- Break: The break statement immediately ends the loop and transfers control to the first statement following the loop's body.
- Continue: The continue statement ends the current iteration of the loop, skips the remaining code in this iteration, and proceeds with the next iteration of the loop.

- Pass: The pass keyword in Python is used to fill empty blocks of code. It acts as a placeholder, similar to an empty statement(a semicolon) in languages like Java, C++, and JavaScript.


### 26. What is PEP 8?
- PEP 8 is the Python enhancement Proposal that provides guidelines and best practices on how to write Python code. It is essentially the style guide for Python code, helping developers write code that is readable and consistent.


### 27. What is an Expression?
- An expressions is code that gives a value, like 2 + 3 or len("Hi")


### 28. What is == in Python?
- == checks if two things have the same value. Like: 5 == 5 is true

### 29. What is type conversion in Python?
- Type conversion in Python refers to the process of converting a value from one data type to another.

Here are some common type conversion functions:
- int(): Converts a value to an integer.
- float(): Converts a value to a float.
- str(): Converts a value to a string.
- list(): Converts a value to a list.
- tuple(): Converts a value to a tuple.
- set(): Converts a value to a set.
- dict(): Converts a sequence of key-value pairs into a dictionary.

### 30. Name some commonly used built-in modules in Python?

Some of the commonly used built-in modules are:
- os
- sys
- math
- random
- datetime
- JSON


### 31. What is the difference between range and xrange in functions

In Python, range() and xrange() functions are used to iterate a specific number of times in for loops. The range() function returns a list of numbers. The xrange() functions returns the generator object that can display only numbers by looping. 
It displays only a particular range on demand and thus, it is known as lazy evaluation.
The xrange() function is not found in Python 3. The range function works like xrange() in Python 2.



### 32. What is the zip() function?

In Python, zip() function return a zip object that maps multiple containers identical indexes. It accepts an iterable, transforms it into an iterator, and aggregates the elements depending on iterables passed. Furthermore, it returns an iterator of tuples.


### 33. What is Django Architecture?

Django is a high-level web framework built in Python that allows rapid development of maintainable and secure websites.

Its architecture consists of:
- Model: The back end where the data is managed and stored.
- Template: The frontend of the webpage.
- View: Function which accepts the web requests and delivers the web responses.


### 34. What is inheritance in Python?

Inheritance allows a class to get all members of another class. The members can be methods, attributes, or both. With reusability, inheritance streamlines an application's development and maintenance.

Python supports four types of inheritance:
- Single Inheritance
- Multiple Inheritance
- Multilevel Inheritance
- Hierachical Inheritance


### 35. Define *args and **kwargs in Python?

In Python, *args allows function to accept n number of positional arguments also knows as non-keyword arguments, and variable-length argument lists.
Whereas, **kwargs serves as a special syntax that allows us to pass a variable length of keyword arguments to the function.


### 36. Do runtime errors exists in Python?
Yes, runtime errors are found in Python. For example, when you are duck typiing and things appear like a duck, it is regarded as a duck, although it is merely a stamp or flag. In this case, the code has a runtime error. 


### 37. What is docstring in Python?

- Docstrings or documentation strings are multiline strings used to document a specific code segment. Docstrings usually come within triple quotes and should ideally describe what a function or method does. 
Docstrings are not comments, 


### 38. How can you capitalize the first letter of a string in Python?

You can use the capitalize() method to capitalize the first letter of a string. Howevcer, if a string already consists of a capital letter at the beginning, it wil return the original string.

### 39. What are generators in Python?

- Generators are most important python functions that return an iterable collection of items, one at a time, in an organized manner.

### 40. How to write comments in Python?

### 41. What is GIL?

- GIL or Global Interpreter Lock is a mutex, used to limit access to Python objects. 
- It synchronizes threads and prevents them from running at the same time.


### 42. Is Django better than Flask?
- Django is better suited for large, complex applications with many built in features, while Flask is better for small to medium projects requiring more flexibility and control; the choice depends on your specific needs and project requirements.


### 43. What is Flask? Explain its benefits?

Flask is a lightweight and flecible web framework for Python that provides the essential tools to build web applications, making it easy to get started and scale as needed.

- Simplicity and Minimalism
- Flexibility
- Modular and Extensible
- Wide Adoption and Community Support


### 44. What is PIP?

- PIP is an acronym for Python Installer Package which provides a seamless interface to install various Python modules. It is a commandline tool that can search for packages over the internet and install them without any user interaction.

### 45. What is the difference between Modulus Operator %, Division Operator /, and Floor Division Operators //?

- The modulus % operator returns the remainder of a division. For instnce, 5 % 2 would return 1.
- The division operator performs floating point division and returns a float.
For example, 5/2 would return 2.5
- The // floor division operator that performs division but rounds down the result to the nearest whole number. So 5/2 would return 2.



### 46. Why doesn't Python deallocate all memory upon exit?

- Whenever Python exits, especially those Python modules, which are having circular references to other objects or the objects that are referenced from the global namespaces, the memory is not always de-allocated or freed.
- It is not possible to de-allocate those portions of memory that are reserved by the C library.
- On exit, because of having its own efficient clean-up mechanism, Python will try to de-allocate every objects.

### 47. Why is a set known as unordered? Is it mutable or immutable? 

- A set is called  "unordered" because the items in a set don't have a specific order or sequence like a list does. 
- Sets in Python are mutable, which means you can add or remove items from a set after its created. However the items within the set(the elements) are themselves immutable, meaning they cannot be changed.

### 48. What is difference between DataFrames and Seriies?
 
- A series is one-dimensional array-like object in pandas that can hold any data type, while a DataFrame is a two-dimentional, table like structure with potentially heterogeneously-typed columns. You can think of DataFrame as a collection of Series objects that share the same index.

### 49. What does len() do?

- The len() function is used to determine the length of various data types such as strings, lists, arrays, etc.
- Example:
```python
stg = "PYTHON"
length = len(stg)
print(length)
```
- Output: 6
