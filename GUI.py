# GUI.py
import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp

class CalculatorUI:
    def __init__(self, root, controller):
        self.controller = controller

        root.title("Calculadora Avanzada")
        root.geometry("500x400")
        root.configure(background="#F2BC13")

        # Pestañas para diferentes funcionalidades
        self.tab_control = ttk.Notebook(root)
        
        # Tab para cálculos básicos
        self.basic_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.basic_tab, text="Cálculos Básicos")
        self.build_basic_tab()

        # Tab para integrales
        self.integral_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(self.integral_tab, text="Cálculo de Integrales")
        self.build_integral_tab()

        self.tab_control.pack(expand=1, fill="both")

    def build_basic_tab(self):
        ttk.Label(self.basic_tab, text="Número 1:").pack(pady=5)
        self.entry_num1 = ttk.Entry(self.basic_tab)
        self.entry_num1.pack(pady=5)

        ttk.Label(self.basic_tab, text="Número 2:").pack(pady=5)
        self.entry_num2 = ttk.Entry(self.basic_tab)
        self.entry_num2.pack(pady=5)

        self.operation_var = tk.StringVar(value="sumar")
        operations = [("Suma", "sumar"), ("Resta", "restar"),
                      ("Multiplicación", "multiplicar"), ("División", "dividir"),
                      ("Potencia", "potencia")]

        ttk.Label(self.basic_tab, text="Seleccione una operación:").pack(pady=5)
        for text, value in operations:
            ttk.Radiobutton(
                self.basic_tab, text=text, variable=self.operation_var, value=value
            ).pack(anchor=tk.W)

        self.calculate_button = ttk.Button(
            self.basic_tab, text="Calcular", command=self.perform_basic_operation
        )
        self.calculate_button.pack(pady=10)

        self.basic_result_label = ttk.Label(self.basic_tab, text="Resultado: ")
        self.basic_result_label.pack(pady=10)

    def build_integral_tab(self):
        ttk.Label(self.integral_tab, text="Ecuación de la función (ej.: 2*x + 3):").pack(pady=5)
        self.integral_equation_entry = ttk.Entry(self.integral_tab)
        self.integral_equation_entry.pack(pady=5)

        ttk.Label(self.integral_tab, text="Límite inferior:").pack(pady=5)
        self.integral_lower_limit_entry = ttk.Entry(self.integral_tab)
        self.integral_lower_limit_entry.pack(pady=5)

        ttk.Label(self.integral_tab, text="Límite superior:").pack(pady=5)
        self.integral_upper_limit_entry = ttk.Entry(self.integral_tab)
        self.integral_upper_limit_entry.pack(pady=5)

        self.integral_button = ttk.Button(
            self.integral_tab, text="Calcular Integral", command=self.calculate_integral
        )
        self.integral_button.pack(pady=10)

        self.integral_result_label = ttk.Label(self.integral_tab, text="Resultado: ")
        self.integral_result_label.pack(pady=10)

    def perform_basic_operation(self):
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            operation = self.operation_var.get()
            result = self.controller.realizar_operacion(operation, num1, num2)
            self.basic_result_label.config(text=f"Resultado: {result}")
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese números válidos.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def calculate_integral(self):
        try:
            # Obtener la ecuación y los límites
            equation = self.integral_equation_entry.get()
            lower_limit = float(self.integral_lower_limit_entry.get())
            upper_limit = float(self.integral_upper_limit_entry.get())

            # Crear la variable simbólica
            x = sp.symbols("x")
            func = sp.sympify(equation)

            # Resolver la integral
            integral = sp.integrate(func, (x, lower_limit, upper_limit))
            error = abs(float(sp.N(sp.integrate(func, (x, lower_limit, upper_limit)) - integral)))

            # Mostrar el resultado
            result_text = f"Integral: {integral}\nÁrea: {float(integral)}\nError: {error:.6f}"
            self.integral_result_label.config(text=result_text)
        except Exception as e:
            messagebox.showerror("Error", f"Error en el cálculo de la integral: {e}")
