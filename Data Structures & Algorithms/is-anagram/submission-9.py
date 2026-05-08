class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = dict()
        for elem in s:
            s_dict[elem] = s_dict.get(elem, 0) + 1
            
        t_dict = dict()
        for elem in t:
            t_dict[elem] = t_dict.get(elem, 0) + 1

        return s_dict == t_dict
            
