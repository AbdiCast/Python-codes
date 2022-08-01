# coding=utf-8

cadena1 = input("Introduce la primera cadena: ").upper()
cadena2 = input("Introduce la segunda cadena: ").upper()

if cadena1.isspace() and cadena2.isspace():
    print('Introduce caracteres ademas de espacios en blanco.')
elif sorted(cadena1) == sorted(cadena2):

    print("Anagrama")
else:
    print("No son Anagramas")
# coding=utf-8

#linea agregada
