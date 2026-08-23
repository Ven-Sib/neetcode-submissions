class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        frq = [[] for i in range(len(nums)+1)]
        res = []

        for n in nums:
            dict1[n] = 1 + dict1.get(n,0)
        
        for n, c in dict1.items():
            frq[c].append(n)
        
        for i in range(len(frq)-1, 0, -1):
            for n in frq[i]:
                res.append(n)
                if len(res) == k:
                    return res


                
        