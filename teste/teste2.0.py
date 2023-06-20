import sqlite3

# Função para criar a tabela no banco de dados
def criar_tabela():
    conn = sqlite3.connect('dados_alunos.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                        ra INTEGER PRIMARY KEY,
                        nome TEXT,
                        email TEXT,
                        id_imovel INTEGER,
                        dias_ausentes INTEGER
                    )''')

    conn.commit()
    conn.close()

# Função para inserir um novo aluno no banco de dados
def inserir_aluno(ra, nome, email, id_imovel, dias_ausentes):
    conn = sqlite3.connect('dados_alunos.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO alunos (ra, nome, email, id_imovel, dias_ausentes) VALUES (?, ?, ?, ?, ?)",
                   (ra, nome, email, id_imovel, dias_ausentes))

    conn.commit()
    conn.close()

# Função para buscar um aluno pelo RA
def buscar_aluno(ra):
    conn = sqlite3.connect('dados_alunos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos WHERE ra=?", (ra,))
    aluno = cursor.fetchone()

    conn.close()

    return aluno

# Função para exibir todos os alunos
def exibir_alunos():
    conn = sqlite3.connect('dados_alunos.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()

    conn.close()

    if not alunos:
        print("Não há alunos cadastrados.")
    else:
        for aluno in alunos:
            print(f"RA: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Email: {aluno[2]}")
            print(f"ID do Imóvel: {aluno[3]}")
            print(f"Dias Ausentes: {aluno[4]}")
            print()

# Código principal
criar_tabela()

while True:
    print("1. Inserir aluno")
    print("2. Buscar aluno")
    print("3. Exibir alunos")
    print("4. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        ra = int(input("RA: "))
        nome = input("Nome: ")
        email = input("Email: ")
        id_imovel = int(input("ID do Imóvel: "))
        dias_ausentes = int(input("Dias Ausentes: "))

        inserir_aluno(ra, nome, email, id_imovel, dias_ausentes)
        print("Aluno inserido com sucesso.")
        print()
    elif opcao == "2":
        ra = int(input("RA: "))
        aluno = buscar_aluno(ra)

        if aluno:
            print(f"RA: {aluno[0]}")
            print(f"Nome: {aluno[1]}")
            print(f"Email: {aluno[2]}")
            print(f"ID do Imóvel: {aluno[3]}")
            print(f"Dias Ausentes: {aluno[4]}")
            print()
        else:
            print("Aluno não encontrado.")
            print()
    elif opcao == "3":
        exibir_alunos()
    elif opcao == "4":
        break
    else:
        print("Opção inválida.")
        print()
