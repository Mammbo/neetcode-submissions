class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # i am given an array of temps
        # temp[i] -> temp on the ith day
        # return --> result which consists of the number of days after the ith day before a warmer temp in the future

        # create a result array of all 0's the length of temps so that if it is consistently decreasing i can just return the res as 0

        res = [0] * len(temperatures)

        # to process this since warmer means higher number consistently i think I need to use a monatonically decreasing stack 
        # i could loop through the array for each element but that would be an inefficent algorithim since two passes is O(n^2) time.
        # with a stack i could get O(n) space and time complexity because stack operations are O(1)


        # for loop and while loop strucutre?

        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                pop_val = stack.pop()
                res[pop_val[1]] = i - pop_val[1]

            stack.append([temperatures[i], i])

        return res

        # lets run through a test case
        # stack = [[40, 5], [28, 6]]
        # temps = [30,38,30,36,35,40,28]
        # res = [1, 4, 1, 2, 1, 0, 0]
        #

