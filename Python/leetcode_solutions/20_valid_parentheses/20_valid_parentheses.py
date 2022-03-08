class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = []
        start_end_p = {"(":")", "[":"]", "{":"}"}
        for c in s:
            if c in start_end_p.keys(): # If the character is a starting bracket
                parentheses.append(c)
                continue
            if c in start_end_p.values(): # If the character is an ending bracket
                # If there are more closing brackets than opening brackets currently open.
                if len(parentheses) == 0:
                    return False

                # Checks if the most recent opening bracket matches the most recent closing bracket.
                if c == start_end_p[parentheses[-1]]:
                    parentheses.pop(len(parentheses)-1)
                else:
                    break
        if len(parentheses) > 0:
            return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("(]"))