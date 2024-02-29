import copy

class Forma:
    def clone(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circulo(Forma):
    def __init__(self, x, y, raio, cor):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor

    def clone(self):
        return copy.deepcopy(self)

class Retangulo(Forma):
    def __init__(self, x, y, largura, altura, cor):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.cor = cor

    def clone(self):
        return copy.deepcopy(self)

class Triangulo(Forma):
    def __init__(self, x1, y1, x2, y2, x3, y3, cor):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.cor = cor

    def clone(self):
        return copy.deepcopy(self)
    
circulo = Circulo(10, 20, 5, "vermelho")
circulo_duplicado = circulo.clone()
print(circulo_duplicado.x)  # 10
print(circulo_duplicado.y)  # 20
print(circulo_duplicado.raio)  # 5
print(circulo_duplicado.cor)  # vermelho