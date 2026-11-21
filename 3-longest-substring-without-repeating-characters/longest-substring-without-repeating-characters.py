class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        start = 0
        maxLen = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[start])
                start+=1
            
            seen.add(s[right])
            maxLen = max(right-start+1,maxLen)
        return maxLen



        