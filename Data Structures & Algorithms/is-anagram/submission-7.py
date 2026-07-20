class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # brute force we can use 2 loops and check the occurance each letter
        # optimize we use a hashmap to capture the occurance of each letter

        

        if len(s) != len(t):
            return False
        else:
            occurance_s = {}
            occurance_t = {}
            for s_letter, t_letter in zip(s,t):
                if s_letter in occurance_s:
                    occurance_s[s_letter] += 1
                elif s_letter not in occurance_s:
                    occurance_s[s_letter] = 0

                if t_letter in occurance_t:
                    occurance_t[t_letter] += 1
                elif  t_letter not in  occurance_t:
                    occurance_t[t_letter] = 0

            if occurance_s == occurance_t:
                return True
            else:
                return False 

                
            