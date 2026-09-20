class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            total = 0
            for p in piles:
                total += math.ceil(p/k) 
            if total > h:
                l = k+1
            else:
                r = k-1
                res = min(res, k)
        return res

            
            