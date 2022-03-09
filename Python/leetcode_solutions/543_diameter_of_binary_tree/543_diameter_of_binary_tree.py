class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root):
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left),
                       self.maxDepth(root.right))

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0

        # Left Side check
        left_side_length = self.maxDepth(root.left)
        # Right Side check
        right_side_length = self.maxDepth(root.right)
        longest_path = left_side_length + right_side_length
        return max(self.diameterOfBinaryTree(root.left), longest_path, self.diameterOfBinaryTree(root.right))

if __name__ == "__main__":
    # Create tree
    root = TreeNode(1)
    # First level
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # Second level
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    print(solution.diameterOfBinaryTree(root))