class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        dict_s = dict()
        dict_t = dict()
    
        for elem in s:
            dict_s[elem] = dict_s.get(elem, 0) + 1
        
        for elem in t:
            dict_t[elem] = dict_t.get(elem, 0) + 1

        return dict_t == dict_s
    


        