test_cases = [
    {
        "input":["flower","flow","flight"],
        "output":"fl"
    },
    {
        "input":["dog","racecar","car"],
        "output":""
    }
]

class Solution:
    def longestCommonPrefix(self, strs:list) -> str:
        if len(strs) == 0:
            return ""
        matching_str = strs[0]
        if len(strs) == 1:
            return matching_str
        for str in strs[1:]:
            if len(str) < len(matching_str):
                matching_str = matching_str[:len(str)]
            for i, (c1, c2) in enumerate(zip(matching_str, str)):
                if c1 != c2:
                    matching_str = matching_str[:i]
        return matching_str
    
if __name__ == "__main__":
    solution = Solution()
    for i, case in enumerate(test_cases):
        output = solution.longestCommonPrefix(case["input"])
        is_pass = output == case["output"]
        print(f"case {i+1}: {is_pass} (Output:{output}, solution:{case['output']})")