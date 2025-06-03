
import sqlite3

#menu principal do sistema
def main_menu() -> str:
    print("\n1.sistema de cadastro de aluno ")
    print("1. cadastras aluno")  
    print("2. listar aluno") 
    print("3. atualizar aluno")
    print("4. excluir aluno")
    print("5. sair")

    opcao:str = input("escolha uma opção")
    return opcao
    
def create_table():
    conexao =  sqlite3.connect("C:/Projetos/Backend/escola01.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aluno(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOTE NOLL,
                    email TEXT NOT NULL UNIQUE,
                    idade INTEGER
                    )

        """)
    conexao.commit()
    conexao.close()

#funcao para cadastrar o alumo no BD
def register(nome:str , email:str , idade:int ):
    conexao = sqlite3.connect("C:/Projetos/Backend/escola01.db")
    cursor = conexao.cursor()

    try:
        cursor.execute("INSERT INTO aluno (nome, email, idade) VALUES (?,?,?)", 
                       (nome, email, idade))
        conexao.commit()
        print("aluno cadastrado com sucesso")
    except sqlite3.IntegrityError:    
        print("email ja cadastrado")
    finally:
        conexao.close()


def display():
    conexao = sqlite3.connect("C:/Projetos/Backend/escola01.db") # abrir conexao com o banco
    cursor= conexao.cursor()

    cursor.execute("SELECT * FROM aluno") 
    alunos= cursor.fetchall()

    conexao.close() # fechar a conexao com o banco 

    print("Lista de Alunos Cadastrados")

    for aluno in alunos:
        print(aluno)



def update(id,new_nome,new_email,new_idade):
    conexao = sqlite3.connect ("C:/Projetos/Backend/escola01.db")
    cursor= conexao.cursor()

    cursor.execute("UPDATE aluno SET nome = ?, email = ?, idade = ? WHERE id= ?",
                   (new_nome, new_email, new_idade, id))
    
    conexao.commit()
    conexao.close()
    print("Aluno atualizado com sucesso ")

def  delete(id=str):
    conexao = sqlite3.connect("C:/Projetos/Backend/escola01.db")
    cursor= conexao.cursor()

    cursor.execute("DELETE FROM aluno WHERE id = ? ", 
                 (id))
                    
    
    conexao.commit()
    conexao.close()
    print("aluno excluido com sucesso")

if __name__ == "__main__":
    create_table()

    while True: 
        opcao = main_menu()

        if opcao == "1":
            nome:str = input ("Nome:")
            email:str = input ("Email:")
            idade:int = int (input("Idade:"))
            register(nome, email, idade)

        elif opcao == "2":
             display()
             
        elif opcao== "3":
          id = int(input (" informe o ID do Aluno que voce quer atualizar"))
          new_nome  = input ("novo nome:")
          new_email = input ("novo email:")
          new_idade = int(input ("nova idade:"))
          update(id,new_nome,new_email,new_idade)
        
        elif opcao == "4":
            id = (input("informe o ID do aluno que voce quer excluir"))
            delete(id)

        elif opcao == "5":
            break

        else:
            print("Opçao Invádida")

            





       

    



