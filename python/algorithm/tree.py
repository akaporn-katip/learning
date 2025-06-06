class TreeNode:
    def __init__(self, data):
        self.data = data 
        self.children:list[TreeNode] = []

    def add(self, node):
        if self == node:
            return
        if node not in self.children:
            self.children.append(node)
            


def compute_depth(root: TreeNode) -> dict:
    levels = {}
    queue = [(root, 0)]

    while queue:
        current, level = queue.pop(0)
        levels[current.data] = level

        for child in current.children:
            queue.append((child, level + 1))

    return levels

def count_nodes(root: TreeNode) -> int:
    count = 1
    for child in root.children:
        count += count_nodes(child)
    return count

def tree_height(root: TreeNode) -> int:
    if not root.children:
        return 1
    
    return 1 + max(tree_height(child) for child in root.children)

def sum_tree(root: TreeNode) -> int:
    sum = root.data
    for child in root.children:
        sum += sum_tree(child)
    return sum

def count_leaf_nodes(root: TreeNode) -> int:
    if not root.children:
        return 1
    
    count = 0
    for child in root.children:
        count += count_leaf_nodes(child)
    
    return count

def contains_value(root: TreeNode, target) -> bool:
    if root.data == target:
        return True
    
    for child in root.children:
        if contains_value(root=child, target=target):
            return True
        continue

    return False

def count_nodes_with_min_children(root: TreeNode, n : int) -> bool:
    count = 0
    if len(root.children) >= n:
        count = 1
    for child in root.children:
        count += count_nodes(child)
    return count


def longest_path_length(root: TreeNode) -> int:
    diameter = 0

    def dfs(node: TreeNode):
        nonlocal diameter
        if not node.children:
            return 1
        
        max_heights = [0, 0]

        for child in node.children:
            height = dfs(child)
            if height > max_heights[0]:
                max_heights = [height, max_heights[0]]
            elif height > max_heights[1]:
                max_heights[1] = height

        diameter = max(diameter, max_heights[0] + max_heights[1] + 1)

        return max_heights[0] + 1
    
    dfs(root)
    return diameter

def depth_first_search_in_order(root: TreeNode):
    None


def depth_first_search_pre_order(root: TreeNode, visited = None):
    if visited is None:
        visited = []
    visited.append(root)
    for child in root.children:
            depth_first_search_pre_order(root = child, visited=visited)

    return visited


def depth_first_search_post_order(root: TreeNode):
    None


def max_root_to_leaf_sum(root: TreeNode) -> tuple[int, list[int]]: 
    def dfs(node: TreeNode):
        best_path = []
        if not node.children:
            return node.data, [node.data]
        
        max_sum = 0

        for child in node.children:
            child_sum, child_path = dfs(child)
            if child_sum > max_sum:
                max_sum = child_sum
                best_path = child_path
                
        return node.data + max_sum, [node.data] + best_path

    return  dfs(root)


def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    None