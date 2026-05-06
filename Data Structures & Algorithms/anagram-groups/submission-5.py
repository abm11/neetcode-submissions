class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_dict = dict()
        for elem in strs:
            hash = 26*[0]
            for char in elem:
                hash[ord(char) - 97] += 1
            hash = str(hash)
            if hash in hash_dict:
                hash_dict[str(hash)].append(elem)
            else:
                hash_dict[str(hash)] = [elem]

        return(list(hash_dict.values()))