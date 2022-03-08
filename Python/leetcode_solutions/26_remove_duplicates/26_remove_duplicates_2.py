class Solution:
    def removeDuplicates(self, nums: list) -> int:
        original_values = list(set(nums))
        original_values.sort()
        for i, value in enumerate(original_values):
            nums[i] = value
        return len(original_values)

if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,0,0,0,3,3]
    k = solution.removeDuplicates(nums)
    print(f"k = {k}\nnums = {nums}")