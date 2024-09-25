

{-problema relacionesValidas (relaciones: seq⟨String x String⟩) : Bool {
      requiere: {True}
      asegura: {(res = true) <=> relaciones no contiene ni tuplas repetidas1, ni tuplas con ambas componentes iguales}
    }
    1 A los fines de este problema consideraremos que dos tuplas son iguales si el par de elementos que las componen (sin importar el orden) son iguales.
 -}

relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x,y):xs) | x == y = False
                             | estaContenida (x,y) xs = False
                             | otherwise = relacionesValidas xs
                             

estaContenida :: (String,String) -> [(String,String)] -> Bool
estaContenida (x,y) [] = False
estaContenida (a,b) ((x,y):xs) | a == x && b == y = True
                               | a == y && b == x = True
                               | otherwise = estaContenida (a,b) xs


{-problema personas (relaciones: seq⟨String x String⟩) : seq⟨String⟩ {
      requiere: {relacionesValidas(relaciones)}
      asegura: {res no tiene elementos repetidos}
      asegura: {res tiene exactamente los elementos que figuran en alguna tupla de relaciones, en cualquiera de sus posiciones}
    -}


personas :: [(String,String)] -> [(String)]
personas [] = []
personas xs = eliminarRepetidos (personasAux xs)


personasAux :: [(String,String)] -> [(String)]
personasAux [] = []
personasAux ((x,y):xs) = x : y : personasAux xs 

eliminarRepetidos :: [(String)] -> [(String)]
eliminarRepetidos [] = []
eliminarRepetidos [x] = [x]
eliminarRepetidos (x:xs) | estaContenido x xs == False = x : eliminarRepetidos xs
                         | otherwise = eliminarRepetidos xs

estaContenido :: String -> [(String)] -> Bool
estaContenido n [] = False
estaContenido n (x:xs) | n == x = True
                       | otherwise = estaContenido n xs

        
{-    problema amigosDe (persona: String, relaciones: seq⟨String x String⟩) : seq⟨String⟩ {
      requiere: {relacionesValidas(relaciones)}
      asegura: {res tiene exactamente los elementos que figuran en las tuplas de relaciones en las que una 
      de sus componentes es persona}
    -}
type Persona = String
type Relaciones = [(String,String)]


{-
    problema personaConMasAmigos (relaciones: seq⟨String x String⟩) : String {
      requiere: {relaciones no vacía}
      requiere: {relacionesValidas(relaciones)}
      asegura: {res es el Strings que aparece más veces en las tuplas de relaciones (o alguno de ellos si hay empate)}
-}
personaConMasAmigos :: Relaciones -> String
personaConMasAmigos [(x,y)] = x
personaConMasAmigos ((x,y):xs) | contador (amigosDe x ((x,y):xs)) >= contador (amigosDe (personaConMasAmigos xs) xs)  = x 
                               | contador (amigosDe y ((x,y):xs)) >= contador (amigosDe (personaConMasAmigos xs) xs)  = y 
                               | otherwise = personaConMasAmigos xs

contador :: [String] -> Int
contador [] = 0
contador (x:xs) = 1 + contador xs

amigosDe :: Persona -> Relaciones -> [String]
amigosDe p [] = []
amigosDe p ((x,y):xs) | p == x = y : amigosDe p xs
                      | p == y = x : amigosDe p xs
                      | otherwise = amigosDe p xs
