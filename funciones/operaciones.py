def sumar(*args):
    return sum(args)

def restar(*args):
    if len(args) < 2:
        raise ValueError("Se requieren al menos dos números para restar.")
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
    return resultado

def multiplicar(*args):
    resultado = 1
    for num in args:
        resultado *= num
    return resultado

def dividir(*args):
    if len(args) < 2:
        raise ValueError("Se requieren al menos dos números para dividir.")
    resultado = args[0]
    for num in args[1:]:
        if num == 0:
            raise ValueError("No se puede dividir por cero.")
        resultado /= num
    return resultado
