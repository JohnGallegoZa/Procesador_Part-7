from abc import ABC, abstractmethod

class ReglaTransformacion(ABC):
    def __init__(self, token: int):
        self.token = token
        self.alfabeto = ["do", "re", "mi", "fa", "sol", "la", "si"]

    @abstractmethod
    def transformar(self, partitura: str) -> str:
        pass

    @abstractmethod
    def revertir(self, partitura: str) -> str:
        pass

    @abstractmethod
    def partitura_valida(self, partitura : str) -> bool:
        pass

    def encontrar_numeros_partitura(self, partitura : str) -> list:
        return [(i, char) for i, char in enumerate(partitura) if char.isdigit()]

    def encontrar_caracteres_invalidos(self, partitura : str) -> list:
        return [i for i, char in enumerate(partitura) if ord(char) > 127]


class ReglaTransposicion(ReglaTransformacion):
    def partitura_valida(self, partitura : str) -> bool:
        return True

    def transformar(self, partitura: str) -> str:
        partitura = partitura.lower()
        return ""

    def revertir(self, partitura: str) -> str:
        return ""


class ReglaFrecuencia(ReglaTransformacion):
    def partitura_valida(self, partitura : str) -> bool:
        return True

    def transformar(self, partitura : str) -> str:
        frecuencia = {"do": 261, "re": 293, "mi": 329, "fa": 349, "sol": 392, "la": 440, "si": 493}
        return ""

    def revertir(self, partitura : str) -> str:
        return ""


class Compositor:
    def __init__(self, interprete : ReglaTransformacion):
        self.interprete = interprete

    def transformar(self, partitura : str) -> str:
        return self.interprete.transformar(partitura)

    def revertir(self, partitura : str) -> str:
        return self.interprete.revertir(partitura)




































