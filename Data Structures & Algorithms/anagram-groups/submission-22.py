class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = dict()
        for elem in strs:
            hash_array = 26*[0]
            for char in elem:
                hash_array[ord(char)-ord("a")] += 1
            hash_array=tuple(hash_array)
            if hash_array in anagram_dict:
                anagram_dict[hash_array].append(elem)
            else:
                anagram_dict[hash_array] = [elem]


        return(list(anagram_dict.values()))