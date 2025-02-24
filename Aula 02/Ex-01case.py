letra = input("Digite uma letra: ")

match letra.lower:
    case "a":
        print("A letra digitada foi uma Vogal")
    case "e":
        print("A letra digitada foi uma Vogal")
    case "i":
        print("A letra digitada foi uma Vogal")
    case "o":
        print("A letra digitada foi uma Vogal")
    case "u":
        print("A letra digitada foi uma Vogal")
    case _:
        print("A letra digitada foi uma Consoante")            