class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        for elem in nums:
            freq_dict[elem] = freq_dict.get(elem, 0) + 1       

        freq_list = [[] for x in range(len(nums) + 1)]
        print(freq_list)
        for key, value in freq_dict.items():
            print(key, value)
            freq_list[value].extend([key])
        
        print(freq_list)

        ret_list = list()
        for elem in range(len(freq_list)-1, -1, -1):
            if len(freq_list[elem]) >=1:
                for sub_elem in freq_list[elem]:
                    if k==0:
                        return ret_list
                    ret_list.extend([sub_elem])
                    k-=1
                    print(ret_list)
        return ret_list

