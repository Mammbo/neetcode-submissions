class Solution:
    def isValid(self, s: str) -> bool:

        # i am given a string s where i have the following characters of brackets (various opening and closing)

        # rules
        # every open bracket is closed by the same type of closing bracket
        # open brackets are closed in the correct order
        # every close bracket has the same open bracket 

        # return if this is true

        # i guess a couple edge cases if the length modulos 2 is not 0 then it will be false since it is uneven ( whether it is 1 or 51):

        # now we need to figure out how to process the string to do this check 
        # i think two pointers seems like a perfectly valid solution here with O(n) time complexity 
        # i dont think it is because of the case where ()[]{} is a valid solution. 

        # put all opening brackets on the stack and once a closing bracket comes up pop an element of the stack compare and if they dont match return false else continue
        # characters are only brackets

        stack = []
        brackets = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        if len(s) % 2 != 0: 
            return False

        for i in range(len(s)):
            if s[i] in brackets:
                if stack:
                    bracket = stack.pop()
                    if brackets[s[i]] != bracket:
                        return False
                else: 
                    return False
            else: 
                stack.append(s[i])
                
        # to check if the stack elements got all popped off
        return not stack 

        

            