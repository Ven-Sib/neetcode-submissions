class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        res = []
        i = 0
        while i < k:
            res.append(sorted_items[i][0])
            i += 1
        return res    

        