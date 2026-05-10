class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        newMap = {}

        for num in nums:
            if num not in newMap:
                newMap[num] = 1
            elif num in newMap:
                newMap[num] += 1
        
        new = newMap.items()

        new2 = sorted(new, key=lambda x: x[1],reverse=True)

        x = []
        for item in new2[:k]:
            x.append(item[0])
        return x 

        # return [item[0] for item in new2[:k]]
        