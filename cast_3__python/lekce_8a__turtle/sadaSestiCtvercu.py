import turtle


def ctverec(zelva, velikost):
    for _ in range(4):
        zelva.forward(velikost)
        zelva.right(90)


# Vytvářím okno a želvu
okno = turtle.Screen()
pero = turtle.Turtle()

pero.penup()
pero.goto(-200, 200)
pero.pendown()

# Nastavuji vzhled
pero.shape("turtle")
pero.color("green")
pero.pensize(5)
pero.speed(1)

pocetKroku = 50

for _ in range(6):
    ctverec(pero, pocetKroku)
    pero.penup()
    pero.forward(pocetKroku)
    pero.pendown()


turtle.exitonclick()
