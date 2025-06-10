import turtle

# Vytvářím okno a želvu
okno = turtle.Screen()
zelva = turtle.Turtle()


def ctverec(velikost):
    for _ in range(4):
        zelva.forward(velikost)
        zelva.right(90)


def nakresliGrid(radky, sloupce, velikost):
    for r in range(radky):
        for s in range(sloupce):
            ctverec(velikost)
            zelva.penup()
            zelva.forward(velikost)
            zelva.pendown()
        zelva.penup()
        zelva.backward(velikost * sloupce)
        zelva.right(90)
        zelva.forward(velikost)
        zelva.left(90)
        zelva.pendown()


zelva.penup()
zelva.goto(-200, 200)
zelva.pendown()

# Nastavuji vzhled
zelva.shape("turtle")
zelva.color("blue")
zelva.pensize(4)
zelva.speed(20)

pocetKroku = 50

nakresliGrid(6, 6, 50)

turtle.exitonclick()
