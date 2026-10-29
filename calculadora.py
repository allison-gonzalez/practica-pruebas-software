def _validar_numeros(a, b):
    for valor in (a, b):
        if not isinstance(valor, (int, float)) or isinstance(valor, bool):
            raise TypeError("Los valores deben ser numéricos")


def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    _validar_numeros(a, b)
    if b == 0:
        raise ValueError("No se puede dividir entre cero")
    return a / b