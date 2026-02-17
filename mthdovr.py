class vehicle:
    def move(self):
        print("vehicle is moving")

class car(vehicle):
    def move(self):print("driving on the road")

class bicycle(vehicle):
    def move(self):
        print("pedaling on the road")
c = car()
c.move()
b = bicycle()
b.move()        