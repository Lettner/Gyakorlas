#with open('fuvar.csv', 'r', encoding = 'UTF-8') as forras:
forras=open('fuvar.csv', 'r', encoding='UTF-8-sig')
#lista=[]
fejlec = forras.readline()
#for sor in forras: 
#    lista.append(sor.strip().split(';'))  #append megtartja az adott sort, aktuális sor befűzése
lista=[sor.strip().replace(',','.').split(';') for sor in forras] #daráló sor for sor in itt készül egy lista változó amibe belekerül a forras txt és az első sor tipuson leszedjük a végződéseket, és ; mentén daraboljuk.
# 3. Hány utazás került feljegyzésre az állományban?
print(f'3. feladat: {len(lista)}')
#4. Határozza meg és írja ki a képernyőre a minta szerint, hogy a 6185-ös azonosítójú taxisnak mennyi volt a bevétele, és ez hány fuvarból állt?
bevetel=0
fuvarszam=0
for sor in lista:
    if sor[0]=='6185':
      bevetel=bevetel+float(sor[4])+float(sor[5])
      fuvarszam += 1
print(f'4. feladat: {fuvarszam} fuvar alatt {bevetel}$')
#5feladat Programjával határozza meg az állomány adataiból a fizetési módokat, majd összesítse, hogy az egyes fizetési módokat hányszor választották az utak során! Ezeket az eredményeket a minta szerint írja a képernyőre! A kiírás során a fizetési módok sorrendje bármilyen lehet.
#fizetesi_modok=[]
#for sor in lista:
#    fizmod=sor[6]
#    if fizmod not in fizetesi_modok:
#        fizetesi_modok.append(fizmod)
fizmodlista=[sor[6] for sor in lista]
fizmodok=set(fizmodlista)                   # halmaz létrehozása amibe a fizetési modokat indexelve felsoorljuk
for fizmod in fizmodok:
    darab=fizmodlista.count(fizmod)
    print(f'{fizmod}: {darab}')

#6feladat  Határozza meg és írja ki a képernyőre a minta szerint, hogy összesen hány km-t tettek meg a taxisok (1 mérföld 1,6 km)! Az eredményt két tizedesjegyre kerekítve jelenítse meg a képernyőn! 
osszestav=0
for sor in lista:
    osszestav += float(sor[3])
print(f'6. feladat{osszestav*1.6:.2f} km')

#7feladat Határozza meg és írja ki a képernyőre a minta szerint az időben leghosszabb fuvar adatait! Feltételezheti, hogy nem alakult ki holtverseny.
leghosszabb=0   # uj változo leghosszabb, ha a meglévő időtartam nagyobb mint az új változó akkor az uj változó egynelő lesz a meglévő időtartam sorral
for sor in lista:
    if int(sor[2]) > leghosszabb:
        leghosszabb = int(sor[2])
        taxi_id=sor[0]  # a ha függvénnybe uj változokkal megindexelve a sorokat kiiratjuk a éleghosszabbak adatait
        megtettut=sor[3]
        viteldij=sor[4]
print(f'Leghosszabb út: {leghosszabb} másodperc')
print(f'   Taxi azonosítója: {taxi_id}')
print(f'   Megtett távolság: {megtettut} km')
print(f'   Viteldíj: {viteldij} $')

#8feladat
with open('hibak.txt', 'w', encoding='utf-8') as hiba:
    print(fejlec)
    for sor in lista:
        if int(sor[2]) > 0 and float(sor[4]) > 0 and float(sor[3]) == 0:
            print(f'{sor[0]};{sor[1]};{sor[2]};{sor[3]};{sor[4]};{sor[5]};{sor[6]}')
