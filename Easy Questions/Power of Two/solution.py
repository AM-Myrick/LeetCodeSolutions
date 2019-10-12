class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # use the bitwise operator to convert n and n - 1 to binary
        # if any of n and n-1's on bits line up, it evaluates to 1
        # otherwise, it evaluates to 0
        return n != 0 and (n & (n - 1)) == 0