# função comparaTexto
def comparatexto(texto1, texto2):
    tamanhoT1 = len(texto1)
    tamanhoT2 = len(texto2)

    diferenca = (tamanhoT1/tamanhoT2)*100

    print(f"O primeiro texto tem {tamanhoT1} caracteres.")
    print(f"O segundo texto tem {tamanhoT2} caracteres.")

    maior = ""
    menor = ""
    if tamanhoT1 == tamanhoT2:
        print("os dois textos tem o mesmo tamanho.")
    else:
        if tamanhoT1 > tamanhoT2:
            maior = "primeiro"
            menor = "segundo"
        elif tamanhoT1 < tamanhoT2:
            maior = "segundo"
            menor = "primeiro"

        print(f"O {menor} texto é menor que o {maior}, \nSendo {diferenca}% menor que este.")


texto1 = input("Cole o primeiro texto: ")
texto2 = input("Cole o segundo texto: ")

comparatexto(texto1, texto2)