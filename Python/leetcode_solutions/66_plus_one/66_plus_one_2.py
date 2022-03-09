class Solution:
    def plusOne(self, digits: list) -> list:
        digits = "".join([str(i) for i in digits])
        digits = list(str(int(digits)+1))
        return digits

if __name__ == "__main__":
    solution = Solution()
    digits = [1,2,3]
    print(solution.plusOne(digits))