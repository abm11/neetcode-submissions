class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_set = set()
        for elem in nums:
            if elem in dup_set:
                return True
            dup_set.add(elem)
        return False