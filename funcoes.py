def cardapio():
    print("==============CARDÁPIO==============\nBrigadeiro - R$ 4,00\nBeijinho - R$ 4,00\nBrownie - R$ 8,00\nBolo de Cenoura (fatia) - R$ 12,00\nPalha Italiana - R$ 9,00\n====================================")

def fazerPedido():
    pedido = [] 
    while True:

        escolha = int(input('Informe a opção desejadae e quando desejar parar, selecione 0: '))
        if escolha == 0:
            break
        elif escolha != 0:
            pedido.append(escolha)
    return pedido