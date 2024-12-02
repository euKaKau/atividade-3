#Calculadora

def soma (a,b):
    return a+ b

def subtração (a, b):
    return a - b

def multiplicação (a,b):
    return a * b

def divisão (a, b):
    if b != 0:
     return a/b
    else:
        return "Erro: Divisão por zero"
    
def calculadora():
    print("Seja bem-vindo à calculadora")
    print("Escolha a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    
    try:
        opcao = int(input("Digite a operação desejada:"))
        if opcao in [1, 2, 3, 4]:
             num1 = float(input("Digite o primeiro número"))
             num2 = float(input("Digite o segundo número"))
             
             if opcao == 1:
                print(f"Resultado: {num1} + {num2} = {soma(num1, num2)}")
             elif opcao == 2:
                print(f"Resultado: {num1} - {num2} = {subtração(num1, num2)}")
             elif opcao == 3:
                print(f"Resultado: {num1} * {num2} = {multiplicação(num1, num2)}")
             elif opcao == 4:
                print(f"Resultado: {num1} / {num2} = {divisão(num1, num2)}")
        else:
            print("Opção inválida. Escolha uma operação entre 1 e 4.")
             
    except ValueError:
        print("Erro: Entrada inválida. Por favor, insira números corretamente.")