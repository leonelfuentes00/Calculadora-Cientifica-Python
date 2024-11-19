# controlador.py

class CalculatorController:
    def __init__(self, calculator):
        self.calculator = calculator

    def realizar_operacion(self, operacion, num1, num2):
        try:
            # Lógica para manejar diferentes operaciones
            if operacion == "sumar":
                return self.calculator.sumar(num1, num2)
            elif operacion == "restar":
                return self.calculator.restar(num1, num2)
            elif operacion == "multiplicar":
                return self.calculator.multiplicar(num1, num2)
            elif operacion == "dividir":
                return self.calculator.dividir(num1, num2)
            elif operacion == "potencia":
                return self.calculator.potencia(num1, num2)
            else:
                raise ValueError("Operación no válida")
        except Exception as e:
            raise e
        
    def realizar_integracion(self, funcion, limites, parametros):
        return self.calculator.integrar(funcion, limites, parametros)