import math

seg = int(input('Digite o tempo em segundos:'))

print('Horas: ', seg//3600)
print('Minutos: ', (seg%3600)//60)
print('Segundos: ', (seg%3600)%60)