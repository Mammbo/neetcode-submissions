class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # i am given the heighets wherre each height[i] repersents the height of the ith bar
        # from this i need to calculate the area and return the max amount of water this container can hold 

        # just thinking this problem can i use any optimization on the list to traverse it ? 
        # stacks wouldnt make too much sense because i need to find the area between two points

        # hashmap doesnt make much sense either cause i still need to use two pointers and it would just be used for storage of a max which i can just return using a variable 

        # i think the strategy here is defining two pointers to traverse the list starting from both ends
        #  i am pretty sure though that you need a sorted list for two pointers 

        # i will revist that in a sec lets walk through how to calculate the area through this method 

        # so the heights of the bar are 7 and 6, their distance from each other is 7 - 1 = 6, the lowest bar is what traps the water so 6 * 6 = which is our answer
        # so to calculate the max area of a container we need to get the min value of the heights the pointers are on and multiply it by the distance between them.

        # how would the two pointer logic on this work though ? 
        # start left and right end, calulcate that area
        # make that the max area 
        # compare which bar is less than the other
        # move that one up one
        # repeat
        # with that though in this example at some point they equal each other
        # i guess i can just make the condition less than or equal to the left bar
        # this also makes sense because the max height of the left bar would be the biggest total area up until that point

        max_water = 0 

        left, right = 0, len(heights) - 1
        while left < right:
            total_water = (right - left) * min(heights[left], heights[right])
            max_water = max(max_water, total_water)

            if heights[left] < heights[right]: 
                left += 1
            # if heights[left] is equal to or greater than height[right] move right pointer
            else:
                right -= 1
        return max_water

  
    

        