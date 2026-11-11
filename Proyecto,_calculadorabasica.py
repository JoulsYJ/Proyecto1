def calculadora():
    print("--- Calculadora Básica ---")
    print("Operaciones: + , - , * , /")

    num1 = float(input("Ingresa el primer número: "))
    operacion = input("Elige una operación (+, -, *, /): ")
    num2 = float(input("Ingresa el segundo número: "))

    if operacion == "+":
        resultado = num1 + num2
    elif operacion == "-":
        resultado = num1 - num2
    elif operacion == "*":
        resultado = num1 * num2
    elif operacion == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Error: No se puede dividir entre cero."
    else:
        return "Operación no válida."

    return f"Resultado: {resultado}"

print(calculadora())
