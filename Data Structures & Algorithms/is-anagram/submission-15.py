class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_dict = {}
        for elem in s:
            s_dict[elem] = s_dict.get(elem, 0) + 1
        
        for elem in t:
            if elem not in s_dict:
                return False
            s_dict[elem] -= 1
            if s_dict[elem] < 0:
                return False
        return True