test_cases  = [
    {
        "input":"III",
        "output":3
    },
    {
        "input":"LVIII",
        "output":58
    },
    {
        "input":"MCMXCIV",
        "output":1994
    }
]

class Solution():
    symbol_values = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }

    def romanToInt(self, s:str) -> int:
        sum = 0
        prev_value = float('inf')
        for i, c in enumerate(s):
            value = self.symbol_values[c]
            if value > prev_value:
                sum += value-2*prev_value+self.romanToInt(s[i+1:])
                return sum
            sum += value
            prev_value = value
        return sum

for i, case in enumerate(test_cases):
    solution = Solution()
    output = solution.romanToInt(case["input"])
    is_pass = output == case["output"]
    print(f"case {i+1}: {is_pass} (Output:{output}, solution:{case['output']})")