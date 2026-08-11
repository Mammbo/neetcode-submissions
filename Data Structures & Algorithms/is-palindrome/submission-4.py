class Solution:
    def isPalindrome(self, s: str) -> bool:
        # so i am given a string (probably have to iterate over it)
        #return true if it is a palindrome 
        # a palindrome is a string that reads the same forward and backward
        # it is case-insenstivie so i should .lower the whole string
        # it ignores all other non alpha numerica characters
        # for this i will have to use two pointers
        # s is made up of only printabel ascii chars 
        # s.length <= 1000 chars 
        # s = "Was it a car or a cat I saw?"
        # 
        newS = s.lower().strip()
        left = 0  
        right = len(newS) - 1 

        while left < right:
            if not newS[right].isalnum():
                right -= 1
            elif not newS[left].isalnum():
                left += 1
            elif newS[right] != newS[left]:
                return False
            else: 
                right -= 1
                left += 1
        return True