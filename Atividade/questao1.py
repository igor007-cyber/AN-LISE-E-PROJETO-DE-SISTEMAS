class VeiculoBuilder:
    def __init__(self):
        self.veiculo = None

    def build_modelo(self, modelo):
        raise NotImplementedError("Subclasses must implement this method")

    def build_motor(self, motor):
        raise NotImplementedError("Subclasses must implement this method")

    def build_cor(self, cor):
        raise NotImplementedError("Subclasses must implement this method")

    def build_acessorios(self, acessorios):
        raise NotImplementedError("Subclasses must implement this method")

    def get_veiculo(self):
        return self.veiculo


class CarroBuilder(VeiculoBuilder):
    def __init__(self):
        super().__init__()
        self.veiculo = Carro()

    def build_modelo(self, modelo):
        self.veiculo.modelo = modelo

    def build_motor(self, motor):
        self.veiculo.motor = motor

    def build_cor(self, cor):
        self.veiculo.cor = cor

    def build_acessorios(self, acessorios):
        self.veiculo.acessorios = acessorios


class Diretor:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construir_veiculo(self):
        self.builder.build_modelo("Modelo de Carro")
        self.builder.build_motor("Motor de Carro")
        self.builder.build_cor("Cor de Carro")
        self.builder.build_acessorios(["Acessório 1", "Acessório 2"])


class Carro:
    def __init__(self):
        self.modelo = None
        self.motor = None
        self.cor = None
        self.acessorios = None

    def __str__(self):
        return f"Carro: Modelo: {self.modelo}, Motor: {self.motor}, Cor: {self.cor}, Acessórios: {self.acessorios}"


if __name__ == "__main__":
    diretor = Diretor()
    carro_builder = CarroBuilder()
    diretor.set_builder(carro_builder)
    diretor.construir_veiculo()
    carro = carro_builder.get_veiculo()
    print(carro)