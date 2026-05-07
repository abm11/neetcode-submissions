class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        for elem in nums:
            freq_dict[elem] = freq_dict.get(elem, 0) + 1       

        freq_list = [[] for x in range(len(nums) + 1)]
        for key, value in freq_dict.items():
            freq_list[value].append(key)
        

        ret_list = list()
        for elem in range(len(freq_list)-1, -1, -1):
            if len(freq_list[elem]) >=1:
                for sub_elem in freq_list[elem]:
                    if k==0:
                        return ret_list
                    ret_list.append(sub_elem)
                    k-=1
        return ret_list

