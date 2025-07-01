# bankovky
b5000 = 5000
b2000 = 2000
b1000 = 1000
b500 = 500
b200 = 200
b100 = 100
b50 = 50
b20 = 20
b10 = 10
b5 = 5
b2 = 2
b1 = 1

# vybírám peníze
m = int(input("Zadejte částku k výběru: "))

# výdej
n5000 = m//b5000
m = m - n5000 * b5000
n2000 = m//b2000
m = m - n2000 * b2000
n1000 = m//b1000
m = m - n1000 * b1000
n500 = m//b500
m = m - n500 * b500
n200 = m//b200
m = m - n200 * b200
n100 = m//b100
m = m - n100 * b100
n50 = m//b50
m = m - n50 * b50
n20 = m//b20
m = m - n20 * b20
n10 = m//b10
m = m - n10 * b10
n5 = m//b5
m = m - n5 * b5
n2 = m//b2
m = m - n2 * b2
n1 = m//b1
m = m - n1 * b1
# výpis
print("Počet bankovek 5000 Kč:", n5000)
print("Počet bankovek 2000 Kč:", n2000)
print("Počet bankovek 1000 Kč:", n1000)
print("Počet bankovek 500 Kč:", n500)
print("Počet bankovek 200 Kč:", n200)
print("Počet bankovek 100 Kč:", n100)
print("Počet bankovek 50 Kč:", n50)
print("Počet bankovek 20 Kč:", n20)
print("Počet bankovek 10 Kč:", n10)
print("Počet bankovek 5 Kč:", n5)
print("Počet bankovek 2 Kč:", n2)
print("Počet bankovek 1 Kč:", n1)