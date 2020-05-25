#név;első;utolsó;súly;magasság
# 0    1    2      3     4
#Jim Abbott;1989-04-08;1999-07-21;200;75

with open('balkezesek.csv', 'r', encoding='latin2') as f:
    fejlec = f.readline()    # első sor eldobjuk
    matrix = [sor.strip().split(';') for sor in f]

#3.feladat
print(f'3.feladat: {len(matrix)} sor található.')

#4feladat határozza meg a játékosok nevét és  testmagasságát centiben akik utoljára 1999 novemberében játszottak?
print('4. feladat:')
for sor in matrix:
    nev = sor[0]
    magassag = int(sor[4])*2.54
    utolso = sor[2][:7]  #az utolsó évből a 0:7 karaktertől számítva a pl:1990-10 igfogja beletenni a változóba
    if utolso =='1990-10':
        print(f'       {nev}, {magassag:.1f} cm')
        
#5.feladat kérjen be egy évszámot 1990<=évszám<=1999 feltételnek megfelelően?
print('5.feladat:')
while True:     # ha igaz a bekért szám tovább megy ha hamis akkor hibás adat üzenet, minden inputnál hasonlóan
    bekeres = int(input('Kérek egy 1990 és 1999 közötti számot: '))
    if 1990<=bekeres<=1999:    # a bekért szám 1990 és 1999 között fogja ellenőrizni és utána leáll breakel
        break
    else:
        print('Hibás adat!', end=" ")  # end=" " egymás mellé irj a hibás adatot és a nomál szövget
        
#6feladat mennyi az átlagsulya a játékosnakakit bekért az előző feladatban, feltételezheti hogy az első és utolsó pályára lépés dátuma között minden évben játsuottak
atlagsulyok = 0
db = 0
for sor in matrix:
    elso = int(sor[1][:4])   #első évből csak az évet vesszük igy az első sor 0:4 karakterig snézve
    utolso = int(sor[2][:4])
    suly = int(sor[3])
    if elso<=bekeres<=utolso:   # elso és utolsó évek között van azaz nagyobb mint az elso és kisebb mint az utolsó év a bekért szám akkor átlagot számol
        atlagsulyok = atlagsulyok + int(suly)  # atlag számítás, változók bevezetése atlagsulyok,db
        db += 1
atlag = atlagsulyok/db
print(f'6. feladat: {atlag:.2f} font') # :.2f 2 tizedesjegyre kerekítés
    

        