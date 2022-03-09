class Solution:
    def plusOne(self, digits: list) -> list:
        digits[-1] += 1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits = [1]+digits
                else:
                    digits[i-1] += 1
            else:
                break
        return digits

if __name__ == "__main__":
    solution = Solution()
    digits = [1,2,3]
    print(solution.plusOne(digits))