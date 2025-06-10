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
        zelva.goto(-300, 300 - velikost*(r+1))
        zelva.pendown()


zelva.penup()
zelva.goto(-300, 300)
zelva.pendown()

# Nastavuji vzhled
zelva.shape("turtle")
zelva.color("blue")
zelva.pensize(2)
zelva.speed(0)


velikostCtverecku = int(input("Velikost čtverečku: "))
pocetRadku = int(input("Počet řádků: "))
pocetSloupcu = int(input("Počet sloupců: "))

nakresliGrid(pocetRadku, pocetSloupcu, velikostCtverecku)

turtle.exitonclick()
