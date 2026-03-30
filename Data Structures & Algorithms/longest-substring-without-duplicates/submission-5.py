class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        charSet = set()

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            longest = max(longest, r - l + 1)
        return longest


        