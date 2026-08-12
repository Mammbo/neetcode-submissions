class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # i am given an array of strings tokens 
        # it repersents # A VALID expression 
        # so i dont have to do error handling for this part 

        # i need to return an int that evaluates that expression 

        # rules: 
        # operands may be int or results of operations 
        # operators are the standard 4
        # assume integer division

        # just looking at the example and seeing how i would process that expression  it seems i have to use a stack that has only numbers on it 

        operators = {"+", "-", "*", "/"}
        stack = []

        for i in range(len(tokens)):
            if tokens[i] in operators: 
                # since it is guaranteed valid i dont have to do guard checks
                intB = int(stack.pop())
                intA = int(stack.pop())

                if tokens[i] == "+": 
                    value = intA + intB
                    stack.append(value)
                elif tokens[i] == "-": 
                    value = intA - intB
                    stack.append(value) 
                elif tokens[i] == "*": 
                    value = intA * intB
                    stack.append(value)
                else:
                    value = intA / intB
                    stack.append(value)
            else: 
                stack.append(tokens[i])
        return int(stack.pop())

