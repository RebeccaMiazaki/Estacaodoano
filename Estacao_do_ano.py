#Projeto Estação do Ano

#Apresentação
print('\n\t\t\t -- Estação do ano -- \n\n\t')

#Entrada
dia=int(input('Informe o dia: '))
mes=int(input('Informe o mês: '))

#Processamento e Saída
if mes==12 and dia>=22 or mes==1 or mes==2 or mes==3 and dia<20:
    print(f'Verão dia {dia} de{mes} de 2023')

elif mes==3 and dia >=20 or mes==4 or mes==5 or mes==6 and dia<21:
    print(f'Outono dia: {dia} de {mes} de 2023')

elif mes==6 and dia >=21 or mes==7 or mes==8 or mes==9 and dia<23:
    print(f'Inverno dia {dia} de {mes} de 2023')

elif mes==9 and dia >=23 or mes==10 or mes==11 or mes==12 and dia <22:
    print(f'Primavera dia {dia} de {mes} de 2023')

else:
    print('Mês inválido')
