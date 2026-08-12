class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # i am given n cars traveling to the same destination on a one lane highway
        # so essentianlly n cars on a one lane highway is like

        # [0 ---> n - 1]

        # position and speed are both of length n which correspond to the position of the ith car and the speed of ith car

        pairs = zip(position, speed)

        # we want to form car fleets with a stack
        # we should form groups for the cars 
        # let me think of the condition at which a fleet starts

        # a car fleet of multiple cars only forms if the position we are looking at is behind  another position and it is slower than the other one

        # ex: pairs = [(4, 2), (1, 2), (0, 1), (7, 1)]

        # we need to compute whether they will form a fleet by the target position

        # we can repersent each pair as part of a stack
        # we pop elements from the stack if their position is less the current position and their speed is == or less than the current as it will not join this fleet and form its own fleet 

        #if stack and stack[-1][0] > pair[0] and stack[-1][1] >=
        #stack = [(4,2), (1, 2)]
        pair = [(p, s) for p, s in zip(position, speed)]
        
        pair.sort(reverse=True)
        stack = []

        for p, s in pair: 
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
            



        

        
        