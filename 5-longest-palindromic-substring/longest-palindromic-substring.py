class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        maxLen = 0
        for center in range(len(s)):
            #for odd length
            l = center
            r = center
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > maxLen:
                    maxLen = r-l+1
                    best = s[l:r+1]
                l-=1
                r+=1
        
            #for even length
            l = center
            r = center+1
            while l>=0 and r<len(s) and s[l]==s[r]:
                if (r-l+1) > maxLen:
                    maxLen = r-l+1
                    best = s[l:r+1]
                l-=1
                r+=1

        return best
        