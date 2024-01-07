test_cases = [
    {
        "input":[[3,2,2,3],3],
        "output":2
    },
    {
        "input":[[0,1,2,2,3,0,4,2],2],
        "output":5
    }
]

class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        val_count = 0
        i = 0
        while(i < len(nums)-val_count):
            if nums[i] == val:
                # Shift all values past the current index to the left.
                for j in range(i,len(nums)-1-val_count):
                    nums[j] = nums[j+1]
                val_count += 1
            else:
                i += 1
        return len(nums)-val_count

for i, case in enumerate(test_cases):
    solution = Solution()
    output = solution.removeElement(*case["input"])
    is_pass = output == case["output"]
    print(f"case {i+1}: {is_pass} (Output:{output}, solution:{case['output']})")