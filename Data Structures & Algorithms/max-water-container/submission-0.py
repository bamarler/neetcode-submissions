class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left: int = 0
        right: int = len(heights) - 1

        max_volume = 0
        best_left = left
        best_right = right

        while left < right:
            curr_volume = min(heights[left], heights[right]) * (right - left) 
            if (curr_volume > max_volume):
                max_volume = curr_volume
                best_left = left
                best_right = right

            if (heights[left] > heights[right]):
                right -= 1
            else:
                left += 1

        return max_volume 

        