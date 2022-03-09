class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.strip() == "":
            return 0
        return len((s.split())[-1])

if __name__ == "__main__":
    solution = Solution()
    s = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord(s))