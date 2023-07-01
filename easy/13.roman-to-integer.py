class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        roman_list = list(s)
        ans: int = 0

        current = roman[roman_list[-1]]
        while roman_list:
            new = roman[roman_list.pop()]
            if current > new:
                ans -= new
            else:
                current = new
                ans += new
        
        return ans


solution = Solution().romanToInt("MCMXCIV")
print(solution)