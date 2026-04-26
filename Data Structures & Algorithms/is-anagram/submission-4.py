class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstMap = {}
        secondMap = {}

        if len(s) != len(t):
            return False
        else:
            for letter in s:
                if letter not in firstMap:
                    firstMap[letter] = 1
                else:
                    firstMap[letter] += 1

            for letter in t:
                if letter not in secondMap:
                    secondMap[letter] = 1
                else:
                    secondMap[letter] += 1
            
        return firstMap == secondMap