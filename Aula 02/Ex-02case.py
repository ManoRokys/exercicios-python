indice = int(input("Digite o indice de poluição: "))

match indice:
    case 0 | 1 | 2:
        print("Considerar aceitavel")
    case 3 | 4 | 5:
        print("Suspender atividades Grupo I")
    case 6 | 7:
        print("Suspender atividades Grupo I e Grupo II")
    case _:
        print("Suspender atividades de todos os grupos")                                