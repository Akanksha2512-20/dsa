class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        left = 0
        right = len(letters) - 1
        result = 0

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] > target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        return letters[result]