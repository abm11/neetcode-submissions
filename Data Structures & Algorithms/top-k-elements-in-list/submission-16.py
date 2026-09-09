class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = {}
        for elem in nums:
            freq_dict[elem] = freq_dict.get(elem, 0) + 1


        bucket_list = [[] for _ in range(0, len(nums)+1)]
        for key, value in freq_dict.items():
            bucket_list[value].append(key)


        ret_list = []
        for elem in range(len(bucket_list)-1, -1, -1):
            for sub_elem in bucket_list[elem]:
                ret_list.append(sub_elem)
                if len(ret_list) == k:
                    return ret_list