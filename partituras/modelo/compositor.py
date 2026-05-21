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
    def transformar(self, partitura: str) -> str:
        pass

    def revertir(self, partitura: str) -> str:
        pass

    def partitura_valida(self, partitura : str) -> bool:
        pass


































