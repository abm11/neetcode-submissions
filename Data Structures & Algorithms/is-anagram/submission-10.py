class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        st_array = 26*[0]

        for s_elem, t_elem in zip(s,t): 
            st_array[ord(s_elem) - ord('a')] +=1
            st_array[ord(t_elem) - ord('a')] -=1
        
        for elem in st_array:
            if elem != 0:
                return False
        return True 