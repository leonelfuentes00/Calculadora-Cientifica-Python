import re

def preprocesar_expresion(expresion):
    expresion = expresion.strip("∫()").strip()
    expresion = re.sub(r'(?<=[0-9])(?=[a-zA-Z])', '*', expresion)
    expresion = re.sub(r'(?<=[a-zA-Z])(?=[0-9])', '*', expresion)
    expresion = re.sub(r'(?<=[)])(?=[a-zA-Z0-9])', '*', expresion)
    expresion = re.sub(r'(?<=[(])(?=[a-zA-Z0-9])', '*', expresion)
    return expresion
