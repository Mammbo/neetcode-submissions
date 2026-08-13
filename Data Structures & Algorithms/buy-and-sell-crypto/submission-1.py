class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # i am given an integer of prices called neetcoin 
        # where the price of neetcoin on a given day is given by prices[i]

        # okay i am just given an array 
        # and i need to find the winodw in which it is the best time to sell 
        # and the difference in prices that day is the profit


        # sliding window of variable size starting from 0 moving to the end of the array
        # i shift the left pointer when right is smaller than left 
        # i take the max each time right is bigger than left 
        # keep doing that till it is profitable

        left = 0 
        max_profit = 0 
        
        for right in range(len(prices)):   

            while prices[left] > prices[right]: 
                left += 1

            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit) 

        return max_profit 
            

        