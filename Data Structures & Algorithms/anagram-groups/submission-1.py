class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        super_set = {}

        for word in strs:
            finger_print = [0] * 26 
            for elem in word:
                finger_print[ord(elem) - ord('a')] +=1
            if tuple(finger_print) in super_set:
                super_set[tuple(finger_print)].append(word)
            else:
                super_set[tuple(finger_print)] = [word]
        

        return(list(super_set.values()))