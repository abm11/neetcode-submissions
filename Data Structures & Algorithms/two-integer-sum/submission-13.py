class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        target_dict = dict()
        for index, value in enumerate(nums):
            temp = target-value
            if temp in target_dict:
                return([target_dict[temp], index])
            else:
                target_dict[value] = index

