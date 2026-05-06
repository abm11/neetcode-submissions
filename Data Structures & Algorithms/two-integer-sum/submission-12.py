class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()

        for integer, value in enumerate(nums):
            temp = target - value 
            if temp in nums_dict:
                return [nums_dict[temp], integer] 

            nums_dict[value] = integer
            

