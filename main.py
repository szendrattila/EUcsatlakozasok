"""
EUcsatlakozas.txt
Ausztria;1995.01.01
Belgium;1958.01.01
"""

class Eu:
    def __init__(self, sor):
        orszag, datum = sor.strip().split(";")
        self.orszag = orszag
        self.datum = datum
        self.ev = int(datum[:4])
        self.honap = int(datum[5:7])
        self.nap = int(datum[8:10])

lista = []
with open ("EUcsatlakozas.txt", encoding="latin2") as f:
    for sor in f:
        lista.append(Eu(sor))

#3. feladat: 2018 tagállamok száma
print(f"3. feladat:Eu tagállamok száma: {len(lista)} db")

#4. feladat: 2007ben csatlakozottak száma:
"""
szamlalo = 0
for sor in lista:
    if sor.ev == 2007:
        szamlalo += 1
print(f"4. feladat: 2007-ben {szamlalo} ország csatlakozott")
"""
szamlalo = len([sor for sor in lista if sor.ev == 2007])
print(f"4. feladat: 2007-ben {szamlalo} ország csatlakozott")
#5. feladat: magyarország csatlakozásának dátuma
"""

csatlakozas = ""
for sor in lista:
    if sor.orszag == "Magyarország":
        csatlakozas = sor.datum
print(f"magyarország csatlakozásának dátuma: {csatlakozas}")
"""
csatlakozas = [sor.datum for sor in lista if sor.orszag == "Magyarország"]
print(f"5. feladat magyarország csatlakozásának dátuma: {csatlakozas[0]}")

#6. feladat: májusban történt-e csatlakozás
"""
szamlalo = 0
for sor in lista:
    if sor.honap == 5:
        szamlalo += 1
if szamlalo > 0:
    print("5. feladat: Májusban volt csatlakozás")
else:
    print("5. feladat: Májusban nem volt csatlakozás")
"""
szamlalo = len([sor for sor in lista if sor.honap == 5])
if szamlalo > 0:
    print("6. feladat: Májusban volt csatlakozás")
else:
    print("6. feladat: Májusban nem volt csatlakozás")
#7. feladat : utolso tagállam
"""

utolso = ""
for sor in lista:
    if sor.datum > utolso:
        utolso = sor.datum
        utolso_sor = sor
print(f"7. feladat Az utolóljára csatlakozott ország: {utolso_sor.orszag}")
"""
utolsoorszag = max(lista, key=lambda x:x.datum).orszag
print(f"7. feladat Az utolóljára csatlakozott ország: {utolsoorszag}")
print("8. feladat statisztika:")
stat = dict()
for sor in lista:
    stat[sor.ev] = stat.get(sor.ev, 0) + 1
for kulcs, ertek in stat.items():
    print(f"        {kulcs} - {ertek} ország")
    




