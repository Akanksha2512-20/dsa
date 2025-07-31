class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
    
        # If there's only one house, the max value to rob is just that house's value.
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses):
            prev1, prev2 = 0, 0
            for current_house_value in houses:
                # Calculate max money that can be robbed if including this house
                new_house = max(prev2 + current_house_value, prev1)
                prev2 = prev1
                prev1 = new_house
            return prev1
        
        # Rob houses from 0 to n-1 and houses from 1 to n to account for the circle.
        result1 = rob_linear(nums[:-1])  # Rob all but last house
        result2 = rob_linear(nums[1:])   # Rob all but first house
        return max(result1, result2)


        