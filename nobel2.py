#év;típus;keresztnév;vezetéknév
# 0   1       2           3
#2017;fizikai;Rainer;Weiss
with open('nobel.csv','r', encoding='utf-8-sig') as f:
    fejlec = f.readline()
    matrix = [sor.strip().split(';') for sor in f]
    
#3 feladat irja ki a képernyőre milyen tipusu dijat kapott Rathur B. McDonald
tipus=''
for sor in matrix:
    if sor[2]=='Arthur B.' and sor[3]=='McDonald':
        tipus=sor[1]
print(f'3.feladat: {tipus}')

#4.feladat ki kapott 2017 ben irodalmi dijat
irodalmi = ''
for sor in matrix:
    if sor[0]=='2017' and sor[1]=='irodalmi':
        irodalmi=sor[2]+ ' ' +sor[3]
print(f'4.feladat: {irodalmi}')

#5.feladat mely szervezetek kaptak béke Nobel dijat 1990 től napjainkig?
print(f'5.feladat:')
for sor in matrix:
    if sor[3]=='' and int(sor[0]) > 1989 and sor[1]=='béke':
        print(f'         {sor[0]}: {sor[2]}')

#6.feladat Curie több tagja kapott dijat, melyik évben és a család melyik tagja kapott díjat?
print(f'6.feladat:')
for sor in matrix:
    keresztnev = sor[2]
    vezeteknev = sor[3]
    ev = int(sor[0])
    tipus = sor[1]
    if 'Curie' in vezeteknev: # a curie nevet keressük a vezetéknevekben
        print(f'         {ev}: {keresztnev} {vezeteknev}({tipus})')
        
#7.feladat melyik tipusú dijból hány darabot osztottak ki a nobel dij történelme során?
print(f'7.feladat:')
dijak=[sor[1]for sor in matrix]
for tipus in set(dijak):      # statisztika, a dijakat egy listába tesszük utána egy ciklusba olvasva nem a sorból hanem a tipusból indul és a  halmazzá alakított dijakon megy át
    darab = dijak.count(tipus)   # ezután egy uj darab változóba dijak nak a típus válzotóit megszámláljuk hány darab tipus volt
    print(f'         {tipus:20} {darab:3}db')   # formázás :20 :3 ezáltal szépen egymás mellett lesz 

#8.feladat hozzonol létre orvosi.txt állományt ami a összes kiosztott orvosi nobel dijat tartalmazza, a minta szerint?
with open('orvosi1.txt','w', encoding='UTF-8') as orvosi1:   # fájlba írás megadunk egy új fájlt amibe irni fogunk
    for sor in sorted(matrix):         # orvosi típusuakat bele irjuk egy fájlba, név és év szerint
        tipus = sor[1]
        keresztnev = sor[2]
        vezeteknev = sor[3]
        ev = int(sor[0])
        if tipus =='orvosi':
            print(f'{ev}:{keresztnev} {vezeteknev}', file=orvosi1)  # file=orvosi1 ez amikor bele printeli a fájlba amit szeretnénk

    