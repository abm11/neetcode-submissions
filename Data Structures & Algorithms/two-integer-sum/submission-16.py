class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dup_dict = dict()
        for index, value in enumerate(nums):
            temp = target-value
            if temp in dup_dict:
                return [dup_dict[temp], index]
            dup_dict[value] = index