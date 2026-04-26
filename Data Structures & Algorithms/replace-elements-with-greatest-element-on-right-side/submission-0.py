class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(0,len(arr)):
            temp = 0 
            for x in range(i+1,len(arr)):
                if temp < arr[x]:
                    temp = arr[x]
            arr[i] = temp 
            
        arr[-1] = -1


        return arr
            