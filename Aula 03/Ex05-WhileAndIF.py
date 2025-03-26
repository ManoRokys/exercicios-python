quest = 1
acertos = 0
while (quest <= 3):
    res = input("Digite a resposta correta\na) A\nb) B\nc) C\nd) D\n")
    if quest == 1 and res == "a":
        acertos +=1
    if quest == 2 and res == "c":
        acertos +=1
    if quest == 3 and res == "d":
        acertos +=1
    quest += 1
print(f"Total de acertos: {acertos}")