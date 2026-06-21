import Modelos
import Servicos
import random


sessoes = [][3]
carregador = [4]
def exibir_menu():


    while True:

        print("\n===== MENU =====")
        print("1 - Adicionar Veículo")
        print("2 - Listar Sessões")
        print("3 - Distribuir Potência")
        print("4 - Relatório")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":

            id += 0
            modelo = input("Digite o modelo do seu carro: ")
            bateria = random.randint(0,80)
            carro = Modelos.Veiculo(modelo, id, bateria)
            sessao = Modelos.SessaoRecarga(id, carro)

            sessoes.append(sessao)

            print(sessoes)

            pass

        elif opcao == "2":

            print("==== Sessões Ativas ====")

            for i in range(len(sessoes)):
                
                print(f"Sessão {i+1}: {sessoes[i]}")

            pass

        elif opcao == "3":
            pass

        elif opcao == "4":
            pass

        elif opcao == "0":
            break

exibir_menu()