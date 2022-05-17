import mysql.connector
from src.Entity.Receptor import *
from src.Entity.Doador import *
from src.Options import *
import os


os.system('clear' if os.name=='posix' else 'cls')
configs = {
    'user': 'root',
    'host': 'localhost',
    'database': 'blood_bank',
    'password': ''
}

try:
    connection  = mysql.connector.connect(**configs)
    cursor = connection.cursor()

    print('Banco de dados conectado\n\n')
    print('\n1 - doador\n2 - receptor\n3 - banco de sangue\n4 - Enfermeiros\n5 - Hospital')
    answ = 0
    db = ''

    while answ == 0 or answ > 7:
        try:
            answ = int(input('Digite o valor da tabela que deseja consultar: '))
        except:
            print('Ocorreu um erro, tente novamente! ')

    if answ == 7:
        pass
    elif answ == 6:
        pass
    elif answ == 5:
        pass
    elif answ == 4:
        pass
    elif answ == 3:
        pass
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


  