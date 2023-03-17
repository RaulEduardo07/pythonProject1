#Sistema que recebe 2 numeros, efetua a soma e subtração e imprima o resultado na tela.

print("Sistema que calcula a soma de dois números! ")

#Entrada de dados

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

#Processamento

soma = a + b



print("Soma: ", soma)

c = int(input("Digite o terceiro número: "))
d = int(input("Digite o quarto número: "))

diferença = c - d

print ("Diferença: ", diferença)

#Comando if(se)
#O comando if testa uma condição. Se o resultado logico dessa condição for verdadeira o bloco de códigos é executado
#if(condição):
# - Bloco de códigos, identado.

a = 6
b = 10
if (a == 6 or b == 10):
    print("Bloco de Códigos do comando IF")
    print("A condição é verdadeira!")

elif(a == 6):
     print("Bloco de Códigos do ELIF")
     print("A condição do ELIF é verdadeira")

else:
    print("Bloco de Códigos do comando ELSE")
    print("A condição é falsa")

print("Voltando ao bloco de códigos do sitema")
