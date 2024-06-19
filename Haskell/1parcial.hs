---Ejercicio 1
cantApariciones :: (Eq t)=> t-> [t] -> Int
cantApariciones _ [] = 0
cantApariciones e (x:xs) | e == x = 1 + cantApariciones e xs
                         | otherwise = cantApariciones e xs

eliminarRepetidos :: (Eq t) => t -> [t] ->[t]
eliminarRepetidos _ [] = []
eliminarRepetidos y (x:xs) | y == x = eliminarRepetidos x xs
                           | otherwise = x : eliminarRepetidos y xs
generarStock :: [[Char]] -> [([Char],Int)]
generarStock [] = []
generarStock (p:ps) = (p,1 + cantApariciones p ps) : generarStock(eliminarRepetidos p ps)
--Ejercicio 2
buscarStock :: [Char] -> [([Char],Int)] -> Int
buscarStock _ [] = 0
buscarStock e ((p,c):ps) | e == p = c 
                         | otherwise = buscarStock e ps

--Ejercicio 3
precioProducto :: [Char] -> [([Char],Float)] -> Float 
precioProducto p [(a,b)] = b
precioProducto p (x:xs) | p == fst x  = snd x
                        | otherwise = precioProducto p xs

dineroStock :: [([Char],Int)] -> [([Char],Float)] -> Float
dineroStock [] (c:cs) = 0
dineroStock (p:ps) cs = (fromIntegral (snd p))* precioProducto (fst p) cs + dineroStock ps cs

--Ejercicio 4 
aplicarOferta :: [([Char],Int)] -> [([Char],Float)] -> [([Char],Float)] 
aplicarOferta [] (p:ps) = (p:ps)
aplicarOferta stock (p:ps) | buscarStock (fst p) stock  > 10 = (fst p,snd p*0.8): aplicarOferta stock ps
                           | otherwise = p : aplicarOferta stock ps
