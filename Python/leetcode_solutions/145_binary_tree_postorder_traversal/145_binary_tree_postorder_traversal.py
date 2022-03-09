# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        if root is None:
            return []
        return (self.postorderTraversal(root.left) +
                self.postorderTraversal(root.right) +
                [root.val])

if __name__ == "__main__":
    # Create tree
    tree_node = TreeNode(1)
    tree_node.right = TreeNode(2)
    tree_node.right.left = TreeNode(3)

    solution = Solution()
    print(solution.postorderTraversal(tree_node))