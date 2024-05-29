# Abre o arquivo para 'append'
ref_arquivo = open(r'C:\Users\enzoo\Desktop\dev\python\college-exercises\csv\salvainput.txt','a')

cont = 1
while cont <= 3:
    # Entrada de dados e escrita no arquivo
    nome = input('Informe o nome: ')
    ref_arquivo.write(f'{nome}\n')
    cont += 1
ref_arquivo.close()