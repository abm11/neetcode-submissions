class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()

        for elem in nums:
            freq_dict[elem] = freq_dict.get(elem, 0) + 1

        print(freq_dict)
        bucket_list = [[] for i in range(len(nums)+1)]
        for key, value in freq_dict.items():
            bucket_list[value].append(key)
        
        print(bucket_list)
        ret_list = list()
        for i in range(len(bucket_list) - 1, -1, -1):
            for num in bucket_list[i]:
                ret_list.append(num)
                k -= 1
                if k == 0:
                    return ret_list

