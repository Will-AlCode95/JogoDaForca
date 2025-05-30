# 🎯 Jogo da Forca em Python

Este é um simples jogo da forca feito em Python, onde o jogador deve adivinhar uma palavra secreta, letra por letra, antes que suas chances acabem. O objetivo é acertar todas as letras da palavra antes de cometer 5 erros.

---

## 🧠 O que o código faz?

- Importa a palavra secreta a partir de um módulo externo chamado `palavraforca`.
- Inicia o jogo com o jogador tendo **5 chances**.
- Solicita que o jogador digite letras, uma por uma:
  - Se a letra estiver na palavra, ela é revelada.
  - Se não estiver, o número de chances diminui.
- A palavra é exibida parcialmente com traços (`_`) para letras ainda não descobertas.
- O jogo termina quando:
  - O jogador adivinha todas as letras (vitória), ou
  - As chances acabam (derrota).
- Exibe uma mensagem final com o resultado e a palavra correta.

---

## 📄 Exemplo de Código

```python
from palavraforca import palavra

letras_user = []
chances = 5
ganhou = False

while True:
    for letra in palavra:
        if letra.lower() in letras_user:
            print(letra, end=" ")
        else:
            print("_", end=" ")
    print(f"\nVocê tem {chances} chances")
    
    tentativa = input("Escolha uma letra para chutar: ")
    letras_user.append(tentativa.lower())

    if tentativa.lower() not in palavra.lower():
        chances -= 1

    ganhou = True
    for letra in palavra:
        if letra.lower() not in letras_user:
            ganhou = False

    if chances == 0 or ganhou:
        break

if ganhou:
    print("================================================")
    print(f"Parabéns, você ganhou! A palavra era: {palavra}")
    print("================================================")
else:
    print("=========================================")
    print(f"Você perdeu! A palavra era: {palavra}")
    print("=========================================")
