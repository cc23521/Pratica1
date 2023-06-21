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
                            database=f"{banco_dados}",
                            uid=f"{user}",
                            pwd=f"{senha}")
        return True
    except bd.Error as err:
        print("Não foi possível conectar ao servidor de BD:", err)
        return False

def incluir_imovel():
    meuCursor = conexao.cursor()
    bloco = "foo"
    while bloco != '':
        bloco = input("Bloco [A-Z] (Enter para terminar): ").upper()

        if bloco == '': continue

        if not bloco.isalpha():
            print("Bloco deve ser caractere.")
            continue
        
        sComando = "insert into timeB.Imovel (bloco) values (?)"
        try:
            meuCursor.execute(sComando, bloco)
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

def listar_imovel():
    meuCursor = conexao.cursor()
    listar_todos = "foo"
    while listar_todos != '':
        listar_todos = input("Listar todos imóves [s/n]? (Enter para sair) ").upper()
        if listar_todos not in ('S', 'N'): continue
        
        if listar_todos == 'S':
            try:
                meuCursor.execute("select * from timeB.Imovel")
                imoveis = meuCursor.fetchall()
                print("idImovel,bloco,vagas")
                for imovel in imoveis:
                    idImovel, bloco, vagas = imovel[0], imovel[1], imovel[2]
                    print(idImovel, bloco, vagas, sep=',')
                print()
            except bd.Error as err:
                print("Não foi possível listar os imóveis:", err)
        else:
            idImovel = input("Id Imovel: ")
            try:
                sComando = "select * from timeB.Imovel where idImovel = (?)"
                meuCursor.execute(sComando, idImovel)
                imovel = meuCursor.fetchall()[0]
                print("idImovel,bloco,vagas")
                for col in imovel:
                    print(col, end=',')
                print("\n")
            except bd.Error as err:
                print("Não foi possível listar o imóvel:", err)
            except IndexError:
                print("Imóvel não está registrado.")

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

def incluir_estudante():
    meuCursor = conexao.cursor()
    ra = "foo"
    while ra != '':
        if not tem_vagas(): break

        ra = input("RA (Enter para terminar): ")
        
        if ra == '': continue

        email = input("Email: ")
        nomeSocial = input("Nome social (Enter para pular): ")
        print("\nImóveis disponíveis")
        listar_imovel()
        idImovel = input("\nId Imóvel: ")
        sComando = "insert into timeB.Estudante (RA, email, nomeSocial, idImovel) values (?, ?, ?, ?)"
        try:
            meuCursor.execute(sComando, ra, email, nomeSocial, idImovel)
            atualizar_vagas_imovel(idImovel)
        except bd.Error as err:
            print("Não foi possível incluir estudante:", err)    
    meuCursor.commit()

def excluir_estudante():
    meuCursor = conexao.cursor()
    ra = "foo"
    while ra != '':
        ra = input("RA (Enter para terminar): ")

        if ra == '': continue
    
        try:
            meuCursor.execute("delete from timeB.Apontamento where RA = ?", ra)
            meuCursor.execute("delete from timeB.Estudante where RA = ?", ra)
        except bd.Error as err:
            print("Ocorreu um erro ao excluir os registros:", err)
    meuCursor.commit()   

def listar_estudante():
    meuCursor = conexao.cursor()
    listar_todos = "foo"
    while listar_todos != '':
        listar_todos = input("Listar todos estudantes [s/n]? (Enter para sair) ").upper()
        if listar_todos not in ('S', 'N'): continue
        
        if listar_todos == 'S':
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
                    print(ra, email, nomeSocial, semestreAtual, diasAusente, idImovel, sep=',')
                print()
            except bd.Error as err:
                print("Não foi possível listar os estudantes:", err)
        else:
            ra = input("RA: ")
            try:
                sComando = "select * from timeB.Estudante where RA = (?)"
                meuCursor.execute(sComando, ra)
                estudante = meuCursor.fetchall()[0]
                print("RA,email,nomeSocial,semestreAtual,diasAusente,idImovel")
                for col in estudante:
                    print(col, end=',')
                print("\n")
            except bd.Error as err:
                print("Não foi possível listar o imóvel:", err)
            except IndexError:
                print("Estudante não está registrado.")

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

def listar_apontamento():
    meuCursor = conexao.cursor()
    listar_todos = "foo"
    while listar_todos != '':
        listar_todos = input("Listar todos apontamentos [s/n]? (Enter para sair) ").upper()
        if listar_todos not in ('S', 'N'): continue
        
        if listar_todos == 'S':
            try:
                meuCursor.execute("select * from timeB.Apontamento")
                apontamentos = meuCursor.fetchall()
                print("idApontamento,RA,entrada,saída")
                for apontamento in apontamentos:
                    idApontamento, ra, entrada, saida = apontamento[0], apontamento[1], apontamento[2], apontamento[3]
                    print(idApontamento, ra, entrada, saida, sep=',')
                print()
            except bd.Error as err:
                print("Não foi possível listar os apontamentos:", err)
        else:
            idApontamento = input("Id Apontamento: ")
            try:
                sComando = "select * from timeB.Apontamento where idApontamento = (?)"
                meuCursor.execute(sComando, idApontamento)
                apontamento = meuCursor.fetchall()[0]
                print("idApontamento,RA,entrada,saída")
                for col in apontamento:
                    print(col, end=',')
                print("\n")
            except bd.Error as err:
                print("Não foi possível listar o apontamento:", err)
            except IndexError:
                print("Apontamento não está registrado.")

def excluir_apontamento():
    meuCursor = conexao.cursor()
    idApontamento = "foo"
    while idApontamento != '':
        idApontamento = input("Id Apontamento (Enter para terminar): ")

        if idApontamento == '': continue
    
        try:
            meuCursor.execute("delete from timeB.Apontamento where idApontamento = ?", idApontamento)
        except bd.Error as err:
            print("Ocorreu um erro ao excluir os registros:", err)
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

def excluir_registro():
    opcao = '1'
    while opcao not in ('0', ''):
        os.system("cls")
        print("Operações disponíveis")
        print("=" * 9, "=" * 11, "\n")
        print("0 - Voltar")
        print("1 - Excluir Estudante")
        print("2 - Excluir Apontamento")
        opcao = input("\nDigite o número da opção desejada: ")
        match opcao:
            case '1': excluir_estudante()
            case '2': excluir_apontamento()

def listar_registro():
    opcao = '1'
    while opcao not in ('0', ''):
        os.system("cls")
        print("Operações disponíveis")
        print("=" * 9, "=" * 11, "\n")
        print("0 - Voltar")
        print("1 - Listar Imóvel")
        print("2 - Listar Estudante")
        print("3 - Listar Apontamento")
        opcao = input("\nOpção desejada: ")
        match opcao:
            case '1': listar_imovel()
            case '2': listar_estudante()
            case '3': listar_apontamento()
            
def atualizar_estudante():
    meuCursor = conexao.cursor()
    ra = "foo"
    while ra != '':
        ra = input("RA (Enter para terminar): ")

        if ra == '': continue

        nomeSocial = input("Novo nome social: ")
        email = input("Novo email: ")
        diasAusente = input("Dias ausente: ")
        semestreAtual = input("Semestre atual: ")
        try:
            meuCursor.execute("update timeB.Estudante set email = ?, nomeSocial = ?, diasAusente = ?, semestreAtual = ? where RA = ?",
                              (email, nomeSocial, diasAusente, semestreAtual, ra))
            conexao.commit()
        except bd.Error as err:
            print("Ocorreu um erro ao alterar o registro:", err)          

def atualizar_apontamento():
    meuCursor = conexao.cursor()
    idApontamento = "foo"
    while idApontamento != '':
        idApontamento = input("Id Apontamento (Enter para terminar): ")

        if idApontamento == '': continue

        saida = input("Nova data de saída: ")
        sComando = "update timeB.Apontamento set saida = convert(date, ?, 103) where idApontamento = ?"
        try:
            meuCursor.execute(sComando, saida, idApontamento)
            conexao.commit()
        except bd.Error as err:
            print("Ocorreu um erro ao alterar o registro:", err)

def atualizar_registro():
    opcao = '1'
    while opcao not in ('0', ''):
        os.system("cls")
        print("Operações disponíveis")
        print("=" * 9, "=" * 11, "\n")
        print("0 - Voltar")
        print("1 - Atualizar Estudante")
        print("2 - Atualizar Apontamento")
        opcao = input("\nOpção desejada: ")
        match opcao:
            case '1': atualizar_estudante()
            case '2': atualizar_apontamento()

def seletor():
    opcao = '1'
    while opcao not in ('0', ''):
        os.system("cls")
        print("Operações disponíveis")
        print("=" * 9, "=" * 11, "\n")
        print("0 - Sair")
        print("1 - Incluir Registro")
        print("2 - Excluir Registro")
        print("3 - Atualizar Registro")
        print("4 - Listar Registro")
        opcao = input("\nOpção desejada: ")
        match opcao:
            case '1': incluir_registro()
            case '2': excluir_registro()
            case '3': atualizar_registro()
            case '4': listar_registro()

if conectou():
    seletor()
    conexao.close()

print("Programa encerrado.")