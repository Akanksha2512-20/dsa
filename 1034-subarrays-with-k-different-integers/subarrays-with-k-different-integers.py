class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atmostk(k):
            freq = {}
            count = 0
            left = 0
            for right in range(len(nums)):
                freq[nums[right]] = freq.get(nums[right],0)+1
                while len(freq) > k:
                    freq[nums[left]]-=1
                    if freq[nums[left]]==0:
                        del freq[nums[left]]
                    left+=1
                count+= right-left+1    
            return count
                
        return atmostk(k)-atmostk(k-1)
        