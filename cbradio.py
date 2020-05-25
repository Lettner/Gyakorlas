#Ora;Perc;AdasDb;Nev
# 0   1     2     3
#6;    0;   2;  Laci


with open ('cb.txt','r', encoding='utf-8-sig') as f:
    elsosor = f.readline()
    matrix = [sor.strip().split(';') for sor in f ]

#3.feladat
print (f'3. feladat: Bejegyzések száma: {len(matrix)} db')

#4.feladatDöntse el és írja ki a képernyőre a minta szerint, hogy található-e a naplóban olyan
#bejegyzés, amely szerint a sofőr egy percen belül pontosan 4 adást indított! A keresést ne
#folytassa, ha az eredményt meg tudja határozni!
adas = [sor for sor in matrix if sor[2] == '4']

while True:    
    if (len(adas) > 0 ):
        print(f'4. feladat: Volt négy adást inditó sofőr. ')
    else:
        print(f'4. feladat: Nem volt négy adást indító sofőr. ')
    break

#5.feladat Kérje be a felhasználótól egy sofőr nevét, majd határozza meg a sofőr által indított hívások
#számát a napló bejegyzéseiből! Az eredményt a minta szerint írja ki a képernyőre! Ha olyan
#sofőr nevét adja meg a felhasználó, aki nem szerepel a naplóban, akkor a „Nincs ilyen nevű
#sofőr!” mondat jelenjen meg!
nev = input('5. feladat: Kérek egy nevet: ')
db = 0
for sor in matrix:
    if (sor[3] == nev):
        db = db + int(sor[2])
if (db == 0):
    print (f'Nincs ilyen nevű sofőr.')
else:
    print(f' {nev} {db}x használta a CB-rádiót.')

#6.feladatKészítsen AtszamolPercre azonosítóval egész típusú értékkel visszatérő metódust vagy
#függvényt, ami a paraméterként megadott óra- és percértéket percekre számolja át! Egy óra
#60 percből áll. Például: 8 óra 5 perc esetén a visszatérési érték: 485 (perc).
def AtszamolPercre (o, p):
    return p + o * 60

#7.feladat Készítsen szöveges állományt cb2.txt néven, melybe a forrásállományban található
#bejegyzéseket írja ki új formátumban! Az órákat és a perceket percekre számolja át az előző
#feladatban elkészített metódus (függvény) hívásával! Az új állomány első sorát és
#az adatsorokat a minta szerint alakítsa ki!    
with open('cb2.txt','w') as f2:
    f2.write('Kezdes;Nev;AdasDb\n')
    for sor in matrix:   
        percek = AtszamolPercre(sor[0], sor[1])
        text = f'{percek};{sor[3]};{sor[2]}\n'
        f2.write(text)
        
#8.feladatHatározza meg és írja ki a minta szerint a sofőrök számát a forrásállományban található
#becenevek alapján! Feltételezheti, hogy nincs két azonos becenév.
soforok = [ matrix[x][3] for x in  range(len(matrix))].count(sor[3])
print(f'8. feladat: Sofőrök száma: { soforok } fő' )

#9.feladatHatározza meg a legtöbb adást indító sofőr nevét! A sofőr neve és az általa indított hívások
#száma a minta szerint jelenen meg a képernyőn!
maxi = max( [(int(sor[2]), x) for x, sor in enumerate(matrix)])[1]
print('9. feladat: A legtöbb adást indító sofőr' )
print(f'        Név: {matrix[maxi][3]} ')
print(f'        Adások száma: {matrix[maxi][2]} alkalom')

    
    
