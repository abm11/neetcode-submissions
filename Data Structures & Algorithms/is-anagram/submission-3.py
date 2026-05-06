class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
              
        super_dict = dict() 
        for a, b in zip(s, t):
            super_dict[a] = super_dict.get(a, 0) + 1
            super_dict[b] = super_dict.get(b, 0) - 1

        return all(value == 0 for value in super_dict.values())