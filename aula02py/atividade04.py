n = int(input("Quantas pessoas irão responder? "))

soma_idades = 0

for i in range(n):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    soma_idades += idade

media_idade = soma_idades / n

if media_idade <= 25:
    print("A turma é jovem.")
elif 26 <= media_idade <= 60:
    print("A turma é adulta.")
else:
    print("A turma é idosa.")