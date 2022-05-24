
class DB:
    def __init__(self, table, conn, cursor):
        self.table = table
        self.conn = conn
        self.cursor = cursor
    

    def show(self, param='*', where=''):
        query = 'SELECT '+param+' FROM '+self.table+where
        self.cursor.execute(query)
        
        for items in self.cursor:
            for item in items:
                print(item, end='\t')
            print()
    

    def delete(self):
        id = input('Digite o ID que deseja que seja excluido: ')

        query = 'DELETE FROM ' + self.table + " WHERE id = %s"

        try:
            self.cursor.execute(query, (id,))
            self.conn.commit()
            print("\nEntrada deletado com sucesso")
            # print(self.cursor.fetchall())
        except:
            self.conn.rollback()
 
    def tableJoin(self):
         query = 'SELECT e.id, e.nome, e.tipo_sangue, f.nome, s.fk_receptorId FROM doador as e INNER JOIN sangue as s ON s.fk_doadorId = e.id INNER JOIN receptor as f ON f.id = s.fk_receptorId;'

         self.cursor.execute(query)

         for items in self.cursor:
            for item in items:
                 print(item, end='\t')
            print()
    