class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        super_set = {}
        for word in strs:
            temp_set = {}
            for char in word:
                temp_set[char] = temp_set.get(char, 0) + 1
            
            if tuple(sorted(temp_set.items())) in super_set:
                super_set.get(tuple(sorted(temp_set.items()))).append(word)

            else:
                super_set[tuple(sorted(temp_set.items()))] = [word]
                    
        return (list(super_set.values()))