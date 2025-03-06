# Parte para botar os números
num1 = int(input("Digite o primeiro número que deseja: "))
num2 = int(input("Digite o segundo número que deseja: "))

# Loop para garantir que o usuário insira uma operação válida
while True:
    operação = input("Qual operação deseja usar entre adição, subtração, multiplicação e divisão: ").strip().lower()
    
    if operação == "adição":
        print(f"A soma de {num1} + {num2} = {num1 + num2}")
        break
    elif operação == "subtração":
        print(f"A subtração de {num1} - {num2} = {num1 - num2}")
        break
    elif operação == "multiplicação":
        print(f"A multiplicação de {num1} * {num2} = {num1 * num2}")
        break
    elif operação == "divisão":
        if num2 == 0:
            print("Divisão por zero não é permitida!")
        else:
            print(f"A divisão de {num1} / {num2} = {num1 / num2}")
        break
    else:
        print("Escreva exatamente como está na mensagem.")