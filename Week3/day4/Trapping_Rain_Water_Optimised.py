class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = 0
        max_right = 0
        water = 0
        max_height = 0
        index = 0
        n = len(height)

        # find the highest bar and its index
        for i in range(n):
            if height[i] > max_height:
                max_height = height[i]
                index = i

        # left side
        left_max = 0
        for i in range(index):
            left_max = max(left_max, height[i])
            min_ht = min(left_max, max_height)
            if min_ht > height[i]:
                water += min_ht - height[i]

        # right side
        right_max = 0
        for i in range(n - 1, index, -1):
            right_max = max(right_max, height[i])
            min_ht = min(right_max, max_height)
            if min_ht > height[i]:
                water += min_ht - height[i]

        return water
