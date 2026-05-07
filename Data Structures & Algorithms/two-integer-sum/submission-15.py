class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup_dict = dict()
        
        for index, value in enumerate(nums):
            temp = target - value
            if temp in lookup_dict:
                return [lookup_dict[temp], index]
            else:
                lookup_dict[value] = index