class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == "":
            return ""
        countT = {}
        window = {}
        for c in s1:
            countT[c] = 1 + countT.get(c,0)
        
        have, need = 0, len(countT)
        
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            
            window[c] = 1 + window.get(c,0)

            if c in countT and countT[c] == window[c]:
                have += 1
            while have == need:
                if (r-l+1) == len(s1):
                    return True

                window[s2[l]] -= 1
                
                if s2[l] in countT and window[s2[l]] < countT[s2[l]]:
                    have -= 1 
                l += 1
               
                
        return False