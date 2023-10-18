#Projeto Estação do Ano

#Apresentação
print('\n\t\t\t -- Estação do ano -- \n\n\t')

#Entradas
dia=int(input('Informe o dia:\n '))
mes=int(input('Informe o mês:\n '))

#Processamento e Saída
if mes==1 or mes==2 or mes==3:
    if mes == 3 and dia >= 20:
        print('\n Outono \n')
    else:
        print('Verão')

elif mes==4 or mes==5 or mes==6:
    if mes == 6 and dia >= 21:
        print('Inverno')
    else:
        print('Outono')

elif mes==7 or mes==8 or mes==9:
    if mes == 9 and dia >=23:
        print('Primavera')
    else:
        print('Inverno')

elif  mes==10 or mes==11 or mes==12:
    if mes==12 and dia >=22:
        print('Verão')
    else:
        print(f'Primavera')

else:
    print('Mês inválido')
