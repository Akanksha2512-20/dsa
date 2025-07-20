class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sum.append(current_sum)

    def pickIndex(self) -> int:
        target = random.randint(1, self.prefix_sum[-1])
        # Use binary search to find the right index
        index = bisect.bisect_left(self.prefix_sum, target)
        return index
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()