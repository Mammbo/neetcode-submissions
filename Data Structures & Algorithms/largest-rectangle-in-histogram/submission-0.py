class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
    # given an integer array of heights
    # each bar is 1 wide
    # we can not sort the input and we need the bars to be next to each other to compute that area
    # this makes it hard to use two pointers or just iterate through the list
    # my initaly thought process is to use a monatonic stack 
    # length of heights will be at leasy one so no immediate edge cases
    #the height can be 0 with 1 element so that is an edge case
    # i think i just need to handle it within the code


    # i am going to map heights and their index values to each other so i can use that data to compute the area because l x w
    
    # i think we want to make a monatonic stack that places areas on them and we just grab the last element off the stack, meaning the last element should be max_area
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][0] > height:
                popped_height, start_index = stack.pop()
                width = i - start_index
                area = popped_height * width
                max_area = max(max_area, area)

                start = start_index
            stack.append((height, start))
        
        n = len(heights)
        for height, start_index in stack: 
            width = n - start_index
            area = height * width
            max_area = max(max_area, area)
        
        return max_area





    # this is cool i liked this problem a lot and it makes sense to me 
    # the trick is to add the heights to the stack 
    # when we get a decreasing height element
    # we pop the height element off the leist until its untrue 
    # in each iteration we compute the area with l * w compute width from the current iteration - the i value stored in the stack 

    # lets wlak through two  example to see if it works
        
        
        


        