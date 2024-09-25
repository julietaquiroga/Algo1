--guia mas importante de todas RECURSION SOBRE LISTAS
--Ejercicio 1.1
longitud :: (Eq t) => [t] -> Int
longitud [] = 0 
longitud [x] = 1
longitud (x:xs) = 1 +longitud xs
--Ejercicio 1.2
ultimo :: (Eq t) => [t] -> t
ultimo [x] = x
ultimo (x:xs) = ultimo xs
--Ejercicio 1.3
principio :: (Eq t) => [t] -> [t]
principio [] = []
principio (x:xs) | xs == [] = []
                 | otherwise = x : principio xs
--Ejercicio 1.4
reversoA :: (Eq t) => [t] -> [t]
reversoA [] = []
reversoA (x:xs) = ultimo (x:xs) : reversoA(principio(x:xs))

reverso :: (Eq t) => [t] -> [t]
reverso [] = []
reverso (x:xs) = reverso xs ++ [x]
--Ejercicio 2.1
pertenece :: (Eq t) => t -> [t] -> Bool
pertenece _ [] = False
pertenece y (x:xs) | y ==x = True
                   | otherwise = pertenece y xs
--Ejercicio 2.2
todosIguales :: (Eq t) => [t] -> Bool
todosIguales [] = True
todosIguales [x] = True
todosIguales (x:y:xs) = x == y && todosIguales (y:xs) 
--Ejercicio 2.3
todosDistintos :: (Eq t) => [t] -> Bool
todosDistintos [] = True
todosDistintos [x] = True
todosDistintos (y:x:xs) = x/= y && todosDistintos (x:xs) && todosDistintos (y:xs)

--otra forma 
todosDistintosB:: (Eq t) => [t] -> Bool
todosDistintosB [] = True
todosDistintosB [x,y] = x/=y
todosDistintosB (x:xs) | pertenece x xs = False
                       | otherwise = todosDistintosB xs

--Ejercicio 2.4
hayRepetidos :: (Eq t) => [t] -> Bool
hayRepetidos [x] = False
hayRepetidos (x:xs) | pertenece x xs = True
                    | otherwise = hayRepetidos xs
--Ejercicio 2.5
quitar :: (Eq t) => t -> [t] ->[t]
quitar _ [] = []
quitar n (x:xs) | n == x = xs
                | otherwise = x : quitar n xs
--Ejercicio 2.6
quitarTodos :: (Eq t) => t -> [t] ->[t]
quitarTodos _  [] = []
quitarTodos n (x:xs) | n == x = quitarTodos n xs
                     | otherwise = x : quitarTodos n xs
--Ejercicio 2.7
eliminarRepetidos :: (Eq t) => [t] -> [t]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:y:xs) | x == y = eliminarRepetidos (y:xs)
                           | otherwise = x : eliminarRepetidos (y:xs)
--Ejercicio 2.8
estaContenido :: (Eq t) => [t] -> [t] -> Bool
estaContenido [] [] = True
estaContenido x [] = False
estaContenido [] xs = True
estaContenido (x:xs) (y:ys) = pertenece x (y:ys) && estaContenido xs (y:ys) 

mismosElementos :: (Eq t) => [t] -> [t] -> Bool
mismosElementos [] [] = True
mismosElementos (x:xs) (y:ys) = estaContenido (x:xs) (y:ys) && estaContenido (y:ys) (x:xs)  

--Ejercicio 2.9
capicua :: (Eq t) => [t] -> Bool
capicua (x:xs) = (x:xs) == reverso (x:xs)

--Ejercicio 3
sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria [x] = x
sumatoria (x:y:xs) = x + y + sumatoria xs

productoria :: [Int] -> Int
productoria [] = 0
productoria [x] = x
productoria (x:xs) = x * productoria xs

maximo :: [Int] -> Int 
maximo [x] = x
maximo (x:y:xs) | x >=y && xs == [] = x 
                | x < y = maximo (y:xs)
                | otherwise = maximo (x:xs)

sumarN :: Int -> [Int] -> [Int]
sumarN n (x:xs) | xs == [] = [n+x]
                | otherwise = (n+x) : sumarN n xs
        
sumarElPrimero :: [Int] -> [Int]
sumarElPrimero (x:xs) = sumarN x (x:xs)

sumarElUltimo :: [Int] -> [Int]
sumarElUltimo (x:xs) = sumarN (ultimo (x:xs)) (x:xs)

pares :: [Int] -> [Int]
pares [] = []
pares (x:xs) | mod x 2 == 0 && xs == [] = [x]
             | mod x 2 == 0 = x : pares xs
             | otherwise = pares xs

multiplosDeN :: Int -> [Int] -> [Int]
multiplosDeN n (x:xs) | mod x n == 0 && xs == [] = [x]
                      | mod x n == 0 = x : multiplosDeN n xs
                      | otherwise = multiplosDeN n xs

ordenarDecr :: [Int] -> [Int]
ordenarDecr [] = []
ordenarDecr [x] = [x]
ordenarDecr (x:xs) | xs == [] = [x]
                   | otherwise = maximo (x:xs) : ordenarDecr(quitar (maximo(x:xs)) (x:xs) )

ordenar :: [Int] -> [Int]
ordenar [] = []
ordenar [x] = [x]
ordenar (x:xs) = reverso (ordenarDecr (x:xs))    

--Ejercicio 4 FUNCIONES SOBRE LISTAS DE CHAR, PALABRA = SECUENCIA DE CARACTERES SIN BLANCOS
sacarBlancosRepetidos :: [Char] -> [Char]
sacarBlancosRepetidos [] = []
sacarBlancosRepetidos [x] =[x]
sacarBlancosRepetidos (x:y:xs) | x==' ' && x == y = sacarBlancosRepetidos (y:xs)
                               | otherwise = x : sacarBlancosRepetidos (y:xs)
                    
--4b
limpiarLista :: [Char] -> [Char]
limpiarLista [] = []
limpiarLista [x] =[x]
limpiarLista (x:y:xs) | x == ' ' && y == ' ' = limpiarLista (x:xs)
                      | otherwise = x: limpiarLista (y:xs)

contarPalabras :: [Char] -> Int
contarPalabras [] = 0
contarPalabras [x] = 1
contarPalabras (x:xs) | x ==' ' = 1 + contarPalabras (limpiarLista(xs))
                      | otherwise = contarPalabras (limpiarLista (xs))
--4c
rebanarEnPalabras :: [Char] -> [Char] -> [[Char]]
rebanarEnPalabras (x:xs) y | xs == [] || xs == [' '] = [y++[x]]
                           | x == ' ' = [y] ++ rebanarEnPalabras xs [] 
                           | otherwise = rebanarEnPalabras xs (y++[x])

palabras :: [Char] -> [[Char]]
palabras (x:xs) = rebanarEnPalabras (limpiarLista (x:xs)) []

--4d
--palabraMasLarga :: [Char] -> [Char]
--palabraMasLarga 
