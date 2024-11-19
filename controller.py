from funciones import sumar, restar, multiplicar, dividir, primera_funcion, segunda_funcion, tercera_funcion

class ControladorCalculadora:    
    def operar(self, operacion, a, b):
        if operacion == 'Suma':
            return sumar(a, b)
        elif operacion == 'Resta':
            return restar(a, b)
        elif operacion == 'Multiplicacion':
            return multiplicar(a, b)
        elif operacion == 'Division':
            return dividir(a, b)
        else:
            raise ValueError("Operación no valida")

    def calcular_integral(self, tipo, *args):
        if tipo == 'Primera Función':
            return primera_funcion(*args)
        elif tipo == 'Segunda Función':
            return segunda_funcion(*args)
        elif tipo == 'Tercera Función':
            return tercera_funcion(*args)
        else:
            raise ValueError("Tipo de integral no valido")
        
        
