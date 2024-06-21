def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """
    if not height:
        return 0
    
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water = 0
    
    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    
    return water

# 測試案例
height = [5, 0, 3, 4, 5, 6, 0, 1, 2, 0, 1, 0, 4]
print(trap(height))  