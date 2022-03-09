class Solution:
    def binary_search(self, min, max, condition):
        while min <= max:
            position = (max + min)//2
            result = condition(position, max, min)
            if result == "found":
                    return position
            elif result == "left":
                max = position-1
            else:
                min = position+1
        return -1

    def search(self, nums: list, target: int) -> int:
        def condition(position, max_position, min_position):
            if nums[position] == target:
                return "found"
            elif nums[position] > nums[max_position]: # axis on the right side case
                if target > nums[position] or target <= nums[max_position]:
                    return "right"
                return "left"
            elif nums[position] < nums[min_position]: # axis on the left side case
                if target < nums[position] or target >= nums[min_position]:
                    return "left"
                return "right"
            else:
                if target > nums[position]: # list in order
                    return "right"
                return "left"
        return self.binary_search(0, len(nums)-1, condition)

if __name__ == "__main__":
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(solution.search(nums, target))