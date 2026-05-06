class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        key_dict = dict()
        for elem in strs:
            key = 26*[0]
            for char in elem:
                key[ord(char) - 97] += 1
            key = tuple(key)
            if key in key_dict:
                key_dict[tuple(key)].append(elem)
            else:
                key_dict[tuple(key)] = [elem]

        return(list(key_dict.values()))