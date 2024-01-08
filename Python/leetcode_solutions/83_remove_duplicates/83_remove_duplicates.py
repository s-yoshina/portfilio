# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def create_list(values:list):
        if len(values) == 0:
            return None
        node = ListNode(values[0])
        node.next = ListNode.create_list(values[1:])
        return node
    
    def list(node, values:list=None) -> list:
        if node is None:
            return values
        if values is None:
            values = []
        values.append(node.val)
        return ListNode.list(node.next,values)

test_cases = [
    {
        "input":ListNode.create_list([1,1,2]),
        "output":ListNode.create_list([1,2])
    },
    {
        "input":ListNode.create_list([1,1,2,3,3]),
        "output":ListNode.create_list([1,2,3])
    },
    {
        "input":ListNode.create_list([]),
        "output":None
    }
]

class Solution:
    def deleteDuplicates(self, head:ListNode) -> ListNode:
        if head is None:
            return head
        # Find all unique values
        values = [head.val]
        head = head.next
        while(head is not None):
            if values[-1] < head.val:
                values.append(head.val)
            head = head.next
        return ListNode.create_list(values)

if __name__ == "__main__":
    solution = Solution()
    for i, test_case in enumerate(test_cases):
        output = solution.deleteDuplicates(test_case["input"])
        is_pass = output is test_case["output"] if output is None else output.list() == test_case["output"].list()
        solution_value = test_case["output"] if test_case["output"] is None else test_case["output"].list()
        output_value = output if output is None else output.list()
        print(f"case {i+1}: {is_pass} (Output:{output_value}, solution:{solution_value})")