from binary_tree import BinaryTree
from list_node import ListNode

# Time Complexity = O(n)
def two_sum(nums: list[int], target: int) -> list[int]:
    memory = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in memory:
            return [memory[complement], i]
        else:
            memory[num] = i


def valid_parentheses(s: str) -> bool:
    stack: list[str] = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if top != mapping[char]:
                return False

        else:
            stack.append(char)

    return not stack


def longest_repeat_substring(s: str) -> int:
    left = 0
    max_len = 0
    seen_chars = {}

    for i, char in enumerate(s):
        right = i
        if char in seen_chars:
            rm = seen_chars[char] + 1
            left = left if rm < left else rm
        seen_chars[char] = i
        current_len = right - left + 1
        max_len = max(max_len, current_len)
    return max_len


# O(N)
def is_palindrome(s: str) -> bool:
    s = [c for c in s.lower() if c.isalnum()]
    left = 0
    right = len(s) - 1
    while (left < right):
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True


# O(N⋅KlogK)
def group_angrams(strs: list[str]) -> list[list[str]]:
    group: dict[str, list[str]] = {}
    for s in strs:
        # sorted -> O(KlogK)
        key = "".join(sorted(s))
        if key in group:
            group[key].append(s)
        else:
            group[key] = [s]
    return list(group.values())


def invert_tree(root: BinaryTree) -> BinaryTree:
    if not root:
        return None
    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)
    return root


def three_sum(nums: list[int]) -> list[list[int]]:
    nums.sort()
    rs = []
    target = 0
    n = len(nums)

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                tri = [nums[i], nums[left], nums[right]]
                rs.append(tri)
                while left < right and nums[left] == tri[1]:
                    left += 1
                while left < right and nums[right] == tri[2]:
                    right -= 1
    return rs

# O(N)
def climb_stairs(n: int, memo: dict = None) -> int:
    if memo is None:
        return climb_stairs(n, {})
    else:
        if n <= 2:
            return n
        else:
            if n in memo:
                return memo[n]
            else:
                rs = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
                memo[n] = rs
                return rs
        

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

