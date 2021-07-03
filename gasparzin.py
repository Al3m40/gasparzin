#!usr/bin/python3
import random
import os
import requests
from datetime import date
#cores
vd='\033[32m'
am='\033[33m'
vm='\033[31m'
az='\033[36m'
ng='\033[1m'
f='\033[m'
lz='\033[34m'
#variavel
con = bin = 0
data = date.today().year
#layout
os.system('clear')
print(f""" {az}
  @@@@@@@   @@@@@@   @@@@@@ @@@@@@@   @@@@@@  @@@@@@@  @@@@@@@@ @@@ @@@  @@@
 !@@       @@!  @@@ !@@     @@!  @@@ @@!  @@@ @@!  @@@      @@! @@! @@!@!@@@
 !@! @!@!@ @!@!@!@!  !@@!!  @!@@!@!  @!@!@!@! @!@!!@!     @!!   !!@ @!@@!!@!
 :!!   !!: !!:  !!!     !:! !!:      !!:  !!! !!: :!!   !!:     !!: !!:  !!!
  :: :: :   :   : : ::.: :   :        :   : :  :   : : :.::.: : :   ::    :
                                                       by@bydeathlxncer {f}""")
print(f""" {az}                                        __                 
                        _________ ______/ /_____  ___  _____
                       / ___/ __ `/ ___/ __/ __ \/ _ \/ ___/
                      / /__/ /_/ / /  / /_/ /_/ /  __(__  ) 
                      \___/\__,_/_/   \__/\____/\___/____/  
                                      

{f}""")
print(f""" {lz}     gerador de números aleatórios de cartão de credito que talvez funcione {f}""")
print(f"""         {am}                        (1) - informações do script""")
print(f"""                                 (2) - master""")
print(f"""                                 (3) - visa""")
print(f"""                                 (4) - bin """)
print(f"""                                 (5) - vazar do script {f}""")
#layouat
while True:
    op = int(input(f"""{vm}escolha uma opções:{f} """))
    cvv = random.randrange(1,999)
    mes = random.randint(1,12)
    ano = data + random.randint(1,7)
    cc = random.randrange(1,9999999999)
    if op == 3:
        bin = 407347
        con += 1
        print('[•] cartão de credito visa (quantidades geradas {})'.format(con))
        print('[+] cartão: {}{}'.format(bin, cc))
        print('[+] cvv: {}'.format(cvv))
        print('[+] validade: mês {} de {}'.format(mes, ano))
    elif op == 1:
        print("""[!] está script e para estudos não me responsabilizo por seus feito.

[✓] essa script gera números de cartões de crédito aleatórios que talvez
possam funcionar, portando não é de primeira que vai funcionar espero que entenda!...

está script é 100% educativa não me responsabilizo por seus feitos
usando está ferramenta.""")
    elif op == 2: 
        bin = 545805
        con += 1
        print('[•] cartão de credito master (quantidades geradas {})'.format(con))
        print('[+] cartão: {}{}'.format(bin, cc))
        print('[+] cvv: {}'.format(cvv))
        print('[+] validade: mês {} de {}'.format(mes, ano))
    elif op == 4:
        bin = int(input(f"""{lz}uma bin de 6 dígitos caraikkkj: {f}"""))
        con += 1
        print('[•] bin gerada (quantidades geradas {})'.format(con))
        print('[+] cartão: {}{}'.format(bin, cc))
        print('[+] cvv: {}'.format(cvv))
        print('[+] validade: mês {} de {}'.format(mes, ano))
    elif op== 5:
        print(f"""ate a próxima soldado!""")
        exit()
    elif op < 1:
        print('ate a próxima soldado!')
        break
    else:
        print('erro! faz o bagulho certo porra!')
