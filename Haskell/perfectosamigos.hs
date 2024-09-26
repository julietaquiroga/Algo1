
{-
Ejercicio 9. Implementar la funci´on divisoresPropios :: Int ->[Int]
problema divisoresPropios (n: Z) : seq⟨Z⟩ {
requiere: {n > 0}
asegura: {res es la lista de divisores propios de n, ordenada de menor a mayor}
-}

divisoresPropios :: Int -> [Int]
divisoresPropios 0 = []
divisoresPropios n = reverso (divisores (aux n) n)

divisores :: [Int] -> Int -> [Int]
divisores [] d = []
divisores (x:xs) d | mod d x == 0 = x : divisores xs d
                     | otherwise = divisores xs d
aux :: Int -> [Int]
aux 1 = []
aux n = n-1 : aux (n-1)

reverso :: (Eq t) => [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]
{- 
Ejercicio 10. Implementar la funci´on sonAmigos :: Int ->Int ->Bool
problema sonAmigos (n,m: Z) : Bool {
requiere: {n > 0}
requiere: {m > 0}
requiere: {m ̸= n}
asegura: {res = True ⇔ n y m son n´umeros amigos}
-}
sonAmigos :: Int -> Int -> Bool
sonAmigos n s = sumatoria (divisoresPropios n) == s && sumatoria (divisoresPropios s) == n

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

{-
Ejercicio 11. Implementar la funci´on losPrimerosNPerfectos :: Int ->[Int]
problema losPrimerosNPerfectos (n: Z) : seq⟨Z⟩ {
requiere: {n > 0}
asegura: {res es la lista de los primeros n n´umeros perfectos, de menor a mayor}
}
Por cuestiones de tiempos de ejecuci´on, no les recomendamos que prueben este ejercicio con un n > 4.
-}
losPrimerosNPerfectos :: Int -> [Int]
losPrimerosNPerfectos 0 = []
losPrimerosNPerfectos n = reverso (encontrarPerfectos n 1 [])

esPerfecto :: Int -> Bool
esPerfecto n = sumatoria (divisoresPropios n) == n 

encontrarPerfectos :: Int -> Int -> [Int] -> [Int]
encontrarPerfectos 0 _ encontrados = encontrados  
encontrarPerfectos n a encontrados | esPerfecto a = encontrarPerfectos (n-1) (a + 1) (a : encontrados)
                                   | otherwise = encontrarPerfectos n (a +1) encontrados 



{-
Ejercicio 12. Implementar la funci´on listaDeAmigos :: [Int] ->[(Int,Int)]
problema sonAmigos (lista: seq⟨Z⟩) : seq⟨Z × Z⟩ {
requiere: {Todos los n´umeros de lista son mayores a 0}
requiere: {Todos los n´umeros de lista son distintos}
asegura: {res es una lista de tuplas sin repetidos, que contienetuplas de dos n´umeros donde esos dos n´umeros
pertenecen a lista y son amigos}
asegura: {|res| es la cantidad de tuplas de dos n´umeros amigos que hay en lista. Consideraremos que la tupla (a, b)
(con a y b pertenecientes a Z) es igual a la tupla (b, a) para contar la cantidad de tuplas.-}

listaDeAmigos:: [Int] -> [(Int,Int)]
listaDeAmigos [] = []
listaDeAmigos lista = eliminarRepetidos (listaDeAmigosAux lista)

listaDeAmigosAux :: [Int] -> [(Int,Int)]
listaDeAmigosAux [] = []
listaDeAmigosAux (x:xs) = (amigos x xs ++ listaDeAmigosAux xs )



amigos :: Int -> [Int] -> [(Int,Int)]
amigos n [] = []
amigos n (x:xs) | sonAmigos n x = (n,x) : amigos n xs
                | otherwise = amigos n xs

eliminarRepetidos :: (Eq t) => [(t,t)] -> [(t,t)]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos ((x,y):xs) | estaContenido (x,y) xs == False = (x,y) : eliminarRepetidos xs
                             | otherwise = eliminarRepetidos xs

estaContenido :: (Eq t) => (t,t) -> [(t,t)] -> Bool
estaContenido n [] = False
estaContenido (a,b) ((x,y):xs) | a == x && b == y = True
                               | a == y && b == x = True
                               | otherwise = estaContenido (a,b) xs
