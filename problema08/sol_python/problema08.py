pies = 0
yardas = 0
pulgadas = 0
metros = 0
centimetros = 0
contador = 0
suma = 0
cadena0 = ""
cadena1 = ""
cadena2 = ""
cadena3 = " "
cadena4 = " "
cadenafinal = ""
metro = (int(input("Ingrese el valor en metros que desea convertir: ")))
cadena0 = ("Metros | Yardas| Pulgada| Pies")
print(cadena0)
while contador<metro:
    contador = contador + 1
    suma = contador
    yardas = (suma * 1.094)
    pulgadas = (suma * 39.37)
    pies = (suma*3.2804)
    cadena1 =suma
    cadena2="%.2f" % yardas
    cadena3 ="%.2f" % pulgadas
    cadena4="%.2f" % pies
    cadenafinal= cadena1,"",cadena2,cadena3,cadena4
    print(cadenafinal)




