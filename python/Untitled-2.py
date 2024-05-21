def Area_Rec (altura, base):

    'Encontrar el area del rectangulo'
    
    parameters:
    base (float) : 'base del rectangulo'
    altura (float) : 'altura del rectangulo'

    return

float: 'Area del rectangulo'

Ejemplos: 
Area_Rec (2 , 10)
20

return base * altura

def Area_Cuadrado 

 'Encontrar el area de un cuadrado'
    
 parameters :

 lado (float) : 'lado de un cuadrado'

 return  

 float: 'Area de un cuadrado'
 
  Ejemplos: 
 Area_cuadraddo (4)
 16

return lado ** 2 

def Area_Pararelogramo (base, altura):
 
 'Encontrar el area de un Pararelogramo'

 parameters:
    base (float) : 'base del Pararelogramo'
    altura (float) : 'altura del Pararelogramo'


 return  

 float: 'Area de un Pararelogramo'

 Ejemplos: 
 Area_Pararelogramo (5, 3)
 15

 def Area_Rombo (diagonal_mayor, diagonal_menor):
 
 'Encontrar el area de un rombo'

 parameters:
    diagonal_mayor (float) : 'la diagonal mayor del rombo'
    Diagonal_menor (float) : 'la diagonal menor del rombo'


 return  

 float: 'Area del rombo'

 Ejemplos: 
 Area_rombo (8, 6)
 24

 return (diagonal_mayor * diagonal_menor) /2

 def Area_Trapecio (base_mayor, base_menor, altura):
 
 'Encontrar el area de un trapecio'

 parameters:
    base_mayor (float) : 'la base mayor del trapecio'
    base_menor (float) : 'la base menor del trapecio'
    altura (float) : 'la altura de un trapecio'

 return  

 float: 'Area del trapecio'

 Ejemplos: 
 Area_trapecio (3, 5 ,7)
 18

 return (base_mayor + base_menor) * altura /2

def Area_Triangulo (base, altura):
 
 'Encontrar el area de un triangulo'

 parameters:
    base (float) : 'base del triangulo'
    altura (float) : 'altura del triangulo  '


 return  

 float: 'Area de un triangulo'

 Ejemplos: 
  Area_Triangulo (5, 3)
  7.5

return (altura * baase) /2

def Area_Triangulo_Equilatero (lado):
 
 'Encontrar el area de un triangulo equilatero'
    
 parameters :

 lado (float) : 'lado de un triangulo equilatero'

 return  

 float: 'Area de un triangulo equilatero'
 
  Ejemplos: 
 Area_Triangulo_Equilatero (4)
 6.92820

return ((3 ** 0.5)/4 )* lado ** 2

def Area_Triangulo_Rectangular (base, altura):
 
 'Encontrar el area de un triangulo rectangular'

 parameters:
    base (float) : 'base de un triangulo rectangular'
    altura (float) : 'altura de un triangulo rectangular  '


 return  

 float: 'Area de un triangulo rectangular'

 Ejemplos: 
  Area_Triangulo_Rectangular(5, 3)
  7.5

return (altura * base)

def Area_Triangulo_Regular (lado):
 
 'Encontrar el area de un triangulo regular usando la funcion area del triangulo equilatero'
    
 parameters :

 lado (float) : 'lado de un triangulo regular'

 return  

 float: 'Area de un triangulo regular'
 
  Ejemplos: 
 Area_Triangulo_Regular (4)
 6.92820

return Area_Triangulo_Regular (lado)

Lado = 4
Base  = 5
Altura = 3
Diagonal_Mayor = 8
Diagonal_Menor = 6