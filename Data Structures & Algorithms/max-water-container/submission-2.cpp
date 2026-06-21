class Solution {
public:
    int maxArea(vector<int>& heights) {
        int left = 0;
        int right = heights.size() - 1;

        int max_volume = 0;

        while (left < right) {
            int curr_volume = min(heights[left], heights[right]) * (right - left);

            if (curr_volume > max_volume) {
                max_volume = curr_volume;
            }

            if (heights[left] > heights[right]) {
                right--;
            }
            else {
                left++;
            }
        }

        return max_volume;
    }
};
