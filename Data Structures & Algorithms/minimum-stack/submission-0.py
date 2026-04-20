class MinStack:
    stack = []
    minVal = []

    def __init__(self):
        self.stack = []
        self.minVal = []    

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minVal) <= 0:
            self.minVal.append(val)
        else:
            if val <= self.minVal[-1]:
                self.minVal.append(val)
            else:
                self.minVal.append(self.minVal[-1])
                
            

    def pop(self) -> None:
        if len(self.stack) <= 0:
            return "cant pop the length is already 0"
        else:
            self.stack.pop()
            self.minVal.pop()
            


    def top(self) -> int:
        if len(self.stack) <= 0:
            return "No top element the length is already 0"
        else:
            return self.stack[-1]
        
    def getMin(self) -> int:
        if len(self.stack) <= 0:
            return "No length is already 0"
        else:
            return self.minVal[-1]
        
