import simpy as sp

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("No se puede dividir por cero")
    
def calcular_integral(funcion, limites):
    x = sp.Symbol('x')
    integral_definida = sp.integrate(funcion, (x, limites[0], limites[1]))
    resultado = integral_definida.evalf()
    integral_representacion = f"Integral de {sp.latex(funcion)} desde {limites[0]} hasta {limites[1]}"
    return integral_representacion, integral_definida, resultado

def primera_funcion(a, n, limite_inf, limite_sup):
    x = sp.Symbol('x')
    funcion = a * x**n
    integral, resultado = calcular_integral(funcion, (limite_inf, limite_sup))
    error = abs(resultado - float(integral.evalf()))
    if error < 1e-6:
        return integral, resultado, error
    else:
        return "Error excede el limite establecido"

def segunda_funcion(a, b, c, limite_inf, limite_sup):
    x = sp.Symbol('x')
    funcion = a * x**2 + b * x + c
    integral, resultado = calcular_integral(funcion, (limite_inf, limite_sup))
    error = abs(resultado - float(integral.evalf()))
    if error < 1e-6:
        return integral, resultado, error
    else:
        return "Error excede el limite establecido"

def tercera_funcion(A, k, limite_inf, limite_sup):
    x = sp.Symbol('x')
    funcion = A * sp.sin(k * x)
    limite_inf = limite_inf * sp.pi
    limite_sup = limite_sup * sp.pi
    integral, resultado = calcular_integral(funcion, (limite_inf, limite_sup))
    error = abs(resultado - float(integral.evalf()))
    if error < 1e-6:
        return integral, resultado, error
    else:
        return "Error excede el limite establecido"
