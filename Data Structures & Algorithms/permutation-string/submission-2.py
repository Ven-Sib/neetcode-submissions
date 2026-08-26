class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1, dict2 = {}, {}
        resLen = float("inf")

        for c in s1:
            dict1[c] = 1 + dict1.get(c,0)
        
        have = 0
        need = len(dict1)
        l = 0

        for r in range(len(s2)):
            c = s2[r]
            
            dict2[c] = 1 + dict2.get(c,0)

            if c in dict1 and dict1[c] == dict2[c]:
                have += 1
            while need == have:
                if (r-l+1) < resLen:
                    resLen = r-l+1
                    if resLen == len(s1):
                        return True
                dict2[s2[l]] -= 1

                if s2[l] in dict1 and dict1[s2[l]] > dict2[s2[l]]:
                    have -= 1
                l += 1
        return False

