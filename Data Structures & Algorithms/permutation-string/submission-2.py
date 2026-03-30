class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        og_freq = {}
        l =0 
        for s in s1:
            og_freq[s] = og_freq.get(s,0) + 1

        cur_freq = {}
        for r in range(len(s2)):
            cur_freq[s2[r]] = cur_freq.get(s2[r], 0) + 1
            if (r - l + 1) > len(s1):
                cur_freq[s2[l]] -= 1
                # If the count hits 0, remove the key so cur_freq == og_freq can work perfectly
                if cur_freq[s2[l]] == 0:
                    del cur_freq[s2[l]]
                l += 1
            if cur_freq == og_freq:
                return True
        return False