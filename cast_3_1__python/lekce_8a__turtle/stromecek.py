import turtle

zelva = turtle.Turtle()
zelva.left(90)
zelva.speed(0)
zelva.color("green")


def vetvicka(d):
    if d <= 10:
        return
    zelva.forward(d)
    zelva.left(30)
    vetvicka(d * 0.7)  # levá
    zelva.right(60)
    vetvicka(d * 0.7)  # pravá
    zelva.left(30)
    zelva.backward(d)


zelva.penup()
zelva.goto(0, -250)
zelva.pendown()

vetvicka(200)

turtle.exitonclick()
