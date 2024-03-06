from time import sleep
def fibonacci(verif):
    num1, num2 = 0, 1

    # Gerando a sequencia de Fibonacci até o numero informado
    while num2 < verif:
        num1, num2 = num2, num1 + num2

    # Verificando se o numero informado pertence a sequencia de Fibonacci criada
    if num2 == verif:
        return True
    else:
        return False
print('-=' * 30)
print('                  VERIFICAÇÃO DE FIBONACCI')
print('-=' * 30)
numero = int(input("Informe um número: "))
print('-=' * 30)

if fibonacci(numero):
    print(f"O Numero {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O Numero {numero} não pertence à sequência de Fibonacci.")
print('-=' * 30)
print('Finalizando Aplicação...')
sleep(1)
print('Aplicação Finalizada!')











