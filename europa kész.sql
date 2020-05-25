-- 1.Írassa ki európa északi országait!
SELECT Orszag
FROM `europa_europa`
WHERE Egtaj = 'észak európa'


-- 2. Írassa ki európa déli országait, abc szerinti sorrendbe!
SELECT Orszag FROM `europa_europa` WHERE Egtaj = 'dél' ORDER BY Orszag ASC 



-- 3. Adja meg a 10 milliónál nagyobb lélekszámú országokat!
SELECT Orszag
FROM `europa_europa`
WHERE Lakossag > '10'


-- 4. Melyik a legnagyobb lélekszámú ország?
SELECT Orszag FROM `europa_europa` ORDER BY Lakossag DESC LIMIT 1 


-- 5. Melyik a legnagyobb területű nyugati ország?
SELECT Orszag
FROM `europa_europa`
WHERE Egtaj ='nyugat' ORDER BY Terulet DESC LIMIT 1


-- 6. Melyik a legkisebb lélekszámú keleti ország?
SELECT Orszag FROM `europa_europa` WHERE Egtaj ='kelet' ORDER BY Lakossag ASC LIMIT 1 


-- 7. Melyik ország fővárosa Vilnius?
SELECT Orszag
FROM `europa_europa`
WHERE Fovaros = 'Vilnius'


-- 8. Melyik az 5-ik legnagyobb területű ország?
SELECT Orszag
FROM `europa_europa`
ORDER BY Terulet DESC LIMIT 4,1


-- 9. Melyik a három legkisebb területű ország?
SELECT Orszag
FROM `europa_europa`
ORDER BY Terulet ASC LIMIT 3


-- 10. Melyik a három legkisebb területű déli ország?
SELECT Orszag
FROM `europa_europa`
WHERE Egtaj = 'dél' ORDER BY Terulet ASC LIMIT 3

-- 11. Mely országokban kevesebb a lakosság létszáma 5 milliónál?
SELECT Orszag
FROM `europa_europa`
WHERE Lakossag < '5'


-- 12. Mekkora Hollandia területe?
SELECT Terulet FROM `europa_europa` WHERE Orszag = 'hollandia' 


-- 13. Adja meg az országok népsűrűségét!
SELECT Orszag,Lakossag*1000000/Terulet FROM `europa_europa` 


-- 14. Mennyi Málta népsűrűsége?

SELECT Orszag,Lakossag*1000000/Terulet FROM `europa_europa` WHERE Orszag = 'Málta' 
-- 15. Melyik ország népsűrűsége a legnagyobb?

SELECT Orszag,Lakossag*1000000/Terulet FROM `europa_europa` ORDER BY Orszag DESC LIMIT 1 