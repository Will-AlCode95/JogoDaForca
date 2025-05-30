from palavraforca import palavra

letras_user = []

chances = 5

ganhou = False

while True:
 
    for letra in palavra:
        if letra.lower() in letras_user:
            print(letra, end=" ")
        else:
            print("_", end= " ")
    print(f"Você tem {chances} chances")
    tentativa = input("Escolha uma letra para chutar: ")
    letras_user.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
         chances = chances - 1
    
    ganhou = True
    for letra in palavra:  #para cada letra dentro da palavra
        if letra.lower() not in letras_user:
            ganhou = False
    
    if chances == 0 or ganhou:
        break


if ganhou:
    print("================================================")
    print(f"Parabéns, voce ganhou! A palavra era:{palavra}")
    print("================================================")
else:
     print("=========================================")
     print(f"Você perdeu! A palavra era: {palavra}")
     print("=========================================")