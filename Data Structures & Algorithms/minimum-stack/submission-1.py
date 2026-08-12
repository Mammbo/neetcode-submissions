class MinStack:
    # design a stack class that does these operations
    # i think the biggest probably with this is the get min operation 
    # it wants everything to run in O(1) time 

    # iterating through the stack for min would be O(n)
    # to optimize it we can store a value in a variable
    # this wouldnt work because if the min is at the end and gets popped off we lose the next min 

    # we can use a hashmap to store the values
    # i think this would require sorting 
    # i think this is all not going to work 
    # we could just store the cmin at each values for O(1) lookup
    # storing the cmin at each point would allow us to do a peek and look at the current min at that point in the stack resulting in O(1) lookup
    
    # pop top and getmin will get called on nonempty stack
    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        
        if self.min_stack:
            cmin = min(self.getMin(), val)
            self.min_stack.append([val, cmin])
        else: 
            self.min_stack.append([val, val])

    def pop(self) -> None:
        self.min_stack.pop()
        

    def top(self) -> int:
        return self.min_stack[-1][0]
        

    def getMin(self) -> int:
        return self.min_stack[-1][1]

    [[-2, -2], [0, -2]]
