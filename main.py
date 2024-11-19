# main.py
import tkinter as tk
from operaciones import Calculator
from GUI import CalculatorUI
from Controlador import CalculatorController

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator()
    controller = CalculatorController(calc)
    ui = CalculatorUI(root, controller)
    root.mainloop()
