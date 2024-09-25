--2a
absoluto :: Int -> Int
absoluto x | x>=0 = x
           | x<0 = (-x)
--2b
maximoabs :: Int -> Int -> Int
maximoabs x y | absoluto x > absoluto y = x
              | otherwise = absoluto y
--2c
maximo3 :: Int -> Int -> Int -> Int
maximo3 x y z | x > y && x > z = x 
              | y > z = y
              | otherwise = z 
--2d 
algunoEs0 :: Int -> Int -> Bool
algunoEs0 x y | x == 0 || y == 0 = True
              | otherwise = False
--2e 
ambosSon0 :: Int -> Int -> Bool
ambosSon0 x y = x == 0 && y == 0 
--2f 
mismoIntervalo :: Int -> Int -> Bool
mismoIntervalo x y | x <= 3 && y <=3 = True
                   | x > 7 && y > 7 = True
                   | x > 3 && x <= 7&& y > 3 && y<= 7 = True
                   | otherwise = False
--2g
sumaDistintos :: Int -> Int -> Int -> Int
sumaDistintos x y z | x == y && x == z = x 
                    | x == y = x + z
                    | x == z = x + y
                    | y == z = y + x
                    | otherwise = x + y + z  
--2h
esMultiploDe :: Int -> Int -> Bool
esMultiploDe x y | mod x y  == 0 = True 
                 | otherwise = False
--2i
digitoUnidades :: Int -> Int
digitoUnidades x = mod x 10
--2j
digitoDecenas :: Int -> Int
digitoDecenas x = div (mod x 100) 10

--3
estanRelacionados :: Int -> Int -> Bool
estanRelacionados a b = mod a (absoluto b) == 0

--4 TUPLAS
--4a
prodInt :: (Float,Float) -> (Float,Float) -> Float
prodInt (a,b)(c,d) = a*c + b*d
--4b
todoMenor :: (Float,Float) -> (Float,Float) -> Bool
todoMenor (a,b)(c,d) = a < c && b < d 
--4c
distanciaPuntos :: (Float,Float) -> (Float,Float) -> Float
distanciaPuntos (a,b)(c,d) = sqrt((c-a)^2+(d-b)^2)
--4d
sumaTerna :: (Int,Int,Int) -> Int
sumaTerna (a,b,c) = a+b+c
--4e
sumarSoloMultiplos :: (Int,Int,Int) -> Int -> Int
sumarSoloMultiplos (a,b,c) n | mod a n == 0 && mod b n == 0 && mod c n == 0 = a + b + c
                             | mod a n == 0 && mod b n == 0 = a + b
                             | mod a n == 0 && mod c n == 0 = a + c
                             | mod b n == 0 && mod c n == 0 = b + c
                             | mod a n == 0 = a 
                             | mod b n == 0 = b
                             | mod c n == 0 = c
                             | otherwise = 0 
--4f
posPrimerPar :: (Int,Int,Int) -> Int 
posPrimerPar (a,b,c) | mod a 2 == 0 = 1
                     | mod b 2 == 0 = 2
                     | mod c 2 == 0 = 3
                     | otherwise = 4
--4g
crearPar :: t1 -> t2 -> (t1,t2)
crearPar a b = (a,b)
--4h
invertir :: (t1,t2) -> (t2,t1)
invertir (a,b) = (b,a)

--5
todosMenores :: (Int,Int,Int) -> Bool
todosMenores (a,b,c) = f a > g a && f b > g b && f c > g c 

f :: Int -> Int
f x | x <=7 = x^2
    | otherwise = 2*x-1 

g :: Int -> Int
g x | mod x 2 == 0 = div x 2
    | otherwise = 3*x+1

--6 bisiesto

--7 distanciaManhattan

--8 
comparar :: Int -> Int -> Int 
comparar a b | sumaUltimosDosDigitos a < sumaUltimosDosDigitos b = 1
             | sumaUltimosDosDigitos a == sumaUltimosDosDigitos b = 0
             | otherwise = -1


sumaUltimosDosDigitos :: Int -> Int
sumaUltimosDosDigitos x = mod x 10 + mod (div x 10) 10
