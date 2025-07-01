prazdnyRetezec = ''
jazyk = 'Python'
zprava = 'Můj kámoš mi řekl: \n"Python je super!"'
viceRadku = '''Více
řádku'''

print(jazyk + zprava)
print(viceRadku)

print(bool(prazdnyRetezec), len(prazdnyRetezec))
print(bool(jazyk), len(jazyk))

print(jazyk[0])

print((jazyk + ", ") * 20)
