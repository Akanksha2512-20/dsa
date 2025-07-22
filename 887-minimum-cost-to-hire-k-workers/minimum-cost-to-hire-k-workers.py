class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        pairs = sorted([(w/q,q) for q,w in zip(quality,wage)], key=lambda p : p[0])
        max_heap = []
        total = 0
        res = float('inf')
        for rate,q in pairs:
            heapq.heappush(max_heap,-q)
            total+=q
            if len(max_heap) > k:
                total+=heapq.heappop(max_heap)

            if len(max_heap)==k:
                res = min(res,total*rate) 
        return res           



        