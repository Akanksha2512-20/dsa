class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        min_heap =[]
        res = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap,int(nums[i]))

            if len(min_heap)>k:
                heapq.heappop(min_heap)
        return str(min_heap[0])        


        