import sys
import time


BATTERY_CAPACITY_KWH = 75.0
CHARGE_POWER_KW = 50.0
SERVICE_TAX_RATE = 0.05
GOVERNMENT_TAX_RATE = 0.12

def get_battery_level():
    while True:
        try:
            nivel = float(input("Nível da bateria (%) [0-100]: "))
            if 0 <= nivel < 100:
                return nivel
            if nivel == 100:
                print("A bateria já está completamente carregada. Nenhuma recarga necessária.")
                sys.exit(0)
            print("Valor deve estar entre 0 e 100.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def get_target_battery_level(current_level):
    while True:
        try:
            alvo = float(input("Nível de carga desejado (%) [0-100]: "))
            if current_level <= alvo <= 100:
                return alvo
            print(f"O nível desejado deve estar entre {current_level:.0f} e 100.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def calculate_energy_needed(current_level, target_level):
    return BATTERY_CAPACITY_KWH * (target_level - current_level) / 100.0

def calcular_tarifa(energia, tipo_usuario):
    tarifa_base = 0.50

    if tipo_usuario == 2:
        desconto = 0.8
    else:
        desconto = 1

    hora = time.localtime().tm_hour
    if hora >= 22 or hora < 6:
        tarifa_base *= 0.9

    return energia * tarifa_base * desconto

def escolher_pagamento():
    opcao = "";
    while opcao not in ["1", "2", "3"]:    
        print("\nEscolha a forma de pagamento:")
        print("1 - Pix")
        print("2 - Débito")
        print("3 - Crédito")
        
        opcao = input("Digite a opção: ")

        if opcao == "1":
            print("Pagamento via Pix selecionado")
        elif opcao == "2":
            print("Pagamento via Débito selecionado")
        elif opcao == "3":
            
            print("Pagamento via Crédito selecionado")
        else:
            print("Opção inválida")

def format_currency(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def simular_recarga():
    print("=== INÍCIO DA SESSÃO DE RECARGA ===")
   
    nivel_atual = get_battery_level()
    nivel_desejado = get_target_battery_level(nivel_atual)

    energia_necessaria = calculate_energy_needed(nivel_atual, nivel_desejado)
    if energia_necessaria <= 0:
        print("A bateria já está no nível desejado. Nenhuma recarga necessária.")
        return

    carga_por_minuto = CHARGE_POWER_KW / 60.0
    duracao_minutos = int((energia_necessaria / carga_por_minuto) + 0.999)

    energia_total = 0.0
    print(f"\nCarregando de {nivel_atual:.0f}% até {nivel_desejado:.0f}%...")
    for minuto in range(1, duracao_minutos + 1):
        energia_total += carga_por_minuto
        if energia_total > energia_necessaria:
            energia_total = energia_necessaria
        print(f"Minuto {minuto}: +{carga_por_minuto:.2f} kWh (Total: {energia_total:.2f} kWh)")
        time.sleep(0.05)
        if energia_total >= energia_necessaria:
            break

    custo_energia = calcular_tarifa(energia_total, usuario)
    taxa_servico = custo_energia * SERVICE_TAX_RATE
    taxa_governo = custo_energia * GOVERNMENT_TAX_RATE
    custo_total = custo_energia + taxa_servico + taxa_governo

    print("\n=== FIM DA SESSÃO ===")
    print("RELATÓRIO DE RECARGA")
    print(f"Nível inicial da bateria: {nivel_atual:.0f}%")
    print(f"Nível final da bateria: {nivel_desejado:.0f}%")
    print(f"Energia consumida: {energia_total:.2f} kWh")
    print(f"Duração estimada: {duracao_minutos} minutos")
    print(f"Custo da energia: {format_currency(custo_energia)}")
    print(f"Taxa de serviço ({SERVICE_TAX_RATE * 100:.0f}%): {format_currency(taxa_servico)}")
    print(f"Taxa governamental ({GOVERNMENT_TAX_RATE * 100:.0f}%): {format_currency(taxa_governo)}")
    print(f"Custo total: {format_currency(custo_total)}")

    escolher_pagamento()

def iniciar_menu():
    while True:
        print("==== Recarregador RAIOS ====")
        print("1 - Iniciar nova sessão")
        print("2 - Monitorar Sessões ativas")
        print("3 - Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            # menu()
            break
        elif opcao == "2":
            print("Monitorando sessões ativas...")
            # monitorar_sessoes_ativas()
            return iniciar_menu()
        else:
            print("Opção inválida. Tente novamente.")

def finalizar_sessao():
    print("Sessão finalizada. Obrigado por usar o Recarregador RAIOS!")

def menu():
    while True:
        print("==== Sessão de Recarga ====")
        print()
        print("1 - Conectar veículo")
        print("2 - Iniciar recarga")
        print("3 - Finalizar sessão")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            print("Veículo conectado com sucesso!")
            #conectar_veiculo()
            simular_recarga()
            break
        elif opcao == "2":
            print("Iniciando recarga...")
        elif opcao == "3":
            # finalizar_sessao()
            break
        else:
            print("Opção inválida. Tente novamente.")

def conectar_veiculo():
if __name__ == "__main__":
    simular_recarga()