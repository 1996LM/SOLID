#PRINCIPIO DE ABIERTO CERRADO
#Las entidades de software deben estar abiertas a la extencion pero cerradas a la modificacion
#lo que ya cree no deberia tocarlo si no extenderlo porque 
# si creo una clase basica puede dañar alguna de las clases que esta heredando


def mayor_dos_numeros(num1, num2):
    if num1>num2:
        return num1
    return num2

#sin aplicar abierto cerrad  quiero un afuncion que me compare tres numeros
def mayor_dos_tres_numeros(a,b,c):
    mayor = b
    if a>b:
        mayor = a
    if c is not None and c > mayor:
        mayor = c
    return mayor



def mayor_tres_numeros(a,b,c):
    mayor_dos_numeros = mayor_dos_numeros(a,b)
    mayor = mayor_dos_numeros(mayor_dos_numeros,c)
    return mayor



