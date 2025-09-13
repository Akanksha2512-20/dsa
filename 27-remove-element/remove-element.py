class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        tmp = []
        for num in nums:
            if num == val:
                continue
            tmp.append(num)
            nums[:len(tmp)]= tmp
        return len(tmp)               
        