# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right))

if __name__ == "__main__":
    # Create tree
    root = TreeNode(3)
    # First level
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    # Second level
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    print(solution.maxDepth(root))