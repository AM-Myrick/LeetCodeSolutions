# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from collections import Counter
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        listA, listB = A.split(" "), B.split(" ")
        word_counter = Counter(listA) + Counter(listB)
        result = []
        
        for k, v in word_counter.items():
            if listA.count(k) == 0 and listB.count(k) == 1 or listB.count(k) == 0 and listA.count(k) == 1:
                result.append(k)
        return result