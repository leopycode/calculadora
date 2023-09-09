print("\n\033[1m{:=^50}\033[m\n\n".format(" Calculadora em Python "))

def soma(a, b):
    print("\nA soma dos valores é: ", a + b)

def subtracao(a, b):
    print("\nA diferença dos valores é: ", a - b)

def produto(a, b):
    print("\nO produto dos valores é: ", a * b)

def divisao(a, b):
    print("\nA divisão dos valores é: ", a / b)

def operacao():
    print("""Que Operação deseja realizar?
    [ 1 ] Adição
    [ 2 ] Subtração
    [ 3 ] Multiplicação
    [ 4 ] Divisão""")
    op = int(input("\n>>>   "))

    while op != 1 and op != 2 and op != 3 and op != 4:
        op = int(input("\nOperação inválida. Que operação deseja realizar? "))

    a = float(input("\nDigite o primeiro valor: "))
    b = float(input("Digige o segundo valor: "))

    if op == 1:
        soma(a, b)
    elif op == 2:
        subtracao(a, b)
    elif op == 3:
        produto(a, b)
    elif op == 4:
        divisao(a, b)

operacao()
nova_op = ""

while nova_op != "N":
    nova_op = str(input("\nDeseja realizar uma nova operação (S/N)? ")).upper().strip()
    if nova_op != "S" and nova_op != "N":
        nova_op = str(input("\nDeseja realizar uma nova operação (S/N)? ")).upper().strip()
    if nova_op == "S":
        operacao()

print("\n\033[1m{:=^50}\033[m\n\n".format(" Encerrando Calculadora "))
