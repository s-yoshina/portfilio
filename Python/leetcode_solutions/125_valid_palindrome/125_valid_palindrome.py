test_cases = [
    {
        "input":"A man, a plan, a canal: Panama",
        "output":True
    },
    {
        "input":"race a car",
        "output":False
    },
    {
        "input":" ",
        "output":True
    }
]

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        valid_chars = string.ascii_lowercase+string.digits
        front, end = 0, len(s)-1
        while(front<end):
            if s[front] not in valid_chars:
                front+=1
                continue
            if s[end] not in valid_chars:
                end-=1
                continue
            if s[front] != s[end]:
                return False
            front += 1
            end -= 1
        return True

for i, case in enumerate(test_cases):
    solution = Solution()
    output = solution.isPalindrome(case["input"])
    is_pass = output == case["output"]
    print(f"case {i+1}: {is_pass} (Output:{output}, solution:{case['output']})")