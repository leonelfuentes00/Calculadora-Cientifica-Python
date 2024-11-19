import tkinter as tk
from tkinter import messagebox
from scipy.integrate import quad
from math import sin, pi

class Calculator:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            messagebox.showerror("Error", "División por cero")
            return None
    
    def potencia(self, a, b):
        return a ** b

    def integrar(self, funcion, limites, parametros):
        try:
            if funcion == "polinomio":
                a, n = parametros
                f = lambda x: a * x**n
            elif funcion == "cuadratica":
                a, b, c = parametros
                f = lambda x: a * x**2 + b * x + c
            elif funcion == "trigonometrica":
                A, k = parametros
                f = lambda x: A * sin(k * x)
            else:
                raise ValueError("Función no válida")

            # Resolver integral
            resultado, error = quad(f, limites[0], limites[1])
            return resultado, error
        except Exception as e:
            raise ValueError(f"Error al calcular la integral: {str(e)}")