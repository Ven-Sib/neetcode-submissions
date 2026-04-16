import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for i in nums:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1
        top_k_keys = heapq.nlargest(k, dict1, key=dict1.get)
        return top_k_keys