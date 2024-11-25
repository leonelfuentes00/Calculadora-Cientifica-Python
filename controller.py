from funciones import sumar, restar, multiplicar, dividir, primera_funcion, segunda_funcion, tercera_funcion

class ControladorCalculadora:    
    def operar(self, operacion, *args):
        if operacion == 'Suma':
            return sumar(*args)
        elif operacion == 'Resta':
            return restar(*args)
        elif operacion == 'Multiplicacion':
            return multiplicar(*args)
        elif operacion == 'Division':
            return dividir(*args)
        else:
            raise ValueError("Operación no válida")

    def calcular_integral(self, tipo, *args):
        if tipo == 'Primera Función':
            return primera_funcion(*args)
        elif tipo == 'Segunda Función':
            return segunda_funcion(*args)
        elif tipo == 'Tercera Función':
            return tercera_funcion(*args)
        else:
            raise ValueError("Tipo de integral no válida")
