test_cases = [
    {
        "input":["sadbutsad","sad"],
        "output":0
    },
    {
        "input":["leetcode", "leeto"],
        "output":-1
    }
]

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        max_range = len(haystack)-1*len(needle)
        for i in range(max_range+1):
            if haystack[i] == needle[0] and haystack[i:i+len(needle)] == needle:
                return i
        return -1

for i, case in enumerate(test_cases):
    solution = Solution()
    output = solution.strStr(*case["input"])
    is_pass = output == case["output"]
    print(f"case {i+1}: {is_pass} (Output:{output}, solution:{case['output']})")