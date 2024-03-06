from time import sleep

print('-=' * 30)
print('                     INVERSOR DE STRING')
print('-=' * 30)

string = str(input('Digite uma palavra ou frase que deseja inverter: '))
print('-=' * 30)

#invertendo String sem utilizar o reverse
invertida = string[::-1]

print(f'A string invertida é: {invertida}')
print('-=' * 30)

print('Finalizando Aplicação...')
sleep(1)
print('Aplicação Finalizada!')