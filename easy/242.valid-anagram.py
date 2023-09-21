class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hash_t = {}
        hash_s = {}
        for i in range(len(s)):
            if s[i] not in hash_s:
                hash_s[s[i]] = 0
            if t[i] not in hash_t:
                hash_t[t[i]] = 0
                
            hash_s[s[i]] += 1
            hash_t[t[i]] += 1

        return hash_t == hash_s