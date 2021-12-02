num1 = int(input("Ingresar número 1: "))
num2 = int(input("Ingresar número 2: "))
num3 = int(input("Ingresar múmero 3: "))
if num1 == num2 or num2 == num3 or num1 == num3:
    print("No se puede ejecutar porque los numeros tienen el mismo valor")
else:
    print("El número mayor entre %d, %d y %d es :%d" %(num1, num2, num3, max(num1, num2, num3)))