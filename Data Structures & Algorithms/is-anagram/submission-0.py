class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        tDict = {}

        for letter in s:
            if letter not in sDict.keys():
                sDict[letter] = 1
            elif letter in sDict.keys():
                sDict[letter] += 1
        
        for letter in t:
            if letter not in tDict.keys():
                tDict[letter] = 1
            elif letter in tDict.keys():
                tDict[letter] += 1

        if len(sDict.keys()) > len(tDict.keys()):
            return False
        elif len(sDict.keys()) < len(tDict.keys()):
            return False 
        elif len(sDict.keys()) == len(tDict.keys()):
            for subKey in sDict.keys():
                if subKey not in tDict or sDict[subKey] != tDict[subKey]:
                    return False
            return True