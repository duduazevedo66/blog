from funcoes import *

opcoes = int(input('1 - Ver cardápio de doces\n' \
'2 - Fazer pedidos\n3 - Calcule o total\n' \
'4 - Aplique desconto\n5 - Registre a forma de pagamento\n'))

match opcoes:
    case 1:
        cardapio()
    case 2:
        fazerPedido()