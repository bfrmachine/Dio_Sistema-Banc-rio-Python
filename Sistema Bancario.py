# Desafio Sistema Bancario - Dio Bootcamp


def deposito(saldo, extrato, valor):
    if valor > 0:
        saldo += valor
        extrato.append(f'Depósito: R$ {valor:.2f}')
        print(f'Depósito de R$ {valor:.2f} realizado com sucesso.')
    else:
        print('Valor de depósito inválido!')
    return saldo, extrato

def saque(saldo, extrato, valor, saques_diarios, limite, limite_saques):
    if valor <= 0:
        print('Valor de saque inválido!')
    elif valor > limite:
        print(f'Valor de saque excede o limite de {limite:.2f}.')
    elif saques_diarios >= limite_saques:
        print(f'Número máximo de saques diários atingido.')
    elif valor > saldo:
        print('Saldo insuficiente!')
    else:
        saldo -= valor
        saques_diarios += 1
        extrato.append(f'Saque: R$ {valor:.2f}')
        print(f'Saque de R$ {valor:.2f} realizado com sucesso.')
    return saldo, extrato, saques_diarios

def mostrar_extrato(saldo, extrato):
    print('\n============= Extrato =================')
    if not extrato:
         print("Não foram realizadas movimentações." if not extrato else extrato)
    else:
        for movimento in extrato:
            print(movimento)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("=======================================")

def menu():
    saldo = 0
    limite = 500
    limite_saques = 3
    saques_diarios = 0
    extrato = []
    
    while True:
        print('\nMenu:')
        print('1. Depósito')
        print('2. Saque')
        print('3. Extrato')
        print('4. Sair')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            valor = float(input('Digite o valor do depósito: '))
            saldo, extrato = deposito(saldo, extrato, valor)
        elif opcao == '2':
            valor = float(input('Digite o valor do saque: '))
            saldo, extrato, saques_diarios = saque(saldo, extrato, valor, saques_diarios, limite, limite_saques)
        elif opcao == '3':
            mostrar_extrato(saldo, extrato)      
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opção inválida! Tente novamente.')

if __name__ == '__main__':
    menu()
