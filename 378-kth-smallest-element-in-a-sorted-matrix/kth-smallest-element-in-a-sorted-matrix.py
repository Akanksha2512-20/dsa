class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        # Initialize a min-heap with elements from the first column
        min_heap = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(min_heap)

        # Extract the minimum element k-1 times
        for _ in range(k-1):
            val, r, c = heapq.heappop(min_heap)
            if c + 1 < n:
                # Push the next element in the same row to the heap
                heapq.heappush(min_heap, (matrix[r][c+1], r, c+1))

        # The top of the heap is the k-th smallest element
        return heapq.heappop(min_heap)[0] 
        