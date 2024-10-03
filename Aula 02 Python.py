#Aula de Python 02

nome = "Beline" 
idade = 26
peso = 95
import os # limpar tela 

os.system ('cls' if os.name == 'nt' else 'clear')

'''
Print em formato antigo no Python

print (nome)

print (idade)

print (peso)


print ("Meu nome é %s: "%nome)
print ("Minha idade é : %d "%idade)
print ("Meu peso desejado é : %.2f "%peso)
print ("%s tem %d anos e pesa %.2f " %(nome, idade, peso))
'''

#Print em formato mais novo no Python

print ("{} tem {} de idade e pesa {:.2f} kg.".format (nome, idade, peso))

#Print em formato mais recente no Python (Mai utilizada no Mercado)

'''
print (f"{nome} tem {idade} de idade e pesa {peso} kg.")

nome = input ("Insira um nome: ")

print (f"Meu nome é: {nome}")

idade = int (input ("Digite a idade: "))

print (f"Tenho {idade} anos")

if (idade > 17):
    print("Sou maior de idade")
else:     
    print("Sou menor de idade")
    
'''
    #Verificação Positivo Negativo
    
numero = int (input("Digite um numero:"))
    
if numero > 0: 
        print("O número é positivo")
elif numero < 0:
        print ("O número é negativo")
else:
    print("O número é Zero")