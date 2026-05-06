class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
              
        super_dict = dict() 
        index = 0
        while index < len(s):
            super_dict[s[index]] = super_dict.get(s[index], 0) + 1
            super_dict[t[index]] = super_dict.get(t[index], 0) - 1
            index += 1

        return all(value == 0 for value in super_dict.values())