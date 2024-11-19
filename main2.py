import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from controller import ControladorCalculadora
import keyboard
import os

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Pro con Integrales")
        self.geometry("400x700")
        self.resizable(0, 0)

        self.resultado_var = tk.StringVar()
        self.controlador = ControladorCalculadora()

        self.tipo_integral = tk.StringVar(value="Primera Funcion")
        self.parametros_integral = []

        self.crear_interfaz()

        # Detectar teclas presionadas
        for i in range(10):
            keyboard.on_press_key(str(i), lambda e, n=i: self.click_boton(str(n)))
        keyboard.on_press_key("enter", lambda _: self.operar())
        keyboard.on_press_key("+", lambda _: self.operar_tecla("Suma"))
        keyboard.on_press_key("-", lambda _: self.operar_tecla("Resta"))
        keyboard.on_press_key("*", lambda _: self.operar_tecla("Multiplicación"))
        keyboard.on_press_key("/", lambda _: self.operar_tecla("División"))
        keyboard.on_press_key(".", lambda _: self.click_boton("."))
        keyboard.on_press_key("c", lambda _: self.clear())
        keyboard.on_press_key("backspace", lambda _: self.backspace())

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
            if boton_text == '=':
                boton = tk.Button(self, text=boton_text, font=("Arial", 18), width=5, height=2, bg="#FFA500", fg="#000000", command=self.operar)
            elif boton_text == '∫':
                boton = tk.Button(self, text=boton_text, font=("Arial", 18), width=5, height=2, bg="#6A5ACD", fg="#FFFFFF", command=self.integrar)
            elif boton_text == 'Salir':
                boton = tk.Button(self, text=boton_text, font=("Arial", 18), width=5, height=2, bg="#F74D4D", fg="#FFFFFF", command=self.quit)
            elif boton_text == 'C':
                boton = tk.Button(self, text=boton_text, font=("Arial", 18), width=5, height=2, bg="#FF4500", fg="#FFFFFF", command=self.clear)
            elif boton_text == '⌫':
                boton = tk.Button(self, text=boton_text, font=("Arial", 18), width=5, height=2, bg="#FF4500", fg="#FFFFFF", command=self.backspace)
            else:
                boton = tk.Button(self, text=boton_text, font=("Arial", 18), width=5, height=2, bg="#87CEEB", fg="#000000", command=lambda b=boton_text: self.click_boton(b))
            boton.grid(row=fila, column=columna, padx=5, pady=5)

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
            # Evaluación de expresiones matemáticas básicas y potencias
            if '^' in expression:
                expression = expression.replace('^', '**')
            resultado = eval(expression)
            self.resultado_var.set(resultado)
        except Exception as e:
            messagebox.showerror("Error", f"Entrada no válida: {str(e)}")

    def operar_tecla(self, operacion):
        current_text = self.resultado_var.get()
        if operacion == "Suma":
            self.resultado_var.set(current_text + '+')
        elif operacion == "Resta":
            self.resultado_var.set(current_text + '-')
        elif operacion == "Multiplicación":
            self.resultado_var.set(current_text + '*')
        elif operacion == "División":
            self.resultado_var.set(current_text + '/')
        else:
            messagebox.showerror("Error", "Operación inválida")

    def integrar(self):
        # Colocar texto inicial para la integral y añadir espacio para límites
        current_text = self.resultado_var.get()
        self.resultado_var.set(f"∫({current_text}) dx")
        messagebox.showinfo("Integración", "Introduce los límites de integración y la expresión en términos de x.")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()
