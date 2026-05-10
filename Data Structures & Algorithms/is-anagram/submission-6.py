class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        seen2 = {}

        if len(s) != len(t):
            return False
        else:
            for letter1 in s:
                if letter1 in seen:
                    seen[letter1] += 1
                elif letter1 not in seen:
                    seen[letter1] = 1
                
            for letter2 in t:
                if letter2 in seen2:
                    seen2[letter2] += 1
                elif letter2 not in seen2:
                    seen2[letter2] = 1
            
        return seen == seen2
