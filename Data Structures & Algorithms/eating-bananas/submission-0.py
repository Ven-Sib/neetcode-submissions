class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
            - initiate 2 pointers (l, r) at 0 and at max pile in piles
            - set res value to r because we can potentially eat fastest at max of   piles
            - while l <= r, set mid value to (l+r)//2
            - calculate the time taken to eat a pile at a certain speed
            - if the total time is less than h, means we move to the left side of our k values, update res too
            - else to the right
        
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r)//2
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(float(p)/k)
            if totalTime <= h:
                res = k
                r = k -1
            else:
                l = k + 1
        return res

