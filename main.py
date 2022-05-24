# módulos utilizados
import mysql.connector
import os

# entidades do banco de dados
from src.Entity.Receptor import *
from src.Entity.Doador import *
from src.Entity.Hopsital import *
from src.Entity.Banco_sangue import *
from src.Entity.Sangue import *
from src.Entity.Enfermeiro import *
from src.Entity.Gestor_hospital import *

# seleção de opções de ações
from src.Options import *


os.system('clear' if os.name=='posix' else 'cls')
configs = {
    'user': 'root',
    'host': 'localhost',
    'database': 'blood_bank',
    'password': '',
    'use_pure': 'True'
}

try:
    connection  = mysql.connector.connect(**configs)
    cursor = connection.cursor()

    print('Banco de dados conectado\n\n')
    print('\n1 - doador\n2 - receptor\n3 - sangue\n4 - banco de sangue\n5 - Hospital\nEnfermeiro(a)\nGestor do hospital: ')
    answ = 0
    db = ''

    while answ == 0 or answ > 7:
        try:
            answ = int(input('Digite o valor da tabela que deseja consultar: '))
        except:
            print('Ocorreu um erro, tente novamente! ')

    if answ == 7:
        os.system('clear' if os.name=='posix' else 'cls')
        print('A tabela selecionada foi: 7 - gestor do hospital\n')

        db = Gestor_hospital('gestor_hospital', connection, cursor)
    elif answ == 6:
        os.system('clear' if os.name=='posix' else 'cls')
        print('A tabela selecionada foi: 6 - Enfermeiro\n')

        db = Enfermeiro('enfermeiro', connection, cursor)

    elif answ == 5:
        os.system('clear' if os.name=='posix' else 'cls')
        print('A tabela selecionada foi: 5 - Hospital\n')

        db = Hospital('hospital', connection, cursor)

    elif answ == 4:
        os.system('clear' if os.name=='posix' else 'cls')
        print('A tabela selecionada foi: 4 - Banco de sangue\n')

        db = Banco_sangue('banco_sangue', connection, cursor)

    elif answ == 3:
        os.system('clear' if os.name=='posix' else 'cls')
        print('A tabela selecionada foi: 3 - Sangue\n')

        db = Sangue('sangue', connection, cursor)

    elif answ == 2:
        os.system('clear' if os.name=='posix' else 'cls')
        print('A tabela selecionada foi: 2 - Receptor\n')

        db = Receptor('receptor', connection, cursor)

    else:
        os.system('clear' if os.name=='posix' else 'cls')
        print('A tabela selecionada foi: 1 - Doador\n')

        db = Doador('doador', connection, cursor)



    while True:
        options(db)


except mysql.connector.Error as e:
    print(e)

finally:
    cursor.close()
    connection.close()
    print('\nFechando a conexão...\n')


  