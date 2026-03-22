import turtle
from bouqet_data import bouquet_data # тут можна після from до bouqet_data додати 2 або 3 для виведення різних данних букетів

class Stem:

    def __init__(self, length=157, color="dark green"):
        self.length = length
        self.color = color

    def draw(self, t):
        t.color(self.color)
        t.pensize(5)
        t.forward(self.length)

class Leaf:

    def __init__(self, size=50, color="dark green"):
        self.size = size
        self.color = color

    def draw(self, t):
        t.color(self.color)
        t.fillcolor(self.color)
        t.pensize(2)
        t.begin_fill()
        t.right(45)
        t.circle(self.size, 90)
        t.left(90)
        t.circle(self.size, 90)
        t.right(45)
        t.end_fill()

class Petal:

    def __init__(self, size=60, color="red"):
        self.size = size
        self.color = color

    def draw(self, t):
        t.color(self.color)
        t.fillcolor(self.color)
        t.pensize(2)
        t.begin_fill()
        t.circle(self.size, 60)
        t.left(120)
        t.circle(self.size, 60)
        t.left(120)
        t.end_fill()


class Flower:

    def __init__(self, x, y, petal_color="red", petals_count=6, angle=90):
        self.x = x
        self.y = y
        self.petals_count = petals_count
        self.angle = angle

        self.stem = Stem(length=140)
        self.leaf = Leaf(size=35)
        self.petal = Petal(size=55, color=petal_color)

    def draw(self, t):
        t.penup()
        t.goto(self.x, self.y)
        t.pendown()

        t.setheading(self.angle)

        self.stem.draw(t)

        t.backward(self.stem.length * 0.5)

        t.setheading(self.angle - 45)
        self.leaf.draw(t)

        t.setheading(self.angle + 45)
        self.leaf.draw(t)

        t.setheading(self.angle)
        t.forward(self.stem.length * 0.5)

        for _ in range(self.petals_count):
            self.petal.draw(t)
            t.left(360 / self.petals_count)

def main():
    start_x = 0
    start_y = -250
    screen = turtle.Screen()
    screen.title("Букет")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    for angle, color, p_count in bouquet_data:

        flower = Flower(start_x, start_y, petal_color=color, petals_count=p_count, angle=angle)
        flower.draw(t)

    screen.exitonclick()

if __name__ == "__main__":
    main()