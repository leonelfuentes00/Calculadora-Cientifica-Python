import simpy as sp

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

    
def calcular_integral(funcion, *args):
    limites = args[-2:] 
    coeficientes = args[:-2]  
    x = sp.Symbol('x')
    funcion = funcion(*coeficientes, x)
    integral_definida = sp.integrate(funcion, (x, *limites))
    resultado = integral_definida.evalf()
    integral_representacion = f"Integral de {sp.latex(funcion)} desde {limites[0]} hasta {limites[1]}"
    return integral_representacion, integral_definida, resultado

def primera_funcion(a, n, limite_inf, limite_sup):
    def funcion(a, n, x):
        return a * x**n
    return calcular_integral(funcion, a, n, limite_inf, limite_sup)

def segunda_funcion(a, b, c, limite_inf, limite_sup):
    def funcion(a, b, c, x):
        return a * x**2 + b * x + c
    return calcular_integral(funcion, a, b, c, limite_inf, limite_sup)

def tercera_funcion(A, k, limite_inf, limite_sup):
    def funcion(A, k, x):
        return A * sp.sin(k * x)
    limite_inf *= sp.pi
    limite_sup *= sp.pi
    return calcular_integral(funcion, A, k, limite_inf, limite_sup)

