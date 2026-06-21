# Define as informações do veículo 
class  Veiculo:
        def __init__(self, modelo, bateria, id):
            self.modelo = modelo
            self.bateria = bateria
            self.id = id

        def exibir(self):
            print(f"ID: {self.id}")
            print(f"Modelo: {self.modelo}")
            print(f"Bateria: {self.bateria}%")
class SessaoRecarga:
    
    def __init__(self, id_sessao, veiculo, id_carregador):
        self.id_sessao = id_sessao

        self.id_carregador = id_carregador.append(id_carregador)
        self.veiculo = Veiculo.append(veiculo)
        self.potencia = 0
        self.energia_consumida = 0
        self.status = "Ativa"

    def exibir(self):
        print(f"Sessão: {self.id_sessao}")
        print(f"Carregador: {self.id_carregador}")
        print(f"Veiculo: {self.veiculo}")
        print(f"Status: {self.status}\n")
        print(f"Potencia: {self.potencia} kW")
        print(f"Consumo: {self.energia_consumida} kWh")
        