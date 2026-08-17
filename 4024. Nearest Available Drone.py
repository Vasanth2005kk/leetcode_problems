class Solution:
        def nearestDrone(self, drones: list[list[int]], target: list[int]) -> int:
            n =  len(drones)
            mid = 2147483647
            midindex = -1
            for i in range(n):
                d =  abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1])
                print(d)
                if mid > d and d <= drones[i][2]:
                    mid = d
                    midindex = i

            return midindex
                    