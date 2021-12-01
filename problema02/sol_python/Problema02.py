# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
porcentaje1 = 20
porcentaje2 = 25
porcentaje3 = 40
porcentaje4 = 50
precio= float(input("Ingrese el costo unitario del producto: "))
cantidad= int(input("Ingrese la cantidad que desea de este producto: "))

costoparcial = (precio*cantidad)
print(costoparcial)
descuento1 = (costoparcial*porcentaje1)/(100)
descuento2 = (costoparcial*porcentaje2)/(100)
descuento3 = (costoparcial*porcentaje3)/(100)
descuento4 = (costoparcial*porcentaje4)/(100)

print("Venta de Trajes\n" "Cantidad de productos:",cantidad,"\n" and"\nCosto de los productos:",precio,"\n"and"\nSubtotal:",costoparcial)
if cantidad == 1:
    costofinal = costoparcial - descuento1
    print("Descuento:", descuento1)
if cantidad == 2:
    costofinal = costoparcial - descuento2
    print("Descuento:", descuento2)
if cantidad == 3:
    costofinal = costoparcial - descuento3
    print("Descuento:", descuento3)
if cantidad > 3:
    costofinal = costoparcial - descuento4
    print("Descuento:", descuento4)

print("El costo final de venta es: ", costofinal)