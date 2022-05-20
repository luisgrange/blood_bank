from src.DB import *

class Hospital(DB):
    def __init__(self, table, conn, cursor):
        super().__init__(table, conn, cursor)
    
    def inserir(self):
        nome, alas, funcionarios = input('Digite com espaços => Nome do hospital    Alas    QTD funcionários: ').split()
        query = ' INSERT INTO ' + self.table + ' (nome, alas, funcionarios) VALUES (%s,%s,%s)'

        try:
            self.cursor.execute(query, (nome, alas, funcionarios))
            self.conn.commit()
            print(f'Nova entrada adicionado ao banco')
        except:
            self.conn.rollback()


    
    def editar(self):
        query = 'UPDATE '+self.table+' SET nome="%s"  WHERE id= %s'

        try:
            id = int(input('Digite o ID que deseja alterar: '))
            campos = input('Digite o novo nome do hospital: ')

            self.cursor.execute(query, (campos, id))
            self.conn.commit()

            print(f'#{id} foi alterado com sucesso!\n')

        except:
            self.conn.rollback()
    
    