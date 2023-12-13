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


