import pyodbc as bd
import os
import getpass as gp

def conectou():
    global conexao
    os.system("cls")
    banco_dados = input("Banco de dados: ")
    user = input("Usuário: ")
    senha = gp.getpass("Digite a senha do seu banco de dados: ")
    try:
        conexao = bd.connect(driver="{SQL Server}",
                            server="regulus.cotuca.unicamp.br",
                            database="BD23521",
                            uid="BD23521",
                            pwd=f"{senha}")
                            # database=f"{banco_dados}",
                            # uid=f"{user}",
                            # pwd=f"{senha}") 
        return True
    except bd.Error as err:
        print("Não foi possível conectar ao servidor de BD:", err)
        return False

def incluir_imovel():
    meuCursor = conexao.cursor()
    bloco = "foo"
    while bloco != '':
        bloco = input("Bloco [A-Z] (Enter para terminar): ")

        if bloco == '': continue

        if not bloco.isalpha():
            print("Bloco deve ser caractere.")
            continue
        
        sComando = "insert into timeB.Imovel (bloco) values (?)"
        try:
            meuCursor.execute(sComando, bloco)
            print("Imóvel incluído.")
        except bd.Error as err:
            print("Não foi possível incluir imóvel:", err)    
    meuCursor.commit()        
    
def atualizar_vagas_imovel(idImovel):
    meuCursor = conexao.cursor()
    sComando = f"if (select vagas from timeB.Imovel where idImovel = ?) > 0" +\
               f"begin update timeB.Imovel set vagas = vagas - 1 where idImovel = ? end"
    try:
        meuCursor.execute(sComando, idImovel, idImovel)
    except bd.Error as err:
        print("Não foi possível atualizar número de vagas:", err)

def tem_vagas():
    meuCursor = conexao.cursor()
    try:
        meuCursor.execute("select * from timeB.Imovel")
        imoveis = meuCursor.fetchall()
        for imovel in imoveis:
            vagas = imovel[2]
            if vagas > 0:
                return True
        return False
    except bd.Error as err:
        print(err)

def listar_imoveis():
    meuCursor = conexao.cursor()
    try:
        meuCursor.execute("select * from timeB.Imovel")

        imoveis = meuCursor.fetchall()
        print("idImovel,bloco,vagas")
        for imovel in imoveis:
            idImovel, bloco, vagas = imovel[0], imovel[1], imovel[2]
            if vagas > 0:
                print(idImovel, bloco, vagas, sep=",")
    except bd.Error as err:
        print("Não foi possível listar os imóveis:", err)

def incluir_estudante():
    meuCursor = conexao.cursor()
    ra = "foo"
    while ra != '':
        listar_estudante()
        print()
        if not tem_vagas(): break

        ra = input("RA (Enter para terminar): ")
        
        if ra == '': continue

        email = input("Email: ")
        nomeSocial = input("Nome social (Enter para pular): ")
        print("\nImóveis disponíveis")
        listar_imoveis()
        idImovel = input("\nId Imóvel: ")
        sComando = "insert into timeB.Estudante (RA, email, nomeSocial, idImovel) values (?, ?, ?, ?)"
        try:
            meuCursor.execute(sComando, ra, email, nomeSocial, idImovel)
            atualizar_vagas_imovel(idImovel)
        except bd.Error as err:
            print("Não foi possível incluir estudante:", err)    
    meuCursor.commit()

def listar_estudante():
    meuCursor = conexao.cursor()
    try:
        meuCursor.execute("select * from timeB.Estudante")

        estudantes = meuCursor.fetchall()
        print("RA,email,nomeSocial,semestreAtual,diasAusente,idImovel")
        for estudante in estudantes:
            ra =            estudante[0]
            email =         estudante[1]
            nomeSocial =    estudante[2]
            semestreAtual = estudante[3]
            diasAusente =   estudante[4]
            idImovel =      estudante[5]
            print(ra, email, nomeSocial, semestreAtual, diasAusente, idImovel, sep=",")
    except bd.Error as err:
        print("Não foi possível listar os imóveis:", err)

def incluir_apontamento():
    meuCursor = conexao.cursor()
    ra = "foo"
    while ra != '':
        ra = input("RA (Enter para terminar): ")

        if ra == '': continue

        entrada = input("Data de entrada: ")
        sComando = "insert into timeB.Apontamento (ra, entrada) values (?, convert(date, ?, 103))"
        try:
            meuCursor.execute(sComando, ra, entrada)
        except bd.Error as err:
            print("Não foi possível incluir apontamento:", err)    
    meuCursor.commit()
    
def incluir_registro():
    opcao = 'foo'
    while opcao not in ('0', ''):
        os.system("cls")
        print("Operações disponíveis")
        print("=" * 9, "=" * 11, "\n")
        print("0 - Voltar")
        print("1 - Incluir Imóvel")
        if tem_vagas(): 
            print("2 - Incluir Estudante")
        else: 
            print("2 - Incluir Estudante (NÃO HÁ VAGAS)")
        print("3 - Incluir Apontamento")
        opcao = input("\nDigite o número da opção desejada: ")
        match opcao:
            case '1': incluir_imovel()
            case '2': incluir_estudante()
            case '3': incluir_apontamento()

def excluir_estudante():
    meuCursor = conexao.cursor()
    ra = "foo"
    while ra != '':
        ra = input("RA (Enter para terminar): ")

        if ra == '': continue
    
        try:
            meuCursor.execute("DELETE FROM timeB.Apontamento WHERE RA = ?", ra)
            meuCursor.execute("DELETE FROM timeB.Estudante WHERE RA = ?", ra)
            print("Registros excluídos com sucesso!")
        except bd.Error as err:
            print("Ocorreu um erro ao excluir os registros:", err)
    meuCursor.commit()    

def excluir_imovel():
    meuCursor = conexao.cursor()
    idImovel = 'foo'
    while idImovel not in ('0', ''):
        idImovel = input("Id Imóvel (Enter para terminar): ")

        if idImovel in ('0', ''): continue

        try:
            meuCursor.execute("delete from timeB.Imovel where idImovel = ?", idImovel)
            print("Registros excluídos com sucesso!")
        except bd.Error as err:
            print("Ocorre um erro ao excluir o registro:", err)
    meuCursor.commit()

def excluir_registro():
    opcao = '1'
    while opcao not in ('0', ''):
        os.system("cls")
        print("Operações disponíveis")
        print("=" * 9, "=" * 11, "\n")
        print("0 - Voltar")
        print("1 - Excluir Estudante")
        print("2 - Excluir Imóvel")
        opcao = input("\nDigite o número da opção desejada: ")
        match opcao:
            case '1': excluir_estudante()
            case '2': excluir_imovel()

def alterar_registro():
    meuCursor = conexao.cursor()
    ra = "12345"
    while ra != '':
        ra = input("RA (Enter para terminar): ")
        if ra != '':
            novo_nome = input("Novo nome: ")
            novo_email = input("Novo email: ")
            try:
                meuCursor.execute("UPDATE timeB.Estudante SET email = ?, nome = ? WHERE RA = ?",
                                  (novo_email, novo_nome, ra))
                conexao.commit()

                meuCursor.execute("SELECT * FROM timeB.Estudante WHERE RA = ?", ra)
                rows = meuCursor.fetchall()
                for row in rows:
                    print(row)

                print("Registro alterado com sucesso!")

            except bd.Error as err:
                print("Ocorreu um erro ao alterar o registro:", err)

def seletor():
    opcao = '1'
    while opcao not in ('0', ''):
        os.system("cls")
        print("Operações disponíveis")
        print("=" * 9, "=" * 11, "\n")
        print("0 - Sair")
        print("1 - Incluir Registro")
        print("2 - Excluir Registro")
        print("3 - Alterar Registro")
        print("4 - Listar Registro")
        opcao = input("\nOpção desejada: ")
        match opcao:
            case '1': incluir_registro()
            case '2': excluir_registro()
            # case 3: alterar_registro()
            # case 4: listar_registro()

if conectou():
    seletor()
    conexao.close()

print("Programa encerrado.")