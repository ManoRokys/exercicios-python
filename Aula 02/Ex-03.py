alt1 = float(input("Digite a primeira altura: "))
alt2 = float(input("Digite a segunda altura: "))
alt3 = float(input("Digite a terceira altura: "))

if alt1 > alt2 and alt1 > alt3:
    if alt2 > alt3:
        print(f"A sequencia de alturas é: {alt1:.2f}, {alt2:.2f}, {alt3:.2f}")
    else:
        print(f"A sequencia de alturas é: {alt1:.2f}, {alt3:.2f}, {alt2:.2f}")    
elif alt2 > alt1 and alt2 > alt3:
    if alt1 > alt3:
        print(f"A sequencia de alturas é: {alt2:.2f}, {alt1:.2f}, {alt3:.2f}")
    else:
        print(f"A sequencia de alturas é: {alt2:.2f}, {alt3:.2f}, {alt1:.2f}")   
elif alt3 > alt1 and alt3 > alt1:
    if alt1 > alt2:
        print(f"A sequencia de alturas é: {alt3:.2f}, {alt1:.2f}, {alt2:.2f}")
    else:
        print(f"A sequencia de alturas é: {alt3:.2f}, {alt2:.2f}, {alt1:.2f19}")   
else:
    print("Você inseriu alguma altura repetida.")        
                        