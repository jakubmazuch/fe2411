text = input("Zadej text: ").strip().lower()
obsahuje = "it step" in text or "step it" in text
print(obsahuje)
