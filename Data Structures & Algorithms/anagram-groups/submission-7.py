class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        print_dict = dict()
        for elem in strs:
            finger_print = 26*[0]
            for char in elem:
                finger_print[ord(char) - ord('a')] += 1
            finger_print = tuple(finger_print)
            if finger_print in print_dict:
                print_dict[finger_print].append(elem)
            else:
                print_dict[finger_print] = [elem]
    
        return(list(print_dict.values()))