from partituras.modelo.compositor import Compositor, ReglaTransposicion, ReglaFrecuencia
from partituras.modelo.lector import LectorPartituras
from partituras.modelo.errores import ErrorArchivo

def ejecutar():
    try:
        lector = LectorPartituras("partituras_ejemplo.json")
        transpositor = Compositor(ReglaTransposicion(token=2))
        frecuencimetro = Compositor(ReglaFrecuencia(token=1))

    except ErrorArchivo as e:
        print(f"Error en el sistema de archivos: {e}")


if __name__ == "__main__":
    ejecutar()

