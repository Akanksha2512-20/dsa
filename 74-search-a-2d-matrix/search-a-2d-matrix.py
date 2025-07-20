class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary(row,target):
            start,end = 0,len(row)-1
            while start<=end:
                mid = (start + end)//2
                if row[mid]<target:
                    start = mid + 1
                elif row[mid]==target:
                    return True    
                else:
                    end = mid -1
            return False

        for row in matrix:
            if binary(row,target):
                return True
        return False           