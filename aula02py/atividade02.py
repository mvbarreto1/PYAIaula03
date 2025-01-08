def encontrar_maior_menor():
    try:
        numeros = []
        for i in range(3):
            numero = float(input(f"Digite o número {i + 1}: "))
            numeros.append(numero)

        maior = max(numeros)
        menor = min(numeros)

        print(f"O maior número é: {maior}")
        print(f"O menor número é: {menor}")
    except ValueError:
        print("Por favor, insira apenas números válidos.")


encontrar_maior_menor()
