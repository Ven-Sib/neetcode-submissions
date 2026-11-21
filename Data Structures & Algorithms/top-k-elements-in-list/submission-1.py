class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        frq = [[] for i in range(len(nums)+1)]
        dict1 = defaultdict(int)

        for i in nums:
            dict1[i] += 1
        
        for key, value in dict1.items():
            frq[value].append(key)
        
        for i in range(len(frq)-1,-1,-1):
            
            for j in frq[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return -1

        
            
