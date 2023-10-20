def producto_sumas_sucesivas(num1, num2):
    producto = 0

if (num1 < 0 and num2 > 0) or (num1 > 0 and num2 < 0):
        producto = -producto
    
    return producto

num1 = int(input("Ingrese el primer número entero: "))
num2 = int(input("Ingrese el segundo número entero: "))

resultado = producto_sumas_sucesivas(num1, num2)

print(f"El producto de {num1} y {num2} es: {resultado}")