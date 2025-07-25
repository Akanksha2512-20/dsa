class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = [(lst[0], i, 0) for i, lst in enumerate(nums)]
        heapq.heapify(heap)
        
        # Determine the initial maximum value from the first elements of each list
        max_val = max(lst[0] for lst in nums)
        min_range = -float('inf'), float('inf')
        
        while heap:
            # Extract the smallest element from the heap
            min_val, from_list, index = heapq.heappop(heap)

            # Update the min_range if a smaller one is found
            if max_val - min_val < min_range[1] - min_range[0]:
                min_range = min_val, max_val

            # Move to next element in the current list
            if index + 1 < len(nums[from_list]):
                next_val = nums[from_list][index + 1]
                heapq.heappush(heap, (next_val, from_list, index + 1))
                # Update the maximum value
                max_val = max(max_val, next_val)
            else:
                # One of the lists has been exhausted, optimal range is found
                break
                
        return min_range
        