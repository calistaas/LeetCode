# Algoritm
# 1. Given an empty array name result for the return value
# 2. Use nested for loop to do the check, use sum var
# 3. If the sum variable equals to the target than append

class Solution:
    # The -> indicates the return value 
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for index in range (len(nums)-1):
            for sub_index in range (index+1,len(nums)):
                sum = nums[index]+nums[sub_index]
                if sum == target:
                    result+=[index,sub_index]
                    return result
                
                
        