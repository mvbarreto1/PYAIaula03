def classificar_idade():
    try:
        idade = int(input("Digite sua idade: "))

        if idade < 12:
            print("Criança")
        elif 12 <= idade <= 17:
            print("Adolescente")
        elif 18 <= idade <= 59:
            print("Adulto")
        elif idade >= 60:
            print("Idoso")
        else:
            print("Idade inválida.")
    except ValueError:
        print("Por favor, insira um número válido.")

classificar_idade()