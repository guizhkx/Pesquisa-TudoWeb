
print("=== PESQUISA DE SATISFAÇÃO TUDOWEB ===")

excelente = 0
ruim = 0

for i in range(1, 11):
    print(f"\nEntrevistado {i}")

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    print("\nComo você avalia nosso atendimento?")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    while opiniao not in (1, 2, 3):
        print("Opção inválida! Tente novamente.")
        opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
        print("Avaliação: EXCELENTE")

    elif opiniao == 2:
        print("Avaliação: BOM")

    else:
        ruim += 1
        print("Avaliação: RUIM")

    print("Obrigado pela participação,", nome)

print("\n=== RESULTADO DA PESQUISA ===")
print("Quantidade de respostas EXCELENTE:", excelente)
print("Quantidade de respostas RUIM:", ruim)
print("Total de entrevistados: 50")