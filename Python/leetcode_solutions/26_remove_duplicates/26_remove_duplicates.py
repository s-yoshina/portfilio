class Solution:
    def target_direction(self, target, nums, p):
        if nums[p] > target:
            return "left"
        elif nums[p] < target:
            return "right"
        else:
            return "target"

    def find_duplicate_range(self, target, nums):
        max = len(nums)-1
        min = 0
        mid = (max+min)//2
        while max > min:
            mid = (max+min)//2
            direction = self.target_direction(target, nums, mid)
            if direction == "target":
                if nums[mid+1] == target:
                    min = mid+1
                else:
                    return mid
            elif direction == "right":
                min = mid+1
            else:
                max = mid-1
        return (max+min)//2

    def removeDuplicates(self, nums: list) -> int:
        n_nums = 0
        p = 0
        while p < len(nums):
            nums[n_nums] = nums[p]
            if p == len(nums)-1:
                n_nums += 1
                break
            if nums[p] == nums[p+1]:
                shift = self.find_duplicate_range(nums[p], nums[p:])
                p += shift
            p += 1
            n_nums += 1
        return n_nums

if __name__ == "__main__":
    solution = Solution()
    nums = [-1,0,0,0,0,3,3]
    k = solution.removeDuplicates(nums)
    print(f"k = {k}\nnums = {nums}")
