class Solution:
    def isValid(self, s: str) -> bool:
        close = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []

        for char in s:
            if char in close:
                stack.append(close[char])
            elif stack and char in stack[-1]:
                stack.pop()
            else:
                return False

        return not stack