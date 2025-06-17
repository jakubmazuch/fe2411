from clovek import Clovek

# vytvářím osoby
karel = Clovek("Karel", "Novák", 33)
cyril = Clovek("Cyril", "Nový", 27)
jana = Clovek("Jana", "Zelená", 22)
eva = Clovek("Eva", "Kolínská", 36)
kai = Clovek("Kai", "Janů", 78)

# seznamka
karel.pridej_kamose(cyril)
karel.pridej_kamose(eva)
karel.pridej_kamose(kai)
jana.pridej_kamose(eva)
eva.pridej_kamose(jana)
kai.pridej_kamose(cyril)
kai.pridej_kamose(eva)

# představování
karel.predstav_se()
cyril.predstav_se()
jana.predstav_se()
eva.predstav_se()
kai.predstav_se()
