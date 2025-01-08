n = int(input("Quantos números você deseja inserir? "))

menor_valor = float('inf')  
maior_valor = float('-inf') 
soma = 0


for i in range(n):
    numero = int(input(f"Digite o {i+1}º número: "))
    
    if numero < menor_valor:
        menor_valor = numero
    
    if numero > maior_valor:
        maior_valor = numero
    
    soma += numero

print(f"O menor valor é: {menor_valor}")
print(f"O maior valor é: {maior_valor}")
print(f"A soma dos valores é: {soma}")