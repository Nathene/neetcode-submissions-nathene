# class Solution:
#     def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        time_to_reach = [0.0] * (target + 1)
            
        for p, s in zip(position, speed):
            time_to_reach[p] = (target - p) / s
        
        fleets = 0
        slowest_car_in_fleet = 0.0
        
        # Iterate from the car closest to the target backwards
        for i in range(target, -1, -1):
            current_time = time_to_reach[i]
            if current_time > slowest_car_in_fleet:
                # This car is slower than the fleet ahead, so it starts a new fleet
                fleets += 1
                slowest_car_in_fleet = current_time
                
        return fleets



        pairs = [ [p, s] for p, s in zip(position, speed) ]

        pairs.sort(reverse=True)

        stack = []

        for p, s in pairs:
            reach = (target - p) / s
            if stack and reach <= stack[-1]:
                continue
            else:
                stack.append(reach)
        
        return len(stack)

# [ 1, 4 ]
# [ 3, 2 ]

# [ 4, 1 ] p
# [ 2, 3] s

# 10 - 4 / 1 = 6
# 10 - 2 / 3 = 

# 1 car pool