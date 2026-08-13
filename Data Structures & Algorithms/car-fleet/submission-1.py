class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # so i am given n cars traveling to the same destination on a one lane highway, THEY CAN NOT PASS EACH OTHER
        #i am given two arrays of integers postiion and spped both matching to the cars
        # the destination is at position target miles

        # a care can not pass another car it can only catch up to it and form a car fleet, so they become apart of the same position
        # a single car is a car fleet, meaning if cars meet we can treat them as 1 car

        # return total number of car fleets that will arrive at desintion
        # input is 100,000
        # positions are unique
        
        # so to process this data we have to see if a car arrives at the destination at the same time or less to see if it becomes a car fleet
        # we can take the cars current position subtract it from the target divide it by the speed, and see if the time reaches the destination in the same time or less
        # i think the best way to process this data is processing the cars as they come in and check this information 
        # we can do it as a stack
        # and we should process the cars by their position towards the target 

        # if we want to check if a car forms a fleet we have to make sure its elements are properly accessed between two cars
        # append speeds to the sop of the stack
        # we can auto append to the stack and then do the check because we want the car fleets to form at the latest possible position
        # if we got rid of the first car we would have to do extra calculations to see if it forms with the second fleet etc
        # there will at least be one car in the stack
        # the target desitnion will be at least 1
        #the speed will at least be 1 allowing us to us division
        #
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        stack = []

        for i in range(len(pairs)):
            time = (target - pairs[i][0]) / pairs[i][1]
            stack.append(time)
            while len(stack) >= 2 and stack[-1] <= stack[-2]: 
                stack.pop()
            
        return len(stack)

    # run through an example 
    # pairs = [(4, 2), (1, 2), (0, 1), (7,1)]
    # pairs sorted reverse = [(7,1), (4, 1), (1, 2) (0, 1)]
    #stack = [3, 4.5, 10]

    # from 0 --> 3
    # time = (10 - 0)/ 1 == 10

