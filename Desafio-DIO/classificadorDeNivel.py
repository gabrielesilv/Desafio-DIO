# Desafio Classificador de nível de Herói

#**O Que deve ser utilizado**

#- Variáveis
#- Operadores
#- Laços de repetição
#- Estruturas de decisões

## Objetivo

#Crie uma variável para armazenar o nome e a quantidade de experiência (XP) de um herói, depois utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo:

#Se XP for menor do que 1.000 = Ferro
#Se XP for entre 1.001 e 2.000 = Bronze
#Se XP for entre 2.001 e 5.000 = Prata
#Se XP for entre 5.001 e 7.000 = Ouro
#Se XP for entre 7.001 e 8.000 = Platina
#Se XP for entre 8.001 e 9.000 = Ascendente
#Se XP for entre 9.001 e 10.000= Imortal
#Se XP for maior ou igual a 10.001 = Radiante

## Saída
#Ao final deve se exibir uma mensagem:"O Herói de nome **{nome}** está no nível de **{nivel}**"

heroiXP = 6789
nome = "Sage"

if heroiXP <= 1000:
    print("Ferro")
elif heroiXP <= 2000:
    print("Bronze")
elif heroiXP <= 5000:
    print("Prata")
elif heroiXP <= 7000:
    print("Ouro")
elif heroiXP <= 8000:
    print("Platina")
elif heroiXP <= 9000:
    print("Ascendente")
elif heroiXP <= 10000:
    print("Imortal")
else:
    print("Radiante")

print(f'O herói de nome {nome} está no nível {heroiXP}')
