class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        for elem in nums:
            freq_dict[elem] = freq_dict.get(elem, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for key, value in freq_dict.items():
            buckets[value].append(key)
        
        ret_list = list()
        for x in range(len(buckets)-1, -1, -1):
            if len(buckets[x]) != 0:
                for elem in buckets[x]:
                    ret_list.append(elem)
                    k -= 1
                    if k == 0:
                        return ret_list