# -*- coding: utf-8 -*-
"""estruturas de repetição.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1etzQQ8qHWTopNweXmRWLpMlOvsH6ByII

# Nova seção
"""

fim = int(input('digite o numero a imprimir: '))
x = 0
while x <= fim:
   if x % 2 ==0:
    print(x)
   x += 2

x = int(input('digite o numero que deseja : '))
tab = 0
while tab <= 9:
    tab += 1
    print('{}x {}  = {}'.format(x , tab ,x * tab))

n = 1
soma = 0
while n <=3 :
  x = int(input( ' digite o valor desejado : '))
  soma= soma + x
  n= n + 1
print(f'soma: {soma}')

soma = 0
while True :
   v = int(input(f'digite o numero : '))
   soma = soma + v
   continuar = input(f'deseja continuar? (s/n) ')
   if continuar.lower() != 's' :
    break
print(f' a soma e : {soma}')



"""# lista de estrutura de repetição ♣
⚡

"""

#exercicio do slide

soma = 0
quantidade = 0
while True:
    numero = int(input('digite um numero : '))
    continuar = input('deseja continuar? (s/n) ')
    if continuar.lower() != 's' :
      break
    soma = soma+ numero
    quantidade += 1
if quantidade >=0 :
    media = soma / quantidade
    print(' a media dos numeros digitados e : ', media)
else :
  print('nenhum numero foi digitado !')

#01. Desenvolva um algoritmo que apresente todos os valores ímpares na faixa de 0 a 100
def apresentar_impares():
 numero = 1
 while numero  <= 101:
   print(numero)
   numero += 2
apresentar_impares()

#02. Faça um algoritmo para apresentar a soma dos 1000 primeiros números inteiros.
def soma_inteiros():
 soma = 0
 numero  = 1
 while numero <= 1000:
    soma += numero
    numero  += 1
 return soma
resultado = soma_inteiros()
print(f' a soma dos numeros de 1 a 1000 e :{resultado}')

#3 corrigido
qtd_numeros = int(input('digite quantos numeros desejados '))
contador = 1
soma = 0
while contador <=qtd_numeros:
  num = int(input(f'a media dos numeros digitados e ; {soma/qtd_numeros}'))
  soma += num
  contador += 1
print(f'a medida dos numeros digitados e;{soma/qtd_numeros}')

# 4 corrigido
contador = 1
soma = 0
while contador <= 500:
  if (contador % 2 == 0) and (contador % 3   == 0 ):
    soma += contador
  contador += 1
print(f'A soma dos numeros pares e multiplos de 3 e : {soma}')

#05. corrigido
qtd_numeros = int(input('digite a quantidade de numeros que deseja : '))
contador = 1
while contador <=qtd_numeros:
   num = int(input('digite um numero: '))
   if num == 0 :
    print('o numero digitado e zero ')
   elif num > 0 :
    print('o numero e postivo')
   elif num < 0 :
      print('o  numero e negativo ')
      if num != qtd_numeros:
        break

#6 Escreva um algoritmo que gere os números de 1000 a 1999 e escreva aqueles que dividido por 11 dão resto igual a 5.
contador = 1000
while contador <=1999:
  if contador % 11 == 5 :
    print(f' O numero {contador} possui resto igual a 5 ')
    contador += 1

#7
n1 =  int(input('digite o primeiro numero do intervalo: '))
n2 = int(input('digite o segundo intervaço : '))
while n1<

#8 Desenvolva um algoritmo para ler 80 números e ao final informar quantos números estão no intervalo entre 10 (inclusive) e 150 (inclusive).
contador_no_intervalo = 0
contador = 0

while contador < 2:
   num = int(input('digite um numero : '))
   if num >=10 and num <= 150:
      print(f'o numero  {num}  esta no intervalo ')
      contador_no_intervalo += 1
   else:
      print(f'o numero {num} nao esta dentro do intervalo ')
   contador += 1
print(f' os  {contador_no_intervalo}  números estão no intervalo entre 10 e 150.')

#9
contador = 1
total_m = 0
total_f = 0
while contador <= 5 :
  nome = input('digite o nome : ')
  sexo = input('digite o sexo da pessoa (M/F) : ')
  if sexo.lower()=='m':
    print(f'A pessoa {nome} e do sexo masculino')
    total_m += 1
  elif sexo.lower()== 'f':
    print(f'a pessoa {nome} e do sexo feminino ')
    total_f += 1
  else:
    print('SEXO INVALIDO')
  contador += 1
print(f'foram lidos a quantidade de {total_m} do sexo masculino e do {total_f} sexo feminino ')

# 10 corrigido
contador = 1
qtd_produtos = 2
soma_preco_custo = 0
soma_preco_venda = 0

while contador < qtd_produtos:
   preco_custo = float(input('digite o valor do preço de custo : '))
   preco_venda = float(input('digite o valor do preço da venda : '))

   soma_preco_custo += preco_custo
   soma_preco_venda+= preco_venda

   resultado= preco_venda - preco_custo

   if resultado < 0 :
    print(f'houve um prejuizo')
   elif resultado > 0:
      print(f'houve lucro ')
   else:
      print(f'houve empate na venda')

print(f'a media do preço de venda foi {soma_preco_venda / qtd_produtos}')
print(f'a media do preço de custo foi { soma_preco_custo / qtd_produtos}')

#11. Desenvolva um algoritmo que leia uma quantidade não determinada de números. Calcule a quantidade de números pares e ímpares, a média de valores pares e ímpares e a média geral dos números lidos. O número que encerrará a leitura será zero.
contador_par = 0
contador_impar = 0
somatorio_par = 0
somatorio_impar = 0
contador_total = 0
somatorio_total = 0

while True :
  numero = int(input('digite o numero desejado : '))
  if numero == 0 :
   break
  if numero % 2 == 0 :
     contador_par += 1
     somatorio_par += numero
  else:
    contador_impar +=  1
    somatorio_impar += numero
contador_total += 1
somatorio_total += num


if contador_par > 0:
  media_pares = somatorio_par / contador_par
else:
  media_pares = 0

if contador_impar > 0 :
  media_impar = somatorio_impar / contador_impar
else:
  media_impar = 0
if contador_total > 0 :
  media_geral = somatorio_total / contador_total
else:
  media_geral = 0

print(f'a quantidade de numeros pares {contador_par}')
print(f'a quantidade de numeros impares e {contador_impar} ')
print(f'a media dos numeros pares   {media_pares}')
print(f'a meedia dos numeros inpares {media_impar}')
print(f' a media geral e {media_geral}')

#12. Escreva um algoritmo para uma empresa que decide dar um reajuste a seus 584 funcionários de acordo com os seguintes critérios: a. 50% para aqueles que ganham menos do que três salários-mínimos;b. 20% para aqueles que ganham entre três até dez salários-mínimos;
contador = 1
total_do_reajuste = 0
salario_minimo = float(input('digite o seu salario '))
while contador <= 3 :
  nome =  input('digite seu nome : ')
  salario = float(input('digite o valor do seu salrio :'))
  novo_salario = salario

if salario < (salario_minimo * 3 ):
  novo_salario = salario * 1.5
elif salario < (salario_minimo * 10 ):
  novo_salario = salario * 1.2
elif salario < (salario_minimo * 20 ):
  novo_salario = salario * 1.1
else:
  novo_salario = salario * 1.50

rejuste = novo_salario - salario
total_do_reajuste += reajuste

print(f'impacto na folha de pagamento : '{total_do_reajuste : 2f})

# 13Faça um algoritmo que receba a idade de 75 pessoas e mostre uma mensagem informando“maior de idade” ou “menor de idade” para cada pessoa. Considere a idade a partir de 18anos como maior de idade.
contador = 1

while contador <= 3:
  idade = int(input('digite a sua idade : '))

if idade >= 18:
  print('maior de idade ')
else:
  print('menor de idade ')
  contador

#14
total_salario = 0
total_filhos = 0
maior_salario = 0
num_pessoas_salario_cem = 0
contador = 0

while True:
  salario = float(input('digite o seu salario '))
  if salario < 0 :
    break

  num_filhos =  int(input('digite a quantidade de filhos : '))

#15
while True
  nome = input('digite o nome : ')
  sexo = input('digite m para masculino e f para femininino : ')
  idade = int(input('digite sua idade : '))
  saude = input('digite sua condição de saude : ')

  if sexo.lower()== 'm' and indade >= 18 and saude.lower()== 'perfeita'
    print(f'{nome} esta apto para serir obrigatoriamente!')
  else:
    print(f'{nome} não esta apto para servir')

#16
contador = 1

 inteiro_k = int(input('digite o numero inteiro : '))
 numero_de_potencias = int(input('digite a potencia : '))

 while contador <= numero_de_potencia:
  resultado_potencia = inteiro_k ** contador
  print(f'{inteiro_k} elevado a {contador} = {resultado_potencia}')
  contador += 1

#17

 while True:
  numero = int(input('digite um numero ou -1 para sair : '))

  if numero == -1 :
   break

  soma += numero

  print(f' a soma final e {soma}')

#18
total_candidato_um = 0
total_candidato_dois = 0
total_candidato_tres = 0
total_candidato_quartro = 0
total_nulo = 0
total_branco = 0

while True:
  voto = int(input('digite o seu voto ou 0 para sair : '))
  if voto = 0
  break
if voto ==1
  total_candidato_um +=1

#19
numero = int(input('digite um numero: '))
contador = 1
produto = numero
if numero > 0 and numero <= 50:
  while True:
    produto =  produto * 3

    if produto >= 250:
     break

  texto = '*3' * contador
  print(f'N {texto} = {produto}')

  contador +=1

#20

#21
altura_chico = 150
altura_ze = 130
contador =  1
while True:
  altura_chico += 2
  altura_ze += 3

  if altura_ze > altura_chico:
    print (f'ze sera maior que chico em {contador} anos ')
    break
  contador +=1

#22
contador = 0
numero = int(input('digite o numero para calcular a tabuada : '))
final = int(input(' a tabuada vai ate quando '))
while contador <= final :
  resultado = numero * contador
  print(f'{numero} x {contador} = {resultado}')
  contador +=1

#23
lidos =int(input('digite a quantidade de numeros a ser lidos '))
contador = 1

while contador <= lidos:
  n = int(input('digite o numero para calcular o fatorial :'))
  fatorial = 1
  i = n

  while i > 1 :
    fatorial *= i
    i -= 1
  print(f' o fatorial de {n} e {fatorial}')
  contador += 1

#24
contador= 0
while contador

lista = [1,2,3,4,5,6,7,8,9,10]
pares = []
impares = []
   for elemento in lista
   if elemento % 2 == 0
   pares.append(elemento)
   impares.append(elemento)
print(f'numeros pares : {pares}')
print(f'numeros impares : {impares}')