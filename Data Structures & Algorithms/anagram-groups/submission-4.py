class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = dict()        
        
        for elem in strs:
            int_array = [0] * 26
            for char in elem:
                int_array[ord(char)-97] += 1

            if tuple(int_array) not in hash_dict:
                hash_dict[tuple(int_array)] = []
            hash_dict[tuple(int_array)].append(elem)
        return list(hash_dict.values())