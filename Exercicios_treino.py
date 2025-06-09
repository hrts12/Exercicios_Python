#curso  de algoritimos em py
print("inicio do curso de algoritimos")

#1
print("hello world")

#2
impressao_1 = int(input("digite um valor: "))

print(impressao_1)

#3
a2 = int(input("digite o primeiro valor: "))
b2 = int(input("digite o segundo valor: "))

print(a2 + b2)

#4
prova1 = int(input("digite a nota da prova: "))
prova2= int(input("digite a nota da prova: "))
prova3 = int(input("digite a nota da prova: "))
prova4 = int(input("digite a nota da prova: "))
media_prova = (prova1 + prova2 + prova3 + prova4) // 4

print(media_prova)

#5
metros = int(input("digite uma quantia de metros: "))
centimetros = metros * 100

print(centimetros)

#6
raio_do_circulo = float(input("digite o raio do circulo: "))
area_do_circulo = 3.14 * (raio_do_circulo ** 2)

print(area_do_circulo)

#7
altura_quadrado = int(input("digite a aultura do  quadrado: "))
area_quadrado = altura_quadrado ** 2
dobro = area_quadrado * 2

print(dobro)

#8
recebimento_hora = float(input("quanto vc recebe por hora: "))
horas_mensais = int(input("quantas horas vc trabalha por mes: "))
salario = recebimento_hora * horas_mensais

print(salario)

#9
farenheit = int(input("quantos graus esta: "))
conversao_celsius = (5 * (farenheit - 32) / 9)

print(conversao_celsius)

#10
celsius = int(input("quantos graus esta: "))
conversao_farenheit = ((celsius * 9) / 5) + 32

print(conversao_farenheit)

#11
numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))
numero3 = float(input("digite o terceiro numero: "))
resultado1 = (numero1) + numero2 / 2
resultado2 = (numero3) + numero1 * 3
resultado3 = numero3 ** 2

print(resultado1)
print(resultado2)
print(resultado3)

#12
altura = float(input("digite sua altura: "))
peso_ideal = (72.7 * altura) - 58

print(peso_ideal)

#13
altura_H = float(input("digite a altura do homem: "))
altura_M = float(input("digite a altura da mulher: "))
peso_ideal_H = (72.7 * altura_H) - 58
peso_ideal_M = (62.1 * altura_M) - 44

print(peso_ideal_H)
print(peso_ideal_M)

#14
peso = float(input("digite o peso da pesca em kg: "))
excesso = peso - 50
multa = excesso * 4

print(multa)

#15
recebimento_hora1 = float(input("quanto vc recebe por hora: "))
horas_mensais1 = float(input("quantas horas vc trabalha por mes: "))
salario1 = recebimento_hora1 * horas_mensais1
imposto = salario1 * 0.11
sindicato = salario1 * 0.05
inss = salario1 * 0.08
salario1_liquido = salario1 - imposto - sindicato - inss

print(salario1)
print(imposto)
print(sindicato)
print(inss)
print("salario liquido é de" , salario1_liquido)

#16
import math
metros_quadrados = float(input('Digite quantos metros quadrados você vai pintar: '))
latas = math.ceil(metros_quadrados/54)
preco = latas * 80
print('Você precisa comprar', latas, 'lata(s), custando', preco)

#17
import math
metrosQuadrados = float(input('Digite os m²: '))
metrosQuadradosMaisDez = metrosQuadrados * 1.0
rendimentoLitro = 6
litrosLata = 18
precoLata = 80
rendimentoLata = rendimentoLitro * litrosLata
litrosGalao = 3.6
precoGalao = 25
rendimentoGalao = rendimentoLitro * litrosGalao
 
somenteLatas = math.ceil(metrosQuadrados / rendimentoLata)
somenteGaloes = math.ceil(metrosQuadrados / rendimentoGalao)
latas = math.floor(metrosQuadradosMaisDez / rendimentoLata)
galoes = math.ceil((metrosQuadradosMaisDez % rendimentoLata) / rendimentoGalao)
 
print(
    f'Somente Latas: {somenteLatas}, custando R${somenteLatas * precoLata}\n'
    f'Somente Galões: {somenteGaloes}, custando R${somenteGaloes * precoGalao}\n'
    f'Latas: {latas} , Galões: {galoes}, '
    f'custando R${((latas * precoLata) + (galoes *precoGalao)):.2f}')

#18
tamanho_arquivo = int(input("qual o tamanho do arquivo em MB: "))
velocidade_arquivo = int(input("qual a velocidade da conexao em Mps: "))
tempos = (tamanho_arquivo * 8) / velocidade_arquivo
minutos = tempos // 60
segundos = tempos % 100

print('minutos:', minutos, 'segundos:', segundos)

#19
number1 = int(input("digite numero aqui: "))
number2 = int(input("digite numero aqui: "))

if(number1 > number2):
    print(number1, "é o maior numero")
else:
    print(number2, "é o maior numero")

#20
numbero_P_N = int(input("digite numero aqui: "))

if(numbero_P_N == True):
    print("é positivo")
else:
    print("é negativo")

#21
sexo = input("digite f para feminimo e m para masculino: ")

if(sexo == "f" or sexo == "F"):
    print("feminino")
elif(sexo == "m" or sexo == "M"):
    print("masculino")
else:
    print("sexo invalido")

#22
vogal_consoante = input("digite uma letra: ")

if(vogal_consoante == "a" or vogal_consoante == "e" or vogal_consoante == "i" or vogal_consoante == "o" or vogal_consoante == "u"):
    print("é vogal")
else:
    print("é consoante")

#23
nota1 =int(input("digite uma nota: "))
nota2 =int(input("digite uma nota: "))

media = (nota1 + nota2) / 2
if(media == 10):
    print("aprovado com distinçao")
elif(media >= 7):
    print("aprovado")
else:
    print("reprovado")

#24
N1 = int(input("digite numero aqui: "))
N2 = int(input("digite numero aqui: "))
N3 = int(input("digite numero aqui: "))

if(N1 > N2 and N1 > N3):
    print(N1, "é o maoir numero")
elif(N2 > N1 and N2 > N3):
    print(N2, "é o maoir numero")
else:
    print(N3, "é o maoir numero")

#25
N1 = int(input("digite numero aqui: "))
N2 = int(input("digite numero aqui: "))
N3 = int(input("digite numero aqui: "))

if(N1 > N2 and N1 > N3):
    print(N1, "é o maoir numero")
elif(N2 > N1 and N2 > N3):
    print(N2, "é o maoir numero")
else:
    print(N3, "é o maoir numero")

if(N1 < N2 and N1 < N3):
    print(N1, "é o menor numero")
elif(N2 < N1 and N2 < N3):
    print(N2, "é o menor numero")
else:
    print(N3, "é o menor numero")

#26
preco_prod1 = int(input("digite preco do primeiro produto aqui: "))
preco_prod2 = int(input("digite preco do segundo produto aqui: "))
preco_prod3 = int(input("digite preco do terceiro produto aqui: "))

if(preco_prod1 < preco_prod2 and preco_prod1 < preco_prod3):
    print("compre  o primeiro produto")
elif(preco_prod2 < preco_prod1 and preco_prod2 < preco_prod3):
    print("compre  o sugundo produto")
else:
    print("compre o terceiro produto")

#27
numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite outro numero: "))
numero_3 = int(input("Digite mais um numero: "))

if numero_1 > numero_2 > numero_3:
    print(numero_1, numero_2, numero_3)
elif numero_1 > numero_3 > numero_2:
    print(numero_1, numero_3, numero_2)
elif numero_2 > numero_1 > numero_3:
    print(numero_2, numero_1, numero_3)
elif numero_2 > numero_3 > numero_1:
    print(numero_2, numero_3, numero_1)
elif numero_3 > numero_1 > numero_2:
    print(numero_3, numero_1, numero_2)
else:
    print(numero_3, numero_2, numero_1)

#28
turno_de_estudo = input("Em qual turno você estuda: ")

if(turno_de_estudo == "manha" or turno_de_estudo == "Manha"):
    print("Bom dia")
elif(turno_de_estudo == "tarde" or turno_de_estudo == "Tarde"):
    print("Boa tarde")
elif(turno_de_estudo == "noite" or turno_de_estudo == "Noite"):
    print("Boa noite")
else:
    print("Valor invalido")

#29
salario_antes_d_reajuste = int(input("digite o seu salario anterior: "))

porcentagem_d_aumento = 0
valor_d_aumento = 0
salario_atual = 0
if(salario_antes_d_reajuste <= 280):
    porcentagem_d_aumento = 20
elif(salario_antes_d_reajuste <= 750):
    porcentagem_d_aumento = 15
elif(salario_antes_d_reajuste <= 1500):
    porcentagem_d_aumento = 10
else:
    porcentagem_d_aumento = 5

valor_d_aumento = salario_antes_d_reajuste * (porcentagem_d_aumento / 100)
salario_atual = salario_antes_d_reajuste + valor_d_aumento

print(salario_antes_d_reajuste)
print(porcentagem_d_aumento)
print(valor_d_aumento)
print(salario_atual)

#30
valorDaHora = float(input("Digite quanto você recebe por hora: "))
horasTrabalhadas = float(input("Digite quantas horas você trabalhou esse mês: "))
salarioBruto = valorDaHora * horasTrabalhadas

if salarioBruto <= 900:
    descontoIr = 0.0
elif salarioBruto <= 1500:
    descontoIr = 5
elif salarioBruto <= 2500:
    descontoIr = 10
else:
    descontoIr = 20
 
IR = salarioBruto * (descontoIr / 100)
INSS = salarioBruto * (10 / 100)
FGTS = salarioBruto * (11 / 100)
totalDeDescontos = IR + INSS
salarioLiquido = salarioBruto - totalDeDescontos
 
print(
    f'\nSalário Bruto     : R${salarioBruto:.2f}',
    f'\n(-) IR (5%)       : R${IR:.2f}',
    f'\n(-) INSS ( 10%)   : R${INSS:.2f}',
    f'\nFGTS (11%)        : R${FGTS:.2f}',
    f'\nTotal de descontos: R${totalDeDescontos:.2f}',
    f'\nSalário Liquido   : R${salarioLiquido:.2f}'
)

#31
dia = 1

while(dia >=1 and dia <= 7):
 dia = int(input("Digite um numero de 1 a 7: "))

 if(dia == 1):
    print("domingo")
 elif(dia == 2):
    print("segunda")
 elif(dia == 3):
    print("terça")
 elif(dia == 4):
    print("quarta")
 elif(dia == 5):
    print("quinta")
 elif(dia == 6):
    print("sexta")
 elif(dia == 7):
     print("sabado")
 else:
    dia = 0

#32
nota1 = float(input("digite sua nota: "))
nota2 = float(input("digite sua nota: "))
conceito = " "
media = (nota1 + nota2) / 2

if(media == 9 or media == 10):
    conceito = "A"
elif(media >= 7.5 and media < 9):
    conceito = "B"
elif(media >= 6 and media < 7.5):
    conceito = "C"
elif(media >= 4 and media < 6):
    conceito = "D"
else:
    conceito = "E"

print(
    f'\nmedia de aproveitamento','conceito'
    f'\n   {nota1} e {nota2}           ', {conceito}
)

#33
lado1 = int(input("tamanho do lado: "))
lado2 = int(input("tamanho do lado: "))
lado3 = int(input("tamanho do lado: "))

if((lado1 + lado2) > lado3 and (lado1 + lado3) > lado2 and (lado2 + lado3) > lado1):
    print("é um triangulo")
elif(lado1 == lado2 and lado1 == lado3 and lado2 == lado3):
    print("é um triangulo equilatero")
elif(lado1 == lado2 or lado1 == lado3 or lado2 == lado3):
    print("é um triangulo sósceles")
else:
    print("é um tringulo escaleno")

#34
a = float(input('Digite o valor de a: '))

if a == 0:
    print('Não é uma equação do segundo grau')
else:
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('Delta menor que 0. Não há raízes reais.')
    elif delta == 0:
        raiz = (-b)/(2 * a)
        print(f'Delta é zero. A raíz é {raiz}')
    else:
        raiz1 = (-b + (delta ** (1/2)))/(2 * a)
        raiz2 = (-b - (delta ** (1/2)))/(2 * a)
        print(f'Delta maior que zero. A raíz 1 é {raiz1}, e a raiz 2 é {raiz2}')

#35
ano = float(input("digite um ano: "))

if(ano % 4 == 0):
    print("é ano bissexto")
else:
    print("nao é ano bissexto")

#36
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split('/') 
dia, mes, ano = int(dia), int(mes), int(ano)
 
if ano < 0:
    print("Ano inválido!")
else:
    if mes < 1 or mes > 12:
        print("Mês inválido!")
    elif mes in [1,3,5,7,8,10,12]:
        if dia > 0 and dia < 32:
            print("Data válida!")
        else:
            print("Dia inválido!")
    elif mes in [4,6,9,11]:
        if dia > 0 and dia < 31:
            print("Data válida!")
        else:
            print("Dia inválido!")
    else:
        if ano % 4 == 0:
            if dia > 0 and dia < 30:
                print("Data válida!")
            else:
                print("Dia inválido!")
        else:
            if dia > 0 and dia < 29:
                print("Data válida!")
            else:
                print("Dia inválido!")

#37
for numero in [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 , 16]:
    print(f"\nNumero: {numero}")
    unidade = numero % 10
    dezena = (numero % 100) // 10
    centena = numero // 100
    separador1 = ""
    separador2 = ""
    if centena > 0 and dezena > 0 and unidade > 0: 
        separador1 = " , "
        separador2 = " e "
    elif centena > 0 and dezena > 0:
        separador1 = " e "
        separador2 = ""
    elif (centena > 0 and unidade > 0) or (dezena > 0 and unidade > 0):
        separador1 = ""
        separador2 = " e "
    if centena > 0:
        if centena == 1:
            centena = "1 centena"
        else:
            centena = f"{centena} centenas"
    else:
        centena = ""
    if dezena > 0:
        if dezena == 1:
            dezena = "1 dezena"
        else:
            dezena = f"{dezena} dezenas"
    else:
        dezena = ""
    if unidade > 0:
        if unidade == 1:
            unidade = "1 unidade"
        else:
            unidade = f"{unidade} unidades"
    else:
        unidade = ""
 
    print(f"{centena}{separador1}{dezena}{separador2}{unidade}")

#38
valor = int(input("Digite o valor a ser sacado (entre 10 e 600): "))

if (valor < 10 or valor > 600):
    print("Valor inválido!")
else:
    cem = valor // 100
    valor -= cem * 100
    cinquenta = valor // 50
    valor -= cinquenta * 50
    dez = valor // 10
    valor -= dez * 10
    cinco = valor // 5
    valor -= cinco * 5
    um = valor
    if (cem > 0):
        print(f"{cem} nota(s) de cem")
    if (cinquenta > 0):
        print(f"{cinquenta} nota(s) de cinquenta")
    if (dez > 0):
        print(f"{dez} nota(s) de dez")
    if (cinco > 0):
        print(f"{cinco} nota(s) de cinco")
    if (um > 0):
        print(f"{um} nota(s) de um")

#39
x = int(input("digite um numero: "))

if(x % 2 == 0):
    print("é par")
else: 
    print("e impar")

#40
y = float(input("digite um numero: "))

if(y % 1 == 0):
    print("inteiro")
else: 
    print("decimal")

#41
numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite outro número: "))
op = input("Digite qual operação (+, -, * ou /) deseja realizar: ")
if (op == '+'):
    resultado = numero1 + numero2
elif (op == '-'):
    resultado = numero1 - numero2
elif (op == '*'):
    resultado = numero1 * numero2
elif (op == '/'):
    resultado = numero1 / numero2
 
print("\nO resultado é: ")
 
if ((resultado//1) % 2 == 0):
    print("Par")
else:
    print("Ímpar")
 
if (resultado >= 0):
    print("Positivo")
else:
    print("Negativo")
 
if (resultado % 1 == 0):
    print("Inteiro")
else:
    print("decimal")

#42
contador = 0
pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")
if(pergunta1 == "sim" or pergunta1 == "Sim"):
    contador = 1
if(pergunta2 == "sim" or pergunta2 == "Sim"):
    contador = 2
if(pergunta3 == "sim" or pergunta3 == "Sim"):
    contador = 3
if(pergunta4 == "sim" or pergunta4 == "Sim"):
    contador = 4
if(pergunta4 == "sim" or pergunta4 == "Sim"):
    contador = 5

  
if(contador < 2):
    print("inocente")
elif(contador == 2):
    print("suspeito")
elif(contador < 5):
    print("cumplice")
else:
    print("assasino")

#43
litros = float(input("Digite quantos litros você quer abastecer: "))
combustivel = input("Digite A para álcool ou G para gasolina: ")
 
if (combustivel == 'A' or combustivel == 'a'):
    preco = litros * 1.9
    if (litros <= 20):
        preco -= 1.9 * litros * 3 / 100
    else:
        preco -= 1.9 * litros * 5 / 100
elif (combustivel == 'G' or combustivel == 'g'):
    preco = litros * 2.5
    if (litros <= 20):
        preco -= 2.5 * litros * 4 / 100
    else:
        preco -= 2.5 * litros * 6 / 100
print(f"O preço a pagar é R${preco:.2f}")

#44
morango = float(input("Digite quantos quilos de morango foram comprados: "))
maca = float(input("Digite quantos quilos de maçã foram comprados: "))
valor = 0
 
if (morango <= 5):
    valor += morango * 2.5
else:
    valor += morango * 2.2
if (maca <= 5):
    valor += maca * 1.8
else:
    valor += maca * 1.5
 
if ((morango + maca) > 8 or valor > 25):
    valor -= valor * 10 / 100
 
print(f"O valor a ser pago é R${valor:.2f}")

#45
carne = input("Digite F para filé duplo, A para alcatra e P para picanha: ")
peso = float(input("Digite quantos quilos dessa carne vai comprar: "))
pagamento = input("Dinheiro ou cartão tabajara (5% de desconto)? D ou C: ")
preco_total = 0
 
print("\nHipermercado Tabajara\nCupom fiscal\n")
if (carne == 'F' or carne == 'f'):
    print("Item: Filé Duplo")
    if (peso > 5):
        preco_total = peso * 5.8
    else:
        preco_total = peso * 4.9
elif (carne == 'A' or carne == 'a'):
    print("Item: Alcatra")
    if (peso > 5):
        preco_total = peso * 6.8
    else:
        preco_total = peso * 5.9
elif (carne == 'P' or carne == 'p'):
    print("Item: Picanha")
    if (peso > 5):
        preco_total = peso * 7.8
    else:
        preco_total = peso * 6.9
print(f"Quantidade: {peso:.2f}Kg")
print(f"Preço total: R${preco_total:.2f}")
if (pagamento == 'D' or pagamento == 'd'):
    print("Tipo de pagamento: Dinheiro")
    desconto = 0
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")
elif (pagamento == 'C' or pagamento == 'c'):
    print("Tipo de pagamento: Cartão Tabajara")
    desconto = preco_total * 5 / 100
    print(f"Desconto: R${desconto:.2f}")
    print(f"Valor a pagar: R${(preco_total - desconto):.2f}")

#46
nota = int(input("digite sua nota de 0 a 10: "))
while(nota < 0 or nota > 10):
    print("nota invalida!")
    nota = int(input("digite sua nota de 0 a 10 novamente: "))

#47
usuario = input("usuario: ")
senha = input("senha: ")

while(usuario == senha):
    print("senha ou usuario invalido")
    usuario = input("usuario: ")
    senha = input("senha: ")

#48
nome = input("seu nome: ")
while len(nome) < 4:
    print("nome invalido")
    nome = input("seu nome: ")
print("nome valido")

idade = int(input("sua idade: "))
while(idade < 0 or idade > 150):
    print("idade invalido")
    idade = int(input("sua idade: "))
print("idade valida")

salario = int(input("seu salario: "))
while(salario < 0):
    print("salario invalido")
    salario = int(input("seu salario: "))
print("salario valido")

sexo = input("seu sexo: ")
while(sexo != "f" and sexo != "m"):
    print("sexo invalido")
    sexo = input("seu sexo: ")
print("sexo valido")

EstadoCivil = input("seu estado civil: ")
while(EstadoCivil != "s" and EstadoCivil != "c" and EstadoCivil != "v" and EstadoCivil != "d"):
    print("estado civil invalido")
    EstadoCivil = input("seu estado civil: ")
print("estado civil valido")

#49
populacaoA = 80000
populacaoB = 200000
anos = 0
crescimentoA = 0.03
crescimentoB = 0.015

while(populacaoA <= populacaoB):
    populacaoA += populacaoA * crescimentoA
    populacaoB += populacaoB * crescimentoB
    anos += 1

print("a populaçao A vai chegar na populaçao B nessa quantia de anos",anos)

#50
populacaoA = int(input("digite a populaçao do pais A: "))
populacaoB = int(input("digite a populaçao do pais B: "))
anos = 0
crescimentoA = float(input("digite a taxa de crescimento do pais A: "))
crescimentoB = float(input("digite a taxa de crescimento do pais B: "))

while(populacaoA == int and populacaoB == int and crescimentoA == float and crescimentoB == float):
    print("so é permitido numeros!")
    populacaoA = int(input("digite a populaçao do pais A: "))
    populacaoB = int(input("digite a populaçao do pais B: "))
    crescimentoA = float(input("digite a taxa de cescimento do pais A: "))
    crescimentoB = float(input("digite a taxa de crescimento do pais B: "))

while(populacaoA <= populacaoB):
    populacaoA += populacaoA * crescimentoA
    populacaoB += populacaoB * crescimentoB
    anos += 1

print("a populaçao A vai chegar na populaçao B nessa quantia de anos",anos)

#51
def Calculo_temp(Loop):

    while Loop == 0:
        try:
            opcoes = int(input('Em qual temperatura você deseja saber o valor? \n1 - Fahrenheit \n2 - Celsius\n'))
            
            if opcoes == 1:
                temperatura_c = int(input("Digite o valor da temperatura em Celsius: "))
                temperatura_f = (temperatura_c * 9/5) + 32
                print(f'{temperatura_f:.0f} Fahrenheit')
                Loop = 1
                
            elif opcoes == 2:
                temperatura_f = int(input("Digite o valor da temperatura em Fahrenheit: "))
                temperatura_c = (temperatura_f - 32) * 5/9
                print(f'{temperatura_c:.0f} Celsius')
                Loop = 1
                
            else:
                print("Opção inválida. Digite 1 ou 2.")
                Loop = 0
        
        except ValueError:
            print('Entrada inválida. Digite apenas números.')
            Loop = 0

Calculo_temp(0)

#52
import re

def Validador_senha():

    print("A senha precisa de maisculas, minusculas, numeros e caracteres especiais")
    senha = input("Digite uma senha: ")
    regex_MA = re.search(r"[A-Z]", senha)
    regex_MI = re.search(r"[a-z]", senha)
    regex_N = re.search(r"[0-9]", senha)
    regex_E = re.search(r"[^a-zA-Z0-9]", senha)

    if len(senha) < 8:
        print("Senha invalida, numero minimo de 8 caracteres")
    elif (regex_MA and regex_MI and regex_N and regex_E):
        print("Validado")
    else:
        if not regex_MA:
            print("Desvalidado, não possui letras maiusculas")
        if not regex_MI:
            print("Desvalidado, não possui letras minusculas")
        if not regex_N:
            print("Desvalidado, não possui numeros")
        if not regex_E:
            print("Desvalidado, não possui caracteres especiais")

Validador_senha()

#53
def manipular_list(list):

    if len(list) == 3:
        print(sum(list))

    elif len(list) == 2:
        print(list[0] * list[1])

    else:
        for i in range(len(list)-1):
            print(list[i] - list[i+1])

#54
class Animal:
    def __init__(self, raca, nome, cor):
        self.raca = raca
        self.nome = nome
        self.cor = cor

    def __str__(self):
        return "Fazendo absolutamene nada"

    def andar(self):
        return "Voce comecou a andar"

    def apresentar(self):
        return f'Oi, eu me chamo {self.nome} e sou um {self.raca}'


class Humano(Animal):
    def __init__(self,apelido):
        super().__init__("Humano", apelido, "branco")
        self.apelido = apelido

    def desenhar(self):
        querer = input("voce quer desenhar? ")
        if querer.lower() == "sim":
            return "voce desenhou algo"
        else:
            return "voce nao desenhou"

vida = Animal("Humano", "Felipe", "branco")
ser_vivo = Humano("Haritos")
print(ser_vivo.desenhar())

#55
import requests
url = "https://jsonplaceholder.typicode.com/posts/1"

api = requests.get(url)

if api.status_code == 200:
    data = api.json()
    print(data)
else:
    print(f'Erro foi gerado {api.status_code}')
