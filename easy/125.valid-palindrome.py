class Solution:

    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s) - 1
        
        while start < end:
            if s[start].isalnum() and s[end].isalnum():
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
            
            start += 0 if s[start].isalnum() else 1
            end -= 0 if s[end].isalnum() else 1
            
            
        return True