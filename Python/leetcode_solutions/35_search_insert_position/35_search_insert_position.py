test_cases = [
    {
        "input":[[1,3,5,6],5],
        "output":2
    },
    {
        "input":[[1,3,5,6],2],
        "output":1
    },
    {
        "input":[[1,3,5,6],7],
        "output":4
    },
    {
        "input":[[1,3,5,6],0],
        "output":0
    }
]

class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        search_list = nums
        num_min = 0
        while(len(search_list) > 0):
            i = len(search_list)//2
            if search_list[i] == target:
                return num_min+i
            elif search_list[i] > target:
                search_list = search_list[:i]
            else:
                search_list = search_list[i+1:]
                num_min += i+1
        return num_min
        
for i, case in enumerate(test_cases):
    solution = Solution()
    output = solution.searchInsert(*case["input"])
    is_pass = output == case["output"]
    print(f"case {i+1}: {is_pass} (Output:{output}, solution:{case['output']})")