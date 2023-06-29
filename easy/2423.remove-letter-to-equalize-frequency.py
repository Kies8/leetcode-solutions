from collections import Counter


class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(word) == len(set(word)): 
            return True
        word = list(word)
        for i, char in enumerate(word):
            word.remove(char)
            if len(set(Counter(word).values())) == 1:
                return True
            else:
                word.insert(i, char)
        return False
    
solution = Solution().equalFrequency("cccaa")
print(solution)
