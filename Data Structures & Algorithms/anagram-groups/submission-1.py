class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for s in strs:
            char_freq = [0] * 26

            for letter in s:
                idk = ord(letter) - ord('a')
                char_freq[idk] += 1
            
            seen[tuple(char_freq)].append(s)
        print(seen.values())
        return list(seen.values())