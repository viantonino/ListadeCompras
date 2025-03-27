
menu = """""

[1] Adicionar item
[2] Remover item
[3] Ver lista
[4] Sair

=> """

lista_de_compras = []

#loop de opções ao usuário
while True:
    
    entrada = input(menu).strip()

    if entrada == '1':
        item = input("Digite um item: ")
        lista_de_compras.append(item)
        

    elif entrada == '2':
        item = input("Digite um item: ")

        if item in lista_de_compras:
            lista_de_compras.remove(item)
        else:
            print(f'{item} não está na lista!')


    elif entrada == '3':
        if not lista_de_compras:
            print("Lista de compras vazia!")
        else:
            print(lista_de_compras)


    elif entrada == '4':
        break


    else:
        print("Operção inválida, por favor selecione novamente a operação desejada.")