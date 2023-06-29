from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ans: int = 0
        for operation in operations:
            if operation in ["++X", "X++"]:
                ans += 1
            else:
                ans -=1
        return ans