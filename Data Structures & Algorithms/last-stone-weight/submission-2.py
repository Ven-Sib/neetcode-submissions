class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-x for x in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heap[0]
            if x == y:
                heapq.heappop(heap)
            elif x < y:
                heapq.heapreplace(heap, -(y-x))
        return -heap[0] if heap else 0



