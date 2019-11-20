# https://leetcode.com/problems/student-attendance-record-i/
class Solution:
    def checkRecord(self, s: str) -> bool:
        if "LLL" in s:
            return False
        absence_count = 0
        
        for letter in s:
            if letter == "A":
                absence_count += 1
                if absence_count > 1:
                    return False
        return True