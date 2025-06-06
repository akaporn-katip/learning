import unittest

from tree import (
    TreeNode,
    compute_depth,
    contains_value,
    count_leaf_nodes,
    count_nodes,
    count_nodes_with_min_children,
    depth_first_search_pre_order,
    longest_path_length,
    max_root_to_leaf_sum,
    sum_tree,
    tree_height,
)


class TestTree(unittest.TestCase):

    

    def test_add_root_node(self):
        root = TreeNode(10) 
        self.assertEqual(root.data, 10)


    def test_add_child(self):
        root = TreeNode(10)
        child = TreeNode(20)
        root.add(child)
        self.assertEqual(len(root.children), 1)
        
    def test_add_same_child(self):
        root = TreeNode(10)
        child = TreeNode(20)
        root.add(child)
        root.add(child)
        self.assertEqual(len(root.children), 1)
        
    def test_add_root(self):
        root = TreeNode(10)
        root.add(root)
        self.assertEqual(len(root.children), 0)
        
    def test_get_depth(self):
        A = TreeNode("A")
        B = TreeNode("B")
        C = TreeNode("C")
        D = TreeNode("D")
        E = TreeNode("E")
        F = TreeNode("F")
        G = TreeNode("G")
        H = TreeNode("H")
        
        B.add(E)
        B.add(F)
        
        D.add(G)
        
        G.add(H)
        
        A.add(B)
        A.add(C)
        A.add(D)
        
        self.assertEqual(compute_depth(A), {'A': 0, 'B': 1, 'C': 1, 'D': 1, 'E': 2, 'F': 2, 'G': 2, 'H': 3})

    def test_count_nodes(self):
        A = TreeNode("A")
        B = TreeNode("B")
        C = TreeNode("C")
        D = TreeNode("D")
        E = TreeNode("E")
        F = TreeNode("F")
        G = TreeNode("G")
        H = TreeNode("H")
        
        B.add(E)
        B.add(F)
        
        D.add(G)
        
        G.add(H)
        
        A.add(B)
        A.add(C)
        A.add(D)
        
        self.assertEqual(count_nodes(A), 8)

    def test_tree_height(self):
        A = TreeNode("A")
        B = TreeNode("B")
        C = TreeNode("C")
        D = TreeNode("D")
        E = TreeNode("E")
        F = TreeNode("F")
        G = TreeNode("G")
        H = TreeNode("H")
        I = TreeNode("I")
        
        B.add(E)
        B.add(F)
        
        D.add(G)
        
        G.add(H)
        
        A.add(B)
        A.add(C)
        A.add(D)

        H.add(I)
        
        self.assertEqual(tree_height(A), 5)

    def test_tree_height_2(self):
        A = TreeNode("A")
        B = TreeNode("B")
        C = TreeNode("C")
        D = TreeNode("D")

        A.add(B)
        A.add(C)
        B.add(D)

        self.assertEqual(tree_height(A), 3)
    

    def test_sum_tree(self):
        A = TreeNode(10)
        B = TreeNode(10)
        C = TreeNode(10)
        D = TreeNode(10)
        E = TreeNode(10)

        A.add(B)
        A.add(C)
        B.add(D)
        D.add(E)

        self.assertEqual(sum_tree(A), 50)


    def test_count_leaf_nodes(self):
        A = TreeNode(10)
        B = TreeNode(10)
        C = TreeNode(10)
        D = TreeNode(10)
        E = TreeNode(10)

        A.add(B)
        A.add(C)
        B.add(D)
        D.add(E)

        self.assertEqual(count_leaf_nodes(A), 2)

    def test_contains_child(self):
        A = TreeNode("A")
        B = TreeNode("B")
        C = TreeNode("C")
        D = TreeNode("D")
        E = TreeNode("E")
        F = TreeNode("F")
        G = TreeNode("G")
        H = TreeNode("H")

        B.add(E)
        B.add(F)
        
        D.add(G)
        
        G.add(H)
        
        A.add(B)
        A.add(C)
        A.add(D)

        self.assertTrue(contains_value(A, "A"))
        self.assertTrue(contains_value(A, "G"))
        self.assertTrue(contains_value(A, "H"))
        self.assertFalse(contains_value(A, "Z"))

    def test_count_nodes_with_min_children(self):
        A = TreeNode("A")
        B = TreeNode("B")
        C = TreeNode("C")
        D = TreeNode("D")
        E = TreeNode("E")
        F = TreeNode("F")
        G = TreeNode("G")
        H = TreeNode("H")

        B.add(E)
        B.add(F)
        
        D.add(G)
        
        G.add(H)
        
        A.add(B)
        A.add(C)
        A.add(D)
        self.assertTrue(count_nodes_with_min_children(A, 2), 2)

    def test_longest_path_length(self):
        A = TreeNode("A")
        B = TreeNode("B")
        C = TreeNode("C")
        D = TreeNode("D")
        E = TreeNode("E")
        F = TreeNode("F")
        G = TreeNode("G")
        H = TreeNode("H")
        # J = TreeNode("J")

        
        A.add(B)
        A.add(C)
        A.add(D)
        
        D.add(E)
        D.add(F)
        
        B.add(G)
        
        G.add(H)

        
        self.assertEqual(longest_path_length(A), 6)
        self.assertEqual(longest_path_length(H), 0)

    def test_dfs_pre_order(self):
        A = TreeNode("A")
        B = TreeNode("B")
        C = TreeNode("C")
        D = TreeNode("D")
        E = TreeNode("E")
        F = TreeNode("F")
        G = TreeNode("G")
        H = TreeNode("H")

        
        A.add(B)
        A.add(C)
        A.add(D)
        
        B.add(E)
        B.add(F)
        
        D.add(G)
        
        G.add(H)
        
        self.assertEqual(' -> '.join(list(map(lambda x: x.data, depth_first_search_pre_order(A)))), 'A -> B -> E -> F -> C -> D -> G -> H')

    def test_max_root_to_leaf_sum(self):
        A = TreeNode(5)
        B = TreeNode(3)
        C = TreeNode(8)
        D = TreeNode(-2)
        E = TreeNode(6)
        F = TreeNode(1)
        G = TreeNode(4)
        H = TreeNode(7)

        A.add(B)
        A.add(C)

        B.add(D)
        B.add(E)

        C.add(F)

        E.add(G)
        F.add(H)


        [sum, nodes] = max_root_to_leaf_sum(A)
        self.assertEqual(sum, 21)
        self.assertEqual(nodes, [5, 8 ,1 ,7])

if __name__ == '__main__':
    unittest.main()
