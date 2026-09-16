class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = [[] for i in range(len(nums)+1)]

        dict1 = {}

        for i in nums:
            dict1[i] = 1 + dict1.get(i,0)
        for num, cnt in dict1.items():
            frq[cnt].append(num)
        
        res = []
        for i in range(len(frq)-1,0,-1):
            for num in frq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
