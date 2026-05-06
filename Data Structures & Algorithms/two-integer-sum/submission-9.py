class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_set = dict()
        for integer, value in enumerate(nums):
            dict_set[value]=dict_set.get(value, [])
            dict_set[value].append(integer)

        for elem in dict_set.keys():
            goal = target-elem
            if dict_set.get(goal) and (goal != elem):
                temp = [dict_set[goal][0], dict_set[elem][0]]
                temp.sort()
                return temp
            elif dict_set.get(goal) and len(dict_set.get(goal))>1:
                print(goal, elem)
                temp = [dict_set[goal][0], dict_set[goal][1]]
                temp.sort()
                return temp
