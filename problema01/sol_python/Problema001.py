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
angulo1= int(input("Ingrese el primer ángulo: "))
angulo2=int(input("Ingrese el segundo ámgulo: "))
angulo3=int(input("Ingrese el tercer ángulo: "))
if angulo1 == 90 or angulo2 == 90  or angulo3 == 90:
    print("El tipo de triangulo es: Rectangulo")
if (angulo1 > 90 and angulo1<180)or(angulo2 > 90 and angulo1<180)or(angulo3 >90 and angulo1<180):
    print("El tipo de triangulo es: Obtusangulo")
if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
    print("El tipo de triangulo es: Acutángulo")