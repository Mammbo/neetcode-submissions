class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # so i am give an int array nums
        # i am given an int k
        # this just the amount of values to return

        # returned output can be in any order but the return the value must be  an array of the most frequent elements

        # i need an O(n) solution 

        # numbers can be neg or pos, this doesnt matter though we are just looking at the count


        # k == 1 up to the number of distinct elements:
        # so in the case of every element being unique, k can be the length of the array, so we can always make a set boundary for our frequency list, making the space of it O(N)

        # i think the solution here is bucket sort


        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # we need to increment count now 
        for n in nums: 
            count[n] = 1 + count.get(n, 0)
        
        for c in count:
            freq[count.get(c)].append(c)

        ans = []

        for b in range(len(freq) -1, -1, -1):
            for val in freq[b]:
                ans.append(val)
        
        return ans[:k]






        