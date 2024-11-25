import sympy as sp

def calcular_integral_indefinida(expresion):
    x = sp.Symbol('x')
    funcion = sp.sympify(expresion)
    return sp.integrate(funcion, x)

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
