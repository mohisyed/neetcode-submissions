class Solution:
    def isValid(self, s: str) -> bool:
      # so we need to essentially just create a stack
      # after that we need to create a hashmap with key being the close char and value being open value
      # once we iterate through the stack (while appending), we check the hashmap to see if there is a matching value 
      # if it doesnt have the correct value then we just return false 
      # return true 

      stack = []
      closeToOpen={ "}": "{", "]": "[", ")": "("}

      for char in s:
        if char in closeToOpen:
          if stack and stack[-1] == closeToOpen[char]:
            stack.pop()
          else:
            return False
        else:
          stack.append(char)

      return True if not stack else False 