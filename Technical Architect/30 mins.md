#### **Python Fundamentals**
- "What’s the difference between a list and a tuple in Python, and when would you use each?"

- "How do you manage memory in Python when working with large datasets?"


- "What are decorators, and how have you used them?"



#### **Architectural Design**
- "How would you design a Python-based system to handle millions of requests daily?"


- "What security risks should you watch for in Python applications, and how do you address them?"


- "Tell me about a time you improved the performance of a Python system."



#### **Problem-Solving (Coding)**
- **String Example**: "Write a function to check if a string is a palindrome."
- **Number Example**: "Given a list of integers, find two numbers that sum to a target value."


#### **Solve Sample Problems**
- **Palindrome Check**:
  ```python
  def is_palindrome(s):
      return s == s[::-1]

  # Test it
  print(is_palindrome("radar"))  # True
  print(is_palindrome("python")) # False
  ```
- **Two Sum**:
  ```python
  def two_sum(nums, target):
      seen = {}
      for i, num in enumerate(nums):
          complement = target - num
          if complement in seen:
              return [seen[complement], i]
          seen[num] = i
      return None

  # Test it
  print(two_sum([3, 5, 7, 2], 9))  # [2, 3]
  ```

#### **Prepare for Quick Behavioral Questions**
- Be ready with a short example of a tough project or a time you met a tight deadline.

- Example: "Describe a situation where you made a key architectural choice under pressure."
