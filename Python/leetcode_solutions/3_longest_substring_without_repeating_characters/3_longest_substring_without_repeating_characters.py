class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letter_positions = {}
        longest_substring_length = 0
        substring = ""
        for index, letter in enumerate(s):
            if letter in substring:
                if len(substring) > longest_substring_length:
                    longest_substring_length = len(substring)
                substring = s[letter_positions[letter]+1:index]
            letter_positions[letter] = index
            substring += letter
        if len(substring) > longest_substring_length:
            longest_substring_length = len(substring)
        return longest_substring_length

if __name__ == "__main__":
    solution = Solution()
    s = "abcabcbb"
    print(solution.lengthOfLongestSubstring(s))