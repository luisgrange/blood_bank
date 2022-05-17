from src.DB import *

class Receptor(DB):
    def __init__(self, table, conn, cursor):
        super().__init__(table, conn, cursor)
    
    def inserir(self):
        nome, tipo_sangue, idade, sexo = input('Digite com espaços => NOME TIPO SANGUÍNEO IDADE SEXO: ').split()
        query = ' INSERT INTO ' + self.table + ' (nome, tipo_sangue, idade, sexo) VALUES (%s,%s,%s,%s)'

        try:
            self.cursor.execute(query, (nome, tipo_sangue, idade, sexo))
            self.conn.commit()
            print(f'{nome} foi adicionado ao banco')
        except:
            self.conn.rollback()
    
    def editar(self):
        query = 'UPDATE '+self.table+' SET nome="%s"  WHERE id= %s'

        try:
            id = int(input('Digite o ID que deseja alterar: '))
            campos = input('Digite um nome: ')

            self.cursor.execute(query, (campos, id))
            self.conn.commit()

            print(f'#{id} foi alterado com sucesso!\n')

        except:
            self.conn.rollback()
    
    