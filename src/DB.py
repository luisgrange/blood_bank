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
 
    # def tableJoin(self):
    #     query = 'SELECT t1.*, t2.* FROM '+self.table+' as t1 INNER JOIN %s as t2 ON t2.'