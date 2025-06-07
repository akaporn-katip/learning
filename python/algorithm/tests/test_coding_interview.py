import unittest

from binary_tree import build_tree, to_values
from coding_interview import (
    group_angrams,
    invert_tree,
    is_palindrome,
    longest_repeat_substring,
    three_sum,
    two_sum,
    valid_parentheses,
)


class TestCodingInterview(unittest.TestCase):

    def test_two_sum(self):
        self.assertEqual(two_sum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(two_sum([3, 2, 4], 6), [1, 2])
        self.assertEqual(two_sum([3, 3], 6), [0, 1])

    def test_valid_parentheses(self):
        self.assertEqual(valid_parentheses("()"), True)
        self.assertEqual(valid_parentheses("()[]{}"), True)
        self.assertEqual(valid_parentheses("(]"), False)
        self.assertEqual(valid_parentheses("([])"), True)
        self.assertEqual(valid_parentheses("]"), False)
        self.assertEqual(valid_parentheses("(){}}{"), False)
        self.assertEqual(valid_parentheses("["), False)
        self.assertEqual(valid_parentheses("[[["), False)

    def test_longest_repeat_substring(self):
        self.assertEqual(longest_repeat_substring("abca"), 3)
        self.assertEqual(longest_repeat_substring("abcabcbb"), 3)
        self.assertEqual(longest_repeat_substring("bbbbb"), 1)
        self.assertEqual(longest_repeat_substring("pwwkew"), 3)

    def test_is_palindrome(self):
        self.assertEqual(is_palindrome('A man, a plan, a canal: Panama'), True)
        self.assertEqual(is_palindrome('race a car'), False)
        self.assertEqual(is_palindrome(' '), True)
        self.assertEqual(is_palindrome('A'), True)
        self.assertEqual(is_palindrome('0P'), False)
        self.assertEqual(is_palindrome('aba'), True)

    def test_group_angrams(self):
        self.assertListEqual(group_angrams(["eat", "tea", "tan", "ate", "nat", "bat"]),
                             [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
        self.assertListEqual(group_angrams([""]), [[""]])
        self.assertListEqual(group_angrams(["a"]), [["a"]])

    def test_invert_tree(self):
        root_1 = build_tree([4, 2, 7, 1, 3, 6, 9])
        expected_output_1 = build_tree([4, 7, 2, 9, 6, 3, 1])
        self.assertListEqual(to_values(invert_tree(root=root_1)), to_values(expected_output_1))

        root_2 = build_tree([])
        expected_output_2 = build_tree([])
        self.assertListEqual(to_values(invert_tree(root=root_2)), to_values(expected_output_2))

        root_3 = build_tree([1])
        expected_output_3 = build_tree([1])
        self.assertListEqual(to_values(invert_tree(root=root_3)), to_values(expected_output_3))

        root_4 = build_tree([1, None, 2, None, 3])
        expected_output_4 = build_tree([1, 2, None, 3])
        self.assertListEqual(to_values(invert_tree(root=root_4)), to_values(expected_output_4))

        root_5 = build_tree([1, 2, None, 3])
        expected_output_5 = build_tree([1, None, 2, None, 3])
        self.assertListEqual(to_values(invert_tree(root=root_5)), to_values(expected_output_5))

        root_6 = build_tree([1, 2, 3])
        expect_output_6 = build_tree([1, 3, 2])
        self.assertEqual(to_values(invert_tree(root=root_6)), to_values(expect_output_6))

    def test_three_sum(self):
        """
        โจทย์: 3Sum
        คำอธิบาย:
        กำหนดให้ array ของจำนวนเต็ม nums จงคืนค่า array ของ [nums[i], nums[j], nums[k]] ทั้งหมด ที่ i != j, i != k, และ j != k และ nums[i] + nums[j] + nums[k] == 0

        ข้อควรทราบ:

        ชุดคำตอบต้องไม่มีชุดซ้ำกัน (No duplicate triplets).
        ตัวอย่าง:

        nums = [-1, 0, 1, 2, -1, -4]

        Output: [[-1, -1, 2], [-1, 0, 1]]
        (อธิบาย:
        -1 + 0 + 1 = 0
        -1 + -1 + 2 = 0 )
        nums = [0, 1, 1]

        Output: []
        (ไม่มีสามตัวรวมกันได้ 0)
        nums = [0, 0, 0]

        Output: [[0, 0, 0]]
        ข้อจำกัด:

        3 <= nums.length <= 3000
        -10^5 <= nums[i] <= 10^5


        sort = [-4, -1 -1, 0, 1 , 2]
        """
        self.assertListEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1 , 2 ], [-1, 0, 1]])
        self.assertListEqual(three_sum([0,1,1]), [])
        self.assertListEqual(three_sum([0, 0, 0]), [[0, 0, 0]])
        self.assertListEqual(three_sum([0, 0, 0, 0]), [[0, 0, 0]])


if __name__ == '__main__':
    unittest.main()
