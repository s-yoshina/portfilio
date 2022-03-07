# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def display_list(node):
        if node is None:
            print("None")
            return
        print(f"{node.val}->", end="")
        ListNode.display_list(node.next)

class Solution:
    def traverse_list(self, node, nums=""):
        if node is None:
            return ""
        return self.traverse_list(node.next,nums)+str(node.val)

    def create_list(values, node=None):
        if values == []:
            return None
        node = ListNode(values[0])
        node.next = Solution.create_list(values[1:], node)
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        nums1 = self.traverse_list(l1)
        nums2 = self.traverse_list(l2)
        sum = str(int(nums1) + int(nums2))
        sum = [int(num) for num in sum]
        return Solution.create_list(sum[::-1])

if __name__ == "__main__":
    l1 = Solution.create_list([2,4,3])
    ListNode.display_list(l1)
    l2 = Solution.create_list([5,6,4])
    ListNode.display_list(l2)
    solution = Solution()
    added_numbers = solution.addTwoNumbers(l1,l2)
    ListNode.display_list(added_numbers)