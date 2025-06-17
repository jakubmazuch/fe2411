from clovek import Clovek

# vytvářím osoby
karel = Clovek("Karel", "Novák", 33)
cyril = Clovek("Cyril", "Nový", 27)
jana = Clovek("Jana", "Zelená", 22)

# seznamka
karel.kamos = cyril
cyril.kamos = jana

# představování
karel.predstav_se()
cyril.predstav_se()
