test_cases = [
    {
        "input":2,
        "output":2
    },
    {
        "input":3,
        "output":3
    },
    {
        "input":1,
        "output":1
    }
]

class Solution:
    solutions = [1,2]
    def climbStairs(self, n:int) -> int:
        if len(self.solutions) < n:
            for i in range(len(self.solutions),n):
                self.solutions.append(self.solutions[i-2]+self.solutions[i-1]) 
        return self.solutions[n-1]

for i, case in enumerate(test_cases):
    solution = Solution()
    output = solution.climbStairs(case["input"])
    is_pass = output == case["output"]
    print(f"case {i+1}: {is_pass} (Output:{output}, solution:{case['output']})")
