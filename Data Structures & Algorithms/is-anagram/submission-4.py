class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = dict()
        dict_t = dict()

        for elem in s:
            if elem in dict_s:
                dict_s[elem] += 1
            else:
                dict_s[elem] = 1
        
        for elem in t:
            if elem in dict_t:
                dict_t[elem] += 1
            else:
                dict_t[elem] = 1

        return dict_t == dict_s
    


        