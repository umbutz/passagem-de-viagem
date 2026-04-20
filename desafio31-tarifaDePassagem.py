#  Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

print('-='*15,' TARIFA DE VIAGEM ','-='*15)
viagem = float(input('Me informe a distância da sua viagem: '))
if viagem <= 200:
    pass200 = viagem *.5
    print(f'Como sua viagem será de {viagem}Km, sua tarifa será de R$0,50 por Km rodado, totalizando R${passa:.2f}.')
else: 
    passa = viagem * .45
    print(f'Sua longa viagem de {viagem}Km, terá uma tarifa de R$0,45 por Km rodado, totalizando R${passa:.2f}.')
