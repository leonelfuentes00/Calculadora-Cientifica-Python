from scipy.integrate import quad
import sympy as sp

def calcular_error(funcion, *args):
    """
    Calcula el error absoluto entre la integración simbólica y la numérica.
    
    Args:
        funcion: Función lambda que representa la expresión matemática.
        *args: Coeficientes y límites de integración en orden.

    Returns:
        Error absoluto entre el resultado simbólico y numérico.
    """
    limites = args[-2:]
    coeficientes = args[:-2]
    x = sp.Symbol('x')

    # Función simbólica
    funcion_simbolica = funcion(*coeficientes, x)
    resultado_simb = sp.integrate(funcion_simbolica, (x, *limites)).evalf()

    # Función numérica
    funcion_numerica = lambda x: funcion(*coeficientes, x)
    resultado_num, _ = quad(funcion_numerica, *limites)

    # Cálculo del error absoluto
    error = abs(resultado_simb - resultado_num)
    print(f"Resultado Simbólico: {resultado_simb:.6f}")
    print(f"Resultado Numérico: {resultado_num:.6f}")
    print(f"Error Absoluto: {error:.6f}")

    return error
