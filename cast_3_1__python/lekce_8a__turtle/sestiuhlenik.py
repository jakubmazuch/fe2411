import turtle

# Vytvářím okno a želvu
okno = turtle.Screen()
zelva = turtle.Turtle()

# Nastavuji vzhled
zelva.shape("turtle")
zelva.color("green")
zelva.pensize(5)
zelva.speed(1)

# Kreslení
for _ in range(6):
    zelva.forward(100)
    zelva.right(60)


turtle.done()
