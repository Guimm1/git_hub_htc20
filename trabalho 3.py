# Tabela FIPE fictícia
tabela_fipe = {
    # Honda 
    "honda hrv": 78000,
    "honda city": 51500,
    "honda crv": 60012,
    # Fiat
    "fiat pulse": 62108,
    "fiat fastback": 36038,
    "fiat toro": 75454,
    # Nissan
    "nissan kicks": 51450,
    "nissan versa": 75480,
    "nissan sentra": 80000,
    # Renault
    "renault kardian": 83300,
    "renault kwid": 67000,
    "renault duster": 50000,
    # Volkswagen
    "volkswagen nivus": 73400,
    "volkswagen t-cross": 93001,
    "volkswagen polo": 73000,
}

# Lista de veículos disponíveis para aluguel e compra
veiculos_disponiveis = ["honda hrv", "honda city", "honda crv", "fiat pulse", "fiat fastback", "fiat toro", 
                        "nissan kicks", "nissan versa", "nissan sentra", "renault kardian", 
                        "renault kwid", "renault duster", "volkswagen nivus", "volkswagen t-cross", 
                        "volkswagen polo"]




# Função para exibir o menu
def exibir_menu():
    print("\nMenu:")
    print("1. Vender veículo")
    print("2. Alugar veículo")
    print("3. Comprar veículo")
    print("4. Sair")

# Função para vender veículo
def vender_veiculo(cliente):
    print("honda hrv\nhonda city\nhonda crv\nfiat pulse\nfiat fastback\nfiat toro\nnissan kicks\nnissan versa\nnissan sentra\nrenault kardian\nrenault kwid\nrenault duster\nvolkswagen nivus\nvolkswagen t-cross\nvolkswagen polo")
    marca = input("Informe a marca e o modelo do veículo: ").lower()
    
    if marca in tabela_fipe:
        valor_avaliado = tabela_fipe[marca]
        proposta = valor_avaliado * 0.88  # 12% de desconto
        print(f"Proposta de venda: R${proposta:.2f}")
        
        aceitar = input("Você aceita a proposta? (s/n): ").lower()
        if aceitar == 's':
            cliente['saldo'] += proposta
            veiculos_disponiveis.append(marca)
            print(f"Veículo vendido! Seu novo saldo é R${cliente['saldo']:.2f}.")
        else:
            print("Venda cancelada.")
    else:
        print("não temos interesse em seu veiculo.")

# Função para alugar veículo
def alugar_veiculo(cliente):
    print("Veículos disponíveis para aluguel:")
    for veiculo in veiculos_disponiveis:
        print(veiculo)
    
    escolha = input("Escolha um veículo para alugar: ").lower()
    if escolha in veiculos_disponiveis:
        try:
            dias = int(input("Informe o número de dias para aluguel: "))
            if dias <= 0:
                print("O número de dias deve ser positivo.")
                return
            custo = dias * 77
            
            if cliente['saldo'] >= custo:
                cliente['saldo'] -= custo
                veiculos_disponiveis.remove(escolha)
                print(f"Veículo alugado! Seu novo saldo é R${cliente['saldo']:.2f}.")
            else:
                print("Saldo insuficiente para aluguel.")
        except ValueError:
            print("Por favor, insira um número válido para os dias.")
    else:
        print("Veículo não disponível.")

# Função para comprar veículo
def comprar_veiculo(cliente):
    print("Veículos disponíveis para compra:")
    for veiculo in veiculos_disponiveis:
        print(veiculo)
    
    escolha = input("Escolha um veículo para comprar: ").lower()
    if escolha in veiculos_disponiveis:
        valor_avaliado = tabela_fipe[escolha]  # Pega o valor diretamente da tabela
        valor_compra = valor_avaliado * 1.25  # 25% de acréscimo
        
        if cliente['saldo'] >= valor_compra:
            cliente['saldo'] -= valor_compra
            veiculos_disponiveis.remove(escolha)
            print(f"Veículo comprado! Seu novo saldo é R${cliente['saldo']:.2f}.")
        else:
            print("Saldo insuficiente para compra.")
    else:
        print("Veículo não disponível.")

# Função principal(dados do usuario)
def main():
    nome = input("Informe seu nome: ")
    telefone = input("Informe seu telefone: ")
    saldo = float(input("Informe seu saldo disponível: "))
    
    cliente = {'nome': nome, 'telefone': telefone, 'saldo': saldo}
    print(f"Bem-vindo, {cliente['nome']}! Seu saldo inicial é R${cliente['saldo']:.2f}.")
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            vender_veiculo(cliente)
        elif opcao == '2':
            alugar_veiculo(cliente)
        elif opcao == '3':
            comprar_veiculo(cliente)
        elif opcao == '4':
            print("Saindo do sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
