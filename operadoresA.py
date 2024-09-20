print("Act 9 clases v2")
print("Angel Gabriel Alvarado Aguirre")
# zona de class 
class Operadores1127:
    # zona de funciones
    # Suma 
    def suma1127(self,E,N):
        sumaTotal1127=E+N
        print(f"la suma de {E} + {N} = {sumaTotal1127}")
    # Resta
    def resta1127(self,E,N):
        sumaTotal1127=E-N
        print(f"la resta de {E} - {N} = {sumaTotal1127}")
    # Multiplicacion
    def multiplicacion1127(self,E,N):
        sumaTotal1127=E*N
        print(f"la multiplicacion de {E} x {N} = {sumaTotal1127}")
    # Division 
    def Division1127(self,E,N):
        sumaTotal1127=E/N
        print(f"la division de {E} / {N} = {sumaTotal1127}")
    # Modulo 
    def Mod1127(self,E,N):
        sumaTotal1127=E%N
        print(f"El residuo de la division (modulo) de {E} % {N} = {sumaTotal1127}")
    # Exponente
    def Exponente1127(self,E,N):
        sumaTotal1127=E**N
        print(f"El exponente de {E} ** {N} = {sumaTotal1127}")
    # Cociente 
    def Cociente1127(self,E,N):
        sumaTotal1127=E//N
        print(f"El cociente de {E} // {N} = {sumaTotal1127}")
# zona de creacion de objeto
operangel=Operadores1127()
# zona de uso de objetos 
print("\nFuncion suma")
operangel.suma1127(5,6)
print("\nFuncion resta")
operangel.resta1127(10,5)
print("\nFuncion multiplicacion")
operangel.multiplicacion1127(5,5)
print("\nFuncion division")
operangel.Division1127(10,2)
print("\nFuncion modulo")
operangel.Mod1127(9,2)
print("\nFuncion exponente")
operangel.Exponente1127(3,5)
print("\nFuncion cociente\n")
operangel.Cociente1127(4,5)