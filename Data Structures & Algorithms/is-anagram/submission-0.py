class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = dict()        
        for elem in s:
            if s_dict.get(elem) is not None:
                s_dict[elem] += 1
            else:
                s_dict[elem] = 1
        
        t_dict = dict()
        for elem in t:
            if t_dict.get(elem) is not None:
                t_dict[elem] += 1
            else:
                t_dict[elem] = 1

        if t_dict == s_dict:
            return True
        else:
            return False