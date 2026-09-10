class Solution:
    def trap(self, height: List[int]) -> int:

        # since i am given an array on non negative integers of height
        # i think i have to traverse the list using pointers one at the end and one at the beginning

        # that would be an o(n) solution
        # the max amount of water that can be the absolute value of the left wall - the right wall

        # so my algo would start at 0 and len of arr

        #i would have a sum var
        if not height: 
            return 0
        left = 0 
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        res = 0

        while left < right: 
            if leftMax < rightMax:
                 left += 1
                 leftMax = max(leftMax, height[left])
                 res += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                res += rightMax - height[right]
            
        return res






    
        

    