from src.DB import *

class Banco_sangue(DB):
    def __init__(self, table, conn, cursor):
        super().__init__(table, conn, cursor)
    
    def inserir(self):
        fk_hospitalId, quantidade = input('Digite com espaços => ID do Hospital   Quantidade de sangue: ').split()
        query = ' INSERT INTO ' + self.table + ' (fk_hospitalId, quantidade) VALUES (%s,%s)'

        try:
            self.cursor.execute(query, (fk_hospitalId, quantidade))
            self.conn.commit()
            print(f'Nova entrada adicionado ao banco')
        except:
            self.conn.rollback()


    
    def editar(self):
        query = 'UPDATE '+self.table+' SET fk_hospitalId="%s"  WHERE id= %s'

        try:
            id = int(input('Digite o ID que deseja alterar: '))
            campos = input('Digite o id do hospital: ')

            self.cursor.execute(query, (campos, id))
            self.conn.commit()

            print(f'#{id} foi alterado com sucesso!\n')

        except:
            self.conn.rollback()
    
    