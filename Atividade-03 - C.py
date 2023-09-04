#Programa recebe o valor em m e converte para cm e mm
print("------------------------------- Preencha o que se pede --------------------------\n")
valor = input("Digite o valor em metros: ")

#Convertendo
ValorCM = int(valor) * 100
ValorMM = int(valor) * 1000

#Imprimindo os resultados
print("O valor em cm é:" + str(ValorCM))
print("O valor em mm é: " + str(ValorMM))