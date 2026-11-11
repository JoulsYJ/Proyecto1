def calculadora():
    print("===Calculadora de papulandia===")
    print("PapuOperaciones: + , - , * , /")

    numero1 = float(input("Ingresa el primer número: "))
    operacion = input("Elige una operación (+, -, *, /): ")
    numero2 = float(input("Ingresa el segundo número: "))

    if operacion == "+":
        resultado = numero1 + numero2
    elif operacion == "-":
        resultado = numero1 - numero2
    elif operacion == "*":
        resultado = numero1 * numero2
    elif operacion == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            return "Error: No se puede dividir entre cero."
    else:
        return "Operación no válida."

    return f"Resultado: {resultado}"

print(calculadora())
