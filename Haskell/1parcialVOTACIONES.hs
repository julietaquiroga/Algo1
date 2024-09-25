{-

CONSIGNA

1) Votos en Blanco [1 punto]

problema votosEnBlanco (formulas: seq⟨String x String⟩,votos:seq< Z >, cantTotalVotos: Z) : Z {
  requiere: {formulasValidas(formulas)}
  requiere: {|formulas| = |votos|}
  requiere: {Todos los elementos de votos son mayores o iguales a 0}
  requiere: {La suma de todos los elementos de votos es menor o igual a cantTotalVotos}
  asegura: {res es la cantidad de votos emitidos que no correspondieron a niguna de las fórmulas que se presentaron}
-}
type Formulas = [(String,String)] 
type Votos = [Int]
type CantTotalVotos = Int

cantVotos :: Votos -> Int
cantVotos [] = 0
cantVotos [v] = v
cantVotos (v:vs) = v + cantVotos vs

votosEnBlanco :: Formulas -> Votos -> CantTotalVotos -> Int
votosEnBlanco formula votos totalv = totalv - (cantVotos votos)


{-

2) Formulas Válidas [3 puntos]

problema formulasValidas (formulas: seq⟨String x String⟩) : Bool {
  requiere: {True}
  asegura: {(res = true) <=> formulas no contiene nombres repetidos, es decir que cada candidato
   está en una única fórmula (no se puede ser candidato a presidente y a vicepresidente ni en la misma 
   fórmula ni en fórmulas distintas)}
-}
formulasValidas :: Formulas -> Bool
formulasValidas [] = True
formulasValidas ((p,v):xs) | p == v = False
                           | pertenece p xs = False
                           | pertenece v xs = False
                           | otherwise = formulasValidas xs
                           

pertenece :: String -> Formulas -> Bool
pertenece candidato [] = False
pertenece candidato ((p,v):xs) | candidato == p || candidato == v = True
                               | otherwise = pertenece candidato xs 

{-3) Porcentaje de Votos [3 puntos]

problema porcentajeDeVotos (presidente: String, formulas: seq⟨String x String⟩,votos:seq< Z >) : R {
  requiere: {La primera componente de algún elemento de formulas es presidente}
  requiere: {formulasValidas(formulas)}
  requiere: {|formulas| = |votos|}
  requiere: {Todos los elementos de votos son mayores o iguales a 0}
  requiere: {Hay al menos un elemento de votos que es mayor que estricto que 0}
  asegura: {res es el porcentaje de votos que obtuvo la fórmula encabezada por presidente sobre el total de votos afirmativos}
}
Para resolver este ejercicio pueden utilizar la siguiente función que devuelve como Float la división entre dos números de tipo Int:
-}
division :: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b) 
type Presidente = String

porcentajeDeVotos :: Presidente -> Formulas -> Votos -> Float
porcentajeDeVotos p formula votos = division (maximo votos*100) (cantVotos votos) 

maximo :: Votos -> Int
maximo (x:y:xs) | x >= y && xs == [] = x
                | y > x && xs == [] = y
                | x >= y = maximo (x:xs)
                | y > x = maximo (y:xs)
                | otherwise = maximo xs

{-
4) Próximo Presidente [3 puntos]

problema proximoPresidente (formulas: seq⟨String x String⟩, votos:seq< Z >) : String {
  requiere: {formulasValidas(formulas)}
  requiere: {|formulas| = |votos|}
  requiere: {Todos los elementos de votos son mayores o iguales a 0}
  requiere: {Hay al menos un elemento de votos mayores estricto a 0}
  requiere: {|formulas| > 0}
  asegura: {res es el candidato a presidente de formulas más votado de acuerdo a los votos contabilizados en votos}
-}

proximoPresidente :: Formulas -> Votos -> String
proximoPresidente ((p,v):xs) votos = posicionPresi (posicionMaximo votos) ((p,v):xs)

posicionPresi :: Int -> Formulas -> Presidente
posicionPresi 1 ((p,v):xs) = p
posicionPresi n ((p,v):xs) = posicionPresi (n-1) xs

posicionMaximo :: Votos -> Int
posicionMaximo [x] = 1
posicionMaximo (x:xs) | x == maximo(x:xs) = 1 
                   | otherwise = 1 + posicionMaximo xs
