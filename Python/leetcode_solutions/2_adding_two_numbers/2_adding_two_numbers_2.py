# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def to_number(n1: list):
            n = ""
            for number in n1:
                n += number
            return int(n)

        # Obtain the first number
        n1 = []
        while(l1 is not None):
            n1.append(str(l1.val))
            l1 = l1.next
        n1.reverse()
        n1 = to_number(n1)

        # Obtain the second number
        n2 = []
        while(l2 is not None):
            n2.append(str(l2.val))
            l2 = l2.next
        n2.reverse()
        n2 = to_number(n2)

        # Find sum and convert into a singly linked list.
        n3 = str(n1+n2)
        l3 = ListNode(int(n3[0]))
        for i in range(1,len(n3)):
            node = ListNode(n3[i], l3)
            l3 = node
        return l3