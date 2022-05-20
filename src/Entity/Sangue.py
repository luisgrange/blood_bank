from src.DB import *

class Sangue(DB):
    def __init__(self, table, conn, cursor):
        super().__init__(table, conn, cursor)
    
    def inserir(self):
        fk_doadorId, fk_receptorId, tipo_sangue = input('Digite com espaços => ID do doador ID do receptor tipo de sangue: ').split()
        query = ' INSERT INTO ' + self.table + ' (fk_doadorId,fk_receptorId, tipo_sangue) VALUES (%s,%s,%s)'

        try:
            self.cursor.execute(query, (fk_doadorId,fk_receptorId, tipo_sangue))
            self.conn.commit()
            print(f'Nova entrada de sangue adicionado ao banco')
        except:
            self.conn.rollback()


    
    def editar(self):
        query = 'UPDATE '+self.table+' SET tipo_sangue="%s"  WHERE id= %s'

        try:
            id = int(input('Digite o ID que deseja alterar: '))
            campos = input('Digite o tipo sanguíneo: ')

            self.cursor.execute(query, (campos, id))
            self.conn.commit()

            print(f'#{id} foi alterado com sucesso!\n')

        except:
            self.conn.rollback()
    
    