# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:
        # base case
        if s == "":
            return ""
        # reverses the string and splits it into an list
        s = s.split()[::-1]
        # reverses each word within the list
        s = [word[::-1] for word in s]
        result = ""
        # since the list is already reversed
        # the last word of s should be the first word of result
        # so just pop while adding spaces, then add the last word
        # without a space and return
        while len(s):
            if len(s) == 1:
                result += s.pop()
                return result
            result += s.pop() + " "