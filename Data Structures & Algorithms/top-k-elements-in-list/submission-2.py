class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # given an integer aray nums, and an integer k, return the k most frequent elements
        # k means how many elements to return, and we get the results back in ascending order 
        # since we need to track frequency using a hashmap would good 
        # so at least for step 1 we should build the hashmap and the frequencies of each element
        # after we build our hash map we need to return the k most frequenc elements
        # k is for distinct elements
        # nums can be from -1000 to 1000 doesnt matter we only care about frequency

        frequency = {} 
        for num in nums: 
            if num not in frequency: 
                frequency[num] = 0
            frequency[num] = frequency.get(num, 0) + 1

        
        res = []
        while k > 0: 
            res.append(max(frequency, key=frequency.get))
            del frequency[max(frequency, key=frequency.get)]
            k -= 1
        return res
        
        