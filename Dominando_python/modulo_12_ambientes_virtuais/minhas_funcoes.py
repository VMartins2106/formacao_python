# funcoes criadas a parte

def somar(*args):
    return sum(args)

def multiplicar(*args):
    resultado=1
    for numero in args:
        resultado *= numero
    return resultado