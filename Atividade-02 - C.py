#Programa que recebe dois numeros e imprime soma, subtração, multiplicação e divisão
num1 = input('Digite o primeiro número: ')
num2 = input('Digite o segundo número: ')
#Calculando
soma = int(num1) + int(num2)
sub = int(num1) - int(num2)
mult = int(num1) * int(num2)
div = int(num1) / int(num2)
print("--------------------------------------- Resultados ------------------------------------------------------\n")
#Imprimindo os resultados
print("A soma é: " + str(soma))
print("A diferença é: " + str(sub))
print("O produto é: "+ str(mult))
print("O quociente é: " + str(div))