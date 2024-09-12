print("Ejemplo de funciones")
## Declarando funciones
def hola():
    print("Alguien uso la funcion hola")
    
def chat(mensa):
    print(f"chat: {mensa}")  
    
def ellacontesta (mensa):
        print(f"chat ella : {mensa}")
def escribenombre(ap,n):
    print(f" Tu Nombre completo es: {n} {ap}")
    
def suma(a,b):
        s= a+b
        return s
    
def resta(Resta1,Resta2):
    r= Resta1- Resta2
    return r 

def multi(Multi1, Multi2):
    m= Multi1 * Multi2
    return m

def divi(Divi1, Divi2):
    d=Divi1/Divi2
    return d
    ## Llamadas a funcion 
hola()
chat("Que bonita estas")
ellacontesta("Gracias")
escribenombre("Ronquillo", "Reny")
print(" Operaciones suma : ")
c1=int(input(" Ingresa un numero "))
c2=int(input("Ingresa un segundo numero: "))
damesuma=suma(c1,c2)
print(f" La suma de {c1} + {c2} = {damesuma}")


print( " Operacion resta: " )
Resta1= int(input(" ingresa el numero que deseas restar: "))
Resta2= int(input(" ingresa el numero que deseas restar: "))
dameresta=resta(Resta1, Resta2)
print(f" La resta de {Resta1 } - {Resta2} = {dameresta} ")

print(" Operacion Multiplicación: ")
Multi1= int(input("Ingresa el numero para multiplicar: "))
Multi2= int(input("Ingresa el numero para multiplicar: "))
damemulti= multi(Multi1, Multi2)
print(f" La multiplicacion de {Multi1} * {Multi2} = {damemulti} ")

print(" Operacion división: ")
D1 = int(input(" Ingresa el 1er numero para dividir: "))
D2 = int(input(" Ingresa el 2do numero para dividir: "))
damedivi=divi(D1,D2)
print(f" La division de {D1} / {D2} = {damedivi} ")
