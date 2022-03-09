=Check Completeness of a Binary Tree=

Checks if a binary tree is complete.
Conditions for a complete binary tree:
1) All levels preceding the last level is filled completely.
2) The last level is filled from left to right with no gaps.

<Examples>
Example 1:

Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (ie. levels with node-values {1} and {2, 3}), and all nodes in the last level ({4, 5, 6}) are as far left as possible.

Example 2:

Input: root = [1,2,3,4,5,null,7]
Output: false
Explanation: The node with value 7 isn't as far left as possible.

Problem link: https://leetcode.com/problems/check-completeness-of-a-binary-tree/
