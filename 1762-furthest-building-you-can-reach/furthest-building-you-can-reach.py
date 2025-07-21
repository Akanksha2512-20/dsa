class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        for i in range(len(heights)-1):
            diff = heights[i+1]-heights[i]
            if diff > 0:
                heapq.heappush(min_heap,-diff)
                bricks-=diff
                if bricks <0:
                    if ladders > 0:
                        bricks += -heapq.heappop(min_heap)
                        ladders-=1
                    else:
                        return i
        return len(heights)-1                    
                