import time

class SistemaRecarga:
    def __init__(self):
        self.sessoes = []
        self.gerenciador_energia = GerenciadorEnergia()
        self.tarifador = Tarifador()
        self.ocpp = ComunicacaoOCPP()


class Tarifador:

    def calcular_tarifa(self, energia, sessoes, carregadores):
        quantidade = len(sessoes)  # Quantidade de sessões
        demanda = quantidade / carregadores  # Calcula a demanda de uso dos carregadores
        tarifa_base = 0.50
        hora = time.localtime().tm_hour

        if demanda > 1:
            tarifa_base *= demanda

        if hora >= 22 or hora < 6:
            tarifa_base *= 0.9

        return energia * tarifa_base


class ComunicacaoOCPP:

    def enviar(self, mensagem):
        print(f"[OCPP] {mensagem}")


class GerenciadorEnergia:
    POTENCIA_TOTAL = 60

    def distribuir_potencia(self, sessoes):
        quantidade = len(sessoes)

        if quantidade > 0:
            potencia = self.POTENCIA_TOTAL / quantidade

            for sessao in sessoes:
                sessao.potencia = potencia


class Relatorio:

    def gerar(self, sessoes):
        print(f"Total de sessões: {len(sessoes)}")
