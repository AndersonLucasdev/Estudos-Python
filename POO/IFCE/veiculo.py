class Veiculo:

  def __init__(self, velocidade_maxima: float, km_rodados: float, marcha_automatica: bool) -> None:
    self.velocidade_maxima = velocidade_maxima
    self.km_rodados = km_rodados
    self.marcha_automatica = marcha_automatica

  def __str__(self):
        return f"O Veículo tem velocidade máxima de {self.velocidade_maxima} km/h com {self.km_rodados} km rodados e {'possui' if self.marcha_automatica else 'não possui'} marcha automática"

class Onibus(Veiculo):

  def __init__(self, velocidade_maxima: float, km_rodados: float, marcha_automatica: bool, num_assentos: int) -> None:
    super().__init__(velocidade_maxima, km_rodados, marcha_automatica)
    self.num_assentos = num_assentos

  def __str__(self):
      return f"O Ônibus tem velocidade máxima de {self.velocidade_maxima} km/h com {self.km_rodados} km rodados {self.num_assentos} no número de assentos e {'possui' if self.marcha_automatica else 'não possui'} marcha automática"

  def tarifa(self):
      return 5.00

class MicroOnibus(Onibus):

  def __init__(self, velocidade_maxima: float, km_rodados: float, marcha_automatica: bool, num_assentos: int) -> None:
    super().__init__(velocidade_maxima, km_rodados, marcha_automatica, num_assentos)
  
  def tarifa(self):
    return 4.50

class EmpresaOnibus():

  @staticmethod
  def faturamento(veiculo: str):
    if isinstance(veiculo, Onibus):
      return veiculo.num_assentos * veiculo.tarifa()
    elif isinstance(veiculo, MicroOnibus):
      return veiculo.num_assentos * veiculo.tarifa()
    else:
      return 0


onibus_teste = Onibus(155.00, 3200.00, True, 55)
print(f" O valor do faturamento foi R${EmpresaOnibus.faturamento(onibus_teste)}")

microonibus_teste = MicroOnibus(155.00, 3200.00, True, 55)
print(f" O valor do faturamento foi R${EmpresaOnibus.faturamento(microonibus_teste)}")

onibus_teste = Onibus(155.00, 3200.00, True, 55)
print(f" R${onibus_teste.tarifa()} de tarifa")

microonibus_teste = MicroOnibus(155.00, 3200.00, True, 35)
print(f" R${microonibus_teste.tarifa()} de tarifa")