class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        length = len(nums)
        if not length:
            return - 1
        start = 0
        end = length - 1
        while start <= end:
            middle = (start + end) / 2
            if nums[middle] == target:
                return middle
            if nums[middle] < nums[end]:
                if nums[middle] < target and target <= nums[end]:
                    start = middle + 1
                else:
                    end = middle - 1
            else:
                if nums[start] <= target and target < nums[middle]:
                    end = middle - 1
                else:
                    start = middle + 1
        return - 1