from src.Entity.Receptor import *
from src.Entity.Doador import *

def options(db):
    choice = input('Digite qual ação tomar: ')

    if choice == 'listar':
        db.show()
    elif choice == 'deletar':
        db.delete()
    elif choice == 'inserir':
        db.inserir()
    elif choice == 'editar':
        db.editar
    else:
        return False