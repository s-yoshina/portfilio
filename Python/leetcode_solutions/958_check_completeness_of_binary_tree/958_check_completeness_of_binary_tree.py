class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def is_complete(self, root):
        if root is None:
            return True, 0, False
        complete_l, height_l, skewed_l = self.is_complete(root.left)
        complete_r, height_r, skewed_r = self.is_complete(root.right)
        complete = complete_l and complete_r
        height = 1 + height_l
        skewed = skewed_l or skewed_r # Whether the tree is skewed to the left

        # Condition 1: More than two left skewed trees leads to an incomplete tree
        # Condition 2: Every level preceding the lowest level needs to be filled.
        if (skewed_l and skewed_r) or (skewed_l and height_r != height_l-1):
            return False, height, True

        # If there is a a skew in the tree
        if height_r != height_l:
            # If the tree is skewed to the right or if a level before the leaf is not complete (filled)
            if (height_r > height_l) or (abs(height_l - height_r) > 1):
                complete = False
            else:
                skewed = True
        return complete, height, skewed

    def isCompleteTree(self, root:TreeNode) -> bool:
        complete = self.is_complete(root)
        if complete[0]:
            return True
        else:
            return False

if __name__ == "__main__":
    # Create tree
    root = TreeNode(1)
    # First level
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    # Second level
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    solution = Solution()
    print(solution.isCompleteTree(root))