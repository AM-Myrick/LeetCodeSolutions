# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        copy = str(n)
        total = 0
        seen = set()
        
        while True:
            for letter in copy:
                number = int(letter)
                total += number ** 2
                
            if total == 1:
                return True
            
            if total in seen:
                return False
            
            seen.add(total)
            copy = str(total)
            total = 0