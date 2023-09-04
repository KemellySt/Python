#Programa que calcula o IMC
print("----------------------------------- Digite as informações abaixo -------------------------------------\n")
peso = input("Digite o seu peso: ")
altura = input("Digite sua altura: ")

#Convertendo e calculando
IMC = float(peso) / ((float(altura) / 100) * (float(altura) / 100) )
#Imprimindo o resultado
print("------------------------------------------ Resultado --------------------------------------------\n")
print("O seu IMC é: " + str(IMC))