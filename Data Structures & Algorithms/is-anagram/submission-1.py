class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            letterMap = {}
            letterMap2 = {} 
            for letter in s:
                if letter in letterMap:
                    letterMap[letter] += 1
                elif letter not in letterMap:
                    letterMap[letter] = 0
            
            for letter in t:
                if letter in letterMap2:
                    letterMap2[letter] += 1
                elif letter not in letterMap2:
                    letterMap2[letter] = 0
            
            if letterMap == letterMap2:
                return True
            return False
        
        