def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i-1])

        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i+1])

        water = 0
        for i in range(n):
            min_ht = min(left_max[i], right_max[i])
            if min_ht - height[i] >= 0:
                water += min_ht - height[i]
        return water

        
