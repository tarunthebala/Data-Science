"""
Author: Tarun Balasubramaniam
Assignment Title: SimpleCar class
Assignment Description: Create and instantiate a simpleCar object
Due Date: 8/26/2026
Date Created: 8/26/2026 
Date Last Modified: 8/26/2026
"""
class SimpleCar:
    def __init__(self, dist = 0):
        self.dist = dist

    def drive(self, dist): #--> adds the distance to existing miles
        self.dist += dist
    def reverse(self, dist): #--> subtracts the distance from existing miles
        self.dist -= dist
    def get_odometer(self): #--> returns miles on odometer
        return self.dist
    def honk_horn(self): #--> prints 'beep beep' as the horn sound
        print("beep beep")
    def report(self): #--> prints 'Car has driven: {self.miles} miles'
        print(f"Car has driven: {self.dist} miles")

if __name__ == '__main__':
    #DA
    car = SimpleCar()

    #input
    forward = int(input())
    back = int(input())

    #process
    car.drive(forward)
    car.reverse(back)

    #output
    car.honk_horn()
    car.report()

    #assumptions
    #user only inputs integers
