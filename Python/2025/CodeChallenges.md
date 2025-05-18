## Python Coding Challenges Problems

### 1. Two-Sum with Sorted Input (Two-Pointer)

```python
def two_sum_sorted(nums, target):
    """
    Given a sorted list `nums` and integer `target`,
    return 1-based indices (i, j) such that nums[i-1] + nums[j-1] == target.
    """
    left, right = 0, len(nums) - 1
    while left < right:
        s = nums[left] + nums[right]
        if s == target:
            return (left + 1, right + 1)
        if s < target:
            left += 1
        else:
            right -= 1
    return None  # if no solution (per problem, won't happen)

# Example
print(two_sum_sorted([2, 7, 11, 15], 9))  # (1, 2)
```

---

### 2. Longest Substring Without Repeating Characters (Sliding Window)

```python
def length_of_longest_substring(s):
    """
    Return the length of the longest substring without repeating characters.
    """
    last_seen = {}
    start = max_len = 0

    for i, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= start:
            start = last_seen[ch] + 1
        last_seen[ch] = i
        max_len = max(max_len, i - start + 1)

    return max_len

# Example
print(length_of_longest_substring("abcabcbb"))  # 3
```

---

### 3. Merge K Sorted Lists (Heap + ListNode)

```python
import heapq

class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt
    def __lt__(self, other):
        return self.val < other.val

def merge_k_lists(lists):
    """
    lists: List[ListNode]
    Return the head of one merged sorted linked list.
    """
    heap = []
    for node in lists:
        if node:
            heapq.heappush(heap, node)

    dummy = tail = ListNode(0)
    while heap:
        node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next
        if node.next:
            heapq.heappush(heap, node.next)

    return dummy.next

# Helper to convert Python list to ListNode chain, and back for testing
def to_listnode(arr):
    dummy = cur = ListNode(0)
    for v in arr:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def from_listnode(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out

# Example
lists = [to_listnode([1,4,5]), to_listnode([1,3,4]), to_listnode([2,6])]
res = merge_k_lists(lists)
print(from_listnode(res))  # [1,1,2,3,4,4,5,6]
```

---

### 4. Word Ladder (BFS on Implicit Graph)

```python
from collections import deque

def ladder_length(beginWord, endWord, wordList):
    """
    Return the length of shortest transformation from beginWord to endWord.
    """
    word_set = set(wordList)
    if endWord not in word_set:
        return 0

    queue = deque([(beginWord, 1)])
    L = len(beginWord)

    while queue:
        word, steps = queue.popleft()
        if word == endWord:
            return steps
        for i in range(L):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                nxt = word[:i] + c + word[i+1:]
                if nxt in word_set:
                    word_set.remove(nxt)
                    queue.append((nxt, steps + 1))
    return 0

# Example
print(ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"]))  # 5
```

---

### 5. LRU Cache (OrderedDict)

```python
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key):
        if key not in self.cache:
            return -1
        # move key to end as most recently used
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            # update and mark as recently used
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            # pop oldest
            self.cache.popitem(last=False)

# Example
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1))   # 1
cache.put(3, 3)       # evicts key 2
print(cache.get(2))   # -1
```

---

### 6. Decode Ways (Dynamic Programming)

```python
def num_decodings(s):
    """
    Given numeric string s, return number of ways to decode.
    """
    if not s or s[0] == '0':
        return 0

    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # empty string
    dp[1] = 1  # first char guaranteed non-zero here

    for i in range(2, n + 1):
        # single digit
        if s[i-1] != '0':
            dp[i] += dp[i-1]
        # two-digit
        two = int(s[i-2:i])
        if 10 <= two <= 26:
            dp[i] += dp[i-2]
    return dp[n]

# Example
print(num_decodings("226"))  # 3
```

---

### 7. Serialize and Deserialize Binary Tree (Preorder + “null” Markers)

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    """Encodes a tree to a single string."""
    vals = []

    def dfs(node):
        if node is None:
            vals.append('null')
            return
        vals.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ','.join(vals)

def deserialize(data):
    """Decodes your encoded data to tree."""
    vals = data.split(',')
    idx = 0

    def dfs():
        nonlocal idx
        if vals[idx] == 'null':
            idx += 1
            return None
        node = TreeNode(int(vals[idx]))
        idx += 1
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()

# Example
#   1
#  / \
# 2   3
#    / \
#   4   5
root = TreeNode(1,
       TreeNode(2),
       TreeNode(3, TreeNode(4), TreeNode(5)))
data = serialize(root)
print(data)                    # "1,2,null,null,3,4,null,null,5,null,null"
restored = deserialize(data)
print(serialize(restored))     # same as data
```

---

### 8. Reverse a Linked List

```python
class ListNode:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.next = nxt

def reverseList(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

---

### 9. Valid Parentheses

```python
def isValid(s: str) -> bool:
    stack = []
    mapping = {')':'(', ']':'[', '}':'{'}
    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else '#'
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack

# Examples
print(isValid("({[]})"))  # True
print(isValid("([)]"))    # False
```

---

### 10. Merge Two Sorted Arrays (In-Place)

```python
def merge(A: list[int], m: int, B: list[int], n: int) -> None:
    i, j, k = m - 1, n - 1, m + n - 1
    while j >= 0:
        if i >= 0 and A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1

# Example
A = [1,3,5,0,0,0]; m=3
B = [2,4,6];       n=3
merge(A, m, B, n)
print(A)  # [1,2,3,4,5,6]
```

---

### 11. Number of Islands

```python
def numIslands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    m, n = len(grid), len(grid[0])

    def dfs(i: int, j: int):
        if i<0 or i>=m or j<0 or j>=n or grid[i][j] != '1':
            return
        grid[i][j] = '0'
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            dfs(i+di, j+dj)

    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                count += 1
                dfs(i, j)
    return count

# Example
grid = [
  ["1","1","0","0"],
  ["1","1","0","0"],
  ["0","0","1","0"],
  ["0","0","0","1"]
]
print(numIslands(grid))  # 3
```

---

### 12. Course Schedule (Detect Cycle / Topo Sort)

```python
from collections import defaultdict, deque

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = defaultdict(list)
    indeg = [0] * numCourses
    for a, b in prerequisites:  # b → a
        graph[b].append(a)
        indeg[a] += 1

    q = deque(i for i in range(numCourses) if indeg[i] == 0)
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in graph[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == numCourses

# Example
print(canFinish(2, [[1,0]]))       # True
print(canFinish(2, [[1,0],[0,1]])) # False
```

---

### 13. Product of Array Except Self

```python
def productExceptSelf(nums: list[int]) -> list[int]:
    n = len(nums)
    res = [1] * n
    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n-1, -1, -1):
        res[i] *= right
        right *= nums[i]
    return res

# Example
print(productExceptSelf([1,2,3,4]))  # [24,12,8,6]
```

---

### 14. Max Sliding Window

```python
from collections import deque

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    dq = deque()  # stores indices, window in decreasing order
    res = []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] < x:
            dq.pop()
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

# Example
print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
```

---

### 15. Find Median from Data Stream

```python
import heapq

class MedianFinder:
    def __init__(self):
        self.small = []  # max-heap via negatives
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # always push onto small first
        heapq.heappush(self.small, -num)
        # balance roots
        if self.small and self.large and -self.small[0] > self.large[0]:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        # rebalance sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        if len(self.large) > len(self.small) + 1:
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return (-self.small[0] + self.large[0]) / 2.0

# Example
mf = MedianFinder()
for x in [5,2,3,4,1]:
    mf.addNum(x)
    print(mf.findMedian())
```

---

### 16. Word Search II (Trie + DFS)

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

def findWords(board: list[list[str]], words: list[str]) -> list[str]:
    # Build trie
    root = TrieNode()
    for w in words:
        node = root
        for ch in w:
            node = node.children.setdefault(ch, TrieNode())
        node.word = w

    m, n = len(board), len(board[0])
    res = []

    def dfs(i: int, j: int, node: TrieNode):
        ch = board[i][j]
        if ch not in node.children:
            return
        nxt = node.children[ch]
        if nxt.word:
            res.append(nxt.word)
            nxt.word = None  # prevent duplicates

        board[i][j] = '#'
        for di, dj in [(1,0),(-1,0),(0,1),(0,-1)]:
            ni, nj = i+di, j+dj
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                dfs(ni, nj, nxt)
        board[i][j] = ch

        # optional: prune leaf
        if not nxt.children:
            node.children.pop(ch)

    for i in range(m):
        for j in range(n):
            dfs(i, j, root)
    return res

# Example
board = [
  ["o","a","a","n"],
  ["e","t","a","e"],
  ["i","h","k","r"],
  ["i","f","l","v"]
]
words = ["oath","pea","eat","rain"]
print(findWords(board, words))  # ['oath','eat']
```

---

### 17. Skyline Problem (Sweep Line + Heap)

```python
import heapq

def getSkyline(buildings: list[list[int]]) -> list[list[int]]:
    # Create events: (x, -h) for start, (x, h) for end
    events = []
    for L, R, H in buildings:
        events.append((L, -H, R))
        events.append((R, 0, 0))
    # Sort by x, then by height
    events.sort(key=lambda x: (x[0], x[1]))

    res = []
    # heap: (−height, end_x)
    heap = [(0, float('inf'))]
    prev_max = 0

    for x, negH, R in events:
        # If start of a building, add to heap
        if negH < 0:
            heapq.heappush(heap, (negH, R))
        # Remove ended buildings
        while heap and heap[0][1] <= x:
            heapq.heappop(heap)
        curr_max = -heap[0][0]
        if curr_max != prev_max:
            res.append([x, curr_max])
            prev_max = curr_max

    return res

# Example
buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(getSkyline(buildings))
# [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
```

---

### 18. Shortest Path with K Stops (BFS + Level-Order)

```python
from collections import defaultdict, deque
import math

def findCheapestPrice(n: int, flights: list[list[int]], src: int, dst: int, K: int) -> int:
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    dist = [math.inf] * n
    dist[src] = 0
    q = deque([src])
    stops = 0

    while q and stops <= K:
        size = len(q)
        tmp = dist.copy()
        for _ in range(size):
            u = q.popleft()
            for v, w in graph[u]:
                if dist[u] + w < tmp[v]:
                    tmp[v] = dist[u] + w
                    q.append(v)
        dist = tmp
        stops += 1

    return dist[dst] if dist[dst] != math.inf else -1

# Example
print(findCheapestPrice(
    4, [[0,1,100],[1,2,100],[2,3,100],[0,3,500]], 0, 3, 1
))  # 500
```

---

### 19. Regular Expression Matching (DP)

```python
def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    dp = [[False]*(n+1) for _ in range(m+1)]
    dp[0][0] = True

    # Handle patterns like a* or a*b* at the start
    for j in range(2, n+1):
        if p[j-1] == '*':
            dp[0][j] = dp[0][j-2]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if p[j-1] == s[i-1] or p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                # Zero occurrences of p[j-2]
                dp[i][j] = dp[i][j-2]
                # One or more, if preceding matches
                if p[j-2] == s[i-1] or p[j-2] == '.':
                    dp[i][j] |= dp[i-1][j]
    return dp[m][n]

# Examples
print(isMatch("aab", "c*a*b"))  # True
print(isMatch("mississippi", "mis*is*p*."))  # False
```
