campos = input('Digite um nome: ')

query = 'UPDATE  SET nome={}'.format(campos)
query += ' WHERE id ='

print(query)
