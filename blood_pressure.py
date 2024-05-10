# Entrada de dados
sist = int(input('Valor da pressão sistólica (mmHg): '))
diast = int(input('Valor da pressão diastólica (mmHg): '))

# Análise da pressão sanguínea
if sist >= 180 or diast >= 120:
    print('Crise hipertensiva.')
elif (sist >= 140 and sist < 180) or (diast >= 90 and diast < 120):
    print('Hipertensão estágio II')
elif (sist >= 130 and sist <= 139) or (diast >= 80 and diast <= 89):
    print('Hipertensão estágio I')
elif (sist >= 120 and sist <= 129) and diast < 80:
    print('Pressão sanguínea elevada')
elif sist < 120 and diast < 80:
    print('Pressão sanguínea normal.')