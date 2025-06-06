


class BinaryTree:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def to_array(self) -> list:
        if not self : 
            return None
        q = [self]
        results = []

        while(q):

            node = q.pop(0)
            if node:
                results.append(node)
                q.append(node.left)
                q.append(node.right)
            else:
                results.append(None)

        while results and results[-1] is None:
            results.pop()

        return results
    


def build_tree(nodes: list) -> BinaryTree :
    if not nodes:
        return None
    
    root = BinaryTree(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current_node = queue.pop(0)
        
        if current_node:
            # Left child
            if i < len(nodes) and nodes[i] is not None:
                current_node.left = BinaryTree(nodes[i])
                queue.append(current_node.left)
            i += 1

            # Right child
            if i < len(nodes) and nodes[i] is not None:
                current_node.right = BinaryTree(nodes[i])
                queue.append(current_node.right)
            i += 1
            
    return root


def to_values(node: BinaryTree) -> list:
    if not node:
        return []
    return list(map(lambda x: x.value if x else None, node.to_array()))