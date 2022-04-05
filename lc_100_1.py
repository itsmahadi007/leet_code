class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            x = target - nums[i]
            try:
                
                j = nums.index(x)
                if i != j:
                    return [i,j]
                else:
                    continue
            except:
                continue
  
"""
Runtime: 1500 ms, faster than 30.24% of Python3 online submissions for Two Sum.
Memory Usage: 14.9 MB, less than 96.05% of Python3 online submissions for Two Sum.
"""
