class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 0:
            return strs

        anagram_dict = dict()
        for elem in strs:
            hash_array = 26*[0]
            for char in elem:
                hash_array[ord(char)-ord("a")] += 1


            if str(hash_array) in anagram_dict:
                anagram_dict[str(hash_array)].append(elem)
            else:
                anagram_dict[str(hash_array)] = [elem]


        return(list(anagram_dict.values()))