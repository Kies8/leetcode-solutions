class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1
        string = []
        while i >= 0:
            if s[i] != " ":
                string.append(s[i])
            if s[i] == " " and string:
                i = -1
            i -= 1
        return len(string)