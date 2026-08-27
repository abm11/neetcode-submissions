class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for elem in s:
            if elem in s_dict:
                s_dict[elem] += 1
            else:
                s_dict[elem] = 1
        
        for elem in t:
            if elem in s_dict:
                s_dict[elem] -= 1
            else:
                return False
        
        for values in s_dict.values():
            if values != 0:
                return False
        return True
        