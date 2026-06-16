class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        lenT = len(countT)
        have, need = 0, lenT
       
        res, resL = [-1,-1], float("inf")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)
            if c in countT and countT[c] == window[c]:
                have += 1
            while need == have:
                if (r-l+1) < resL:
                    resL = (r-l+1)
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l, r = res

        return s[l:r+1] if resL != float("inf") else ""
