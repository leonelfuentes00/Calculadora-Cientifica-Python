import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from funciones.operaciones import sumar, restar, multiplicar, dividir
from funciones.integrales import calcular_integral_indefinida
from funciones.preprocesador import preprocesar_expresion
import keyboard
import threading

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Pro con Integrales")
        self.geometry("400x700")
        self.resizable(0, 0)

        self.resultado_var = tk.StringVar()
        self.crear_interfaz()

        threading.Thread(target=self.iniciar_escucha_teclado, daemon=True).start()

    def crear_interfaz(self):
        img_path = os.path.join(os.path.dirname(__file__), 'img', 'spiderman-png-137.png')
        img = Image.open(img_path).resize((100, 50), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(img)
        tk.Label(self, image=self.img).grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        pantalla = tk.Entry(self, textvariable=self.resultado_var, font=("Arial", 24), state='readonly', justify='right')
        pantalla.grid(row=1, column=0, columnspan=4, padx=10, pady=10, ipady=20)

        botones = [
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('=', 5, 2), ('+', 5, 3),
            ('∫', 6, 0), ('x', 6, 1), ('^', 6, 2), ('(', 6, 3),
            (')', 7, 0), ('C', 7, 1), ('⌫', 7, 2), ('Salir', 7, 3)
        ]

        for text, row, col in botones:
            tk.Button(self, text=text, font=("Arial", 18), width=5, height=2,
                      bg=self.obtener_color_boton(text),
                      fg="#FFFFFF" if text in ('∫', 'Salir', 'C', '⌫') else "#000000",
                      command=lambda b=text: self.ejecutar_comando_boton(b)).grid(row=row, column=col, padx=5, pady=5)

    def obtener_color_boton(self, texto):
        colores = {"=": "#FFA500", "∫": "#6A5ACD", "Salir": "#F74D4D", "C": "#FF4500", "⌫": "#FF4500"}
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
        text = self.resultado_var.get()
        if text:
            self.resultado_var.set(text[:-1])

    def clear(self):
        self.resultado_var.set("")

    def operar(self):
        try:
            expresion = self.resultado_var.get()
            if "∫" in expresion:
                self.procesar_integral(expresion)
            else:
                resultado = eval(expresion) 
                self.resultado_var.set(resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Entrada no válida: {str(e)}")

    def procesar_integral(self, expresion):
        try:
            procesada = preprocesar_expresion(expresion)
            resultado = calcular_integral_indefinida(procesada)
            self.resultado_var.set(str(resultado))
        except Exception as e:
            messagebox.showerror("Error", f"Error al calcular la integral: {str(e)}")

    def integrar(self):
        self.resultado_var.set(self.resultado_var.get() + "∫(")

    def iniciar_escucha_teclado(self):
        # Mapear teclas a funciones de la calculadora
        teclado_map = {
            'enter': lambda: self.ejecutar_comando_boton('='),
            'backspace': self.backspace,
            'c': self.clear,
            '+': lambda: self.click_boton('+'),
            '-': lambda: self.click_boton('-'),
            '*': lambda: self.click_boton('*'),
            '/': lambda: self.click_boton('/'),
            '(': lambda: self.click_boton('('),
            ')': lambda: self.click_boton(')'),
            'q': self.quit
        }
        # Agrego un mapeo
        for i in range(10):
            teclado_map[str(i)] = lambda num=i: self.click_boton(str(num))

        while True:
            for tecla, accion in teclado_map.items():
                if keyboard.is_pressed(tecla):
                    accion()
                    while keyboard.is_pressed(tecla):  # Esperar a que se suelte la tecla
                        pass
