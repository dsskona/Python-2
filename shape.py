class shape:
    def draw(self):
        print("Drawing a shape")

class circle(shape):
    def draw(self):
        print("Drawing a circle")

class rectangle(shape):
    def draw(self):
        print("Drawing a rectangle")
c = circle()
c.draw()
r = rectangle()
r.draw()        