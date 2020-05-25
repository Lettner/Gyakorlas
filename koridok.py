#csapat;           versenyzo;   eletkor;   palya;           korido;   kor
#Versenylovak;  Fürge Ferenc;     29;   Gran Prix Circuit;  00:01:11;  1
#    0                1            2          3                 4      5

with open('autoverseny.csv','r', encoding='utf-8-sig') as f:
    fejlec = f.readline()
    matrix = [sor.strip().split(';') for sor in f]
    
#3.feladat
print(f'3. feladat: {len(matrix)}')

#4.feladat
def ido(t):                #a kettős pont által elválasztott időpontból készítettünk egy másodperc időt csináltunk egy óra perc másodperc változót külön, amit egy mp nevű változóvl összegeztünk
    ora = int(t[0:2])
    perc = int(t[3:5])
    masodperc = int(t[6:8])
    mp = ora*3600 + perc*60 + masodperc
    return(mp)
    
res = [sor[4] for sor in matrix if sor[1] == 'Fürge Ferenc' and sor[5]=='3' and sor[3]=='Gran Prix Circuit']
print(f'4. feladat: {ido(res[0])} másodperc')

#5.feladat
print('5. feladat:')
nev = input('Kérem egy versenyző nevét: ')

#6.feladat
ido_str = ''
mini = 2**32
palya = ''
for sor in matrix:
    korido = ido(sor[4])
    if sor[1] == nev and korido < mini:
        mini = korido
        palya = sor[3]
        ido_str = sor[4]
        
if palya == '':
    print('Nics ilyen versenyző')
else:
    print(f'6.feladat {palya}, {ido_str}')

        
    