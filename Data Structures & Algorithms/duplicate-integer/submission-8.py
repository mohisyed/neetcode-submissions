class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # i am thinking of 2 ways 
        # brute force is a 2 for loops mapping each char to see the occurance
        # optimal i think? is using the hash_map

        # this is the brute force but its o(n^2)
        # for i in range(len(nums)):
        #     for x in range(i+1, len(nums)):
        #         if nums[i] == nums[x]:
        #             return True
    
        # return False


        occurance = {}
        for num in nums:
            if num in occurance:
                return True
            elif num not in occurance:
                occurance[num] = 0 
        return False
        