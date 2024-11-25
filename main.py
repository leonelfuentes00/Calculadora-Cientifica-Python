import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from controller import ControladorCalculadora
import os
import sympy
from sympy import integrate
from sympy import symbols
import re

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Pro con Integrales")
        self.geometry("400x700")
        self.resizable(0, 0)

        self.resultado_var = tk.StringVar()
        self.controlador = ControladorCalculadora()
        self.crear_interfaz()

    def crear_interfaz(self):
        # Crear imagen y mostrarla
        img_path = os.path.join(os.path.dirname(__file__), 'img', 'spiderman-png-137.png')
        img = Image.open(img_path)
        img = img.resize((100, 50), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(img)
        label = tk.Label(self, image=self.img)
        label.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Pantalla de la calculadora
        pantalla = tk.Entry(self, textvariable=self.resultado_var, font=("Arial", 24), state='readonly', justify='right')
        pantalla.grid(row=1, column=0, columnspan=4, padx=10, pady=10, ipady=20)

        # Números, operaciones y símbolos adicionales
        botones = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('∫', 6, 0), ('x', 6, 1), ('^', 6, 2), ('(', 6, 3),
            (')', 7, 0), ('C', 7, 1), ('⌫', 7, 2), ('Salir', 7, 3)
        ]

        for boton_text, fila, columna in botones:
            boton = tk.Button(
                self,
                text=boton_text,
                font=("Arial", 18),
                width=5,
                height=2,
                bg=self.obtener_color_boton(boton_text),
                fg="#FFFFFF" if boton_text in ('∫', 'Salir', 'C', '⌫') else "#000000",
                command=lambda b=boton_text: self.ejecutar_comando_boton(b)
            )
            boton.grid(row=fila, column=columna, padx=5, pady=5)

    def obtener_color_boton(self, texto):
        colores = {
            "=": "#FFA500",
            "∫": "#6A5ACD",
            "Salir": "#F74D4D",
            "C": "#FF4500",
            "⌫": "#FF4500",
        }
        return colores.get(texto, "#87CEEB")

    def ejecutar_comando_boton(self, boton):
        if boton == '=':
            self.operar()
        elif boton == '∫':
            self.integrar()
        elif boton == 'Salir':
            self.quit()
        elif boton == 'C':
            self.clear()
        elif boton == '⌫':
            self.backspace()
        else:
            self.click_boton(boton)

    def click_boton(self, boton):
        self.resultado_var.set(self.resultado_var.get() + str(boton))

    def backspace(self):
        current_text = self.resultado_var.get()
        if current_text:
            self.resultado_var.set(current_text[:-1])

    def clear(self):
        self.resultado_var.set("")

    def operar(self):
        try:
            expression = self.resultado_var.get()

            # Procesar integrales
            if "∫" in expression:
                self.procesar_integral(expression)
            else:
                # Procesar operaciones básicas
                resultado = eval(expression)  # Evalúa expresiones simples (usando operadores básicos)
                self.resultado_var.set(resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Entrada no válida: {str(e)}")

    def procesar_integral(self, expression):
        try:
            # Eliminar el símbolo ∫ y los paréntesis alrededor
            expression = expression.strip("∫()").strip()
            
            # Preprocesar la expresión para agregar los signos de multiplicación donde falten
            expression = re.sub(r'(?<=[0-9])(?=[a-zA-Z])', '*', expression)  # Ej.: 2x -> 2*x
            expression = re.sub(r'(?<=[a-zA-Z])(?=[0-9])', '*', expression)  # Ej.: x2 -> x*2
            expression = re.sub(r'(?<=[)])(?=[a-zA-Z0-9])', '*', expression)  # Ej.: (x+1)x -> (x+1)*x
            
            x = symbols('x')  # Definir la variable simbólica
            
            # Convertir la expresión en una simbólica segura
            funcion = sympy.sympify(expression)
            
            # Calcular la integral indefinida
            resultado = integrate(funcion, x)
            
            # Mostrar el resultado
            self.resultado_var.set(str(resultado))
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la integral: {str(e)}")



    def integrar(self):
        current_text = self.resultado_var.get()
        self.resultado_var.set(current_text + "∫(")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
