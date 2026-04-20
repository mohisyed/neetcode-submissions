class Solution:
    def isValid(self, s: str) -> bool:
      checkHashmap = {"}": "{", "]": "[", ")": "("}
      stack = []
      for letter in s:
        if letter in checkHashmap:
          if stack and stack[-1] == checkHashmap[letter]:
            stack.pop()
          else:
            return False
        else:
          stack.append(letter)  
      return True if not stack else False 




