# https://leetcode.com/problems/unique-morse-code-words/
from typing import List, Dict
class Solution:
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    morse_code_dict: Dict[str, str] = {
      "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
    }
    # sets remove duplicates automatically
    result = set()
    # loop over each word, then each letter
    # convert each letter to morse code with dict lookup
    for word in words:
      new_word = ""
      for letter in word:
        new_word += morse_code_dict[letter]
      result.add(new_word)
    return len(result)