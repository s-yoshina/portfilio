# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:
        if root is None:
            return []
        return ([root.val] +
                self.preorderTraversal(root.left) +
                self.preorderTraversal(root.right))

if __name__ == "__main__":
    # Create tree
    tree_node = TreeNode(1,None)
    tree_node.right = TreeNode(2)
    tree_node.right.left = TreeNode(3)

    solution = Solution()
    print(solution.preorderTraversal(tree_node))