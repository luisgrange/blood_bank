from src.Entity.Receptor import *
from src.Entity.Doador import *

def options(db):
    choice = input('Digite qual ação tomar: ')

    if choice == 'listar':
        db.show()
    else:
        return False