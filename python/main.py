from colorama import init, Fore
import pyodbc as bd
import os
import getpass as gp

init()

def seletor():
    """
    Exibe menu de opções para o usuário.
    """
    os.system('cls') or None
    while True:
        print("Operações disponíveis")
        print("=" * 9, "=" * 9 + "\n")
        print("0 - Sair")
        print("1 - Incluir estudante")
        print("2 - Alterar estudante")     
        print("3 - Excluir estudante")
        print("4 - Listar estudantes")
        opcao = int(input("\nDigite o número da opção desejada:"))
        match opcao:
            case 0: break
            case 1: incluir()
            case 2: alterar()
            case 3: excluir()
            case 4: listar()
            case _: print(Fore.RED + "Opção inválida.\n")

def conectou() -> bool:
    """
    Conecta programa ao servidor de banco de dados.
    """
    global conexao
    os.system('cls') or None
    senha = gp.getpass("Digite a senha do seu banco de dados: ")
    try:
        conexao = bd.connect(driver="{SQL Server}",
                            server="regulus.cotuca.unicamp.br",
                            database="BD23521",
                            uid="BD23521",
                            pwd=f"{senha}")
        print(Fore.GREEN + "Conexão bem sucedida.")
        return True
    except:
        print(Fore.RED + "Não foi possível conectar ao servidor!")
        return False

def incluir():
    """
    Inclui registros de estudante no servidor de banco de dados.
    """    
    cursor = conexao.cursor()
    ra = ""
    while ra != "0":
        ra = input("RA do estudante (0 para sair): ")
        if ra != "0":
            email = input("E-mail: ")
            nomeSocial = input("Nome social (Enter para pular): ")
            idImovel = input("Identificador de imóvel: ")            
            comando = "insert into timeB.Estudante " +\
                      "(RA, email, nomeSocial, idImovel) " +\
                      "VALUES " +\
                      "(?, ?, ?, ?)"               
            try:
                cursor.execute(comando, ra, email, nomeSocial, idImovel)
                print(Fore.GREEN + "Registro incluído.")
            except:
                print(Fore.RED + "Não foi possível incluir! Pode haver RA repetido.")
    cursor.commit()        

def alterar():
    """
    Altera registros de estudante no servidor de banco de dados.
    """
    cursor = conexao.cursor()
    ra = ""
    while ra != "0":
        ra = input("RA do estudante (0 para sair): ")
        if ra != 0:
            resultado = cursor.execute(
                    "SELECT email, nomeSocial, idImovel " +\
                    "FROM timeB.Estudante " +\
                    "WHERE RA = ?", ra)
            registros = resultado.fetchall()
            if len(registros) == 0:
                print(Fore.RED + "Departamento não encontrado.")
            else:
                print(Fore.GREEN + "Registro encontrado:")
                print(registros)
                email = registros[0][0]
                nomeSocial = registros[0][1]
                idImovel = registros[0][2]
                print("e-mail: " + email)
                print("Nome social: " + nomeSocial)
                print("Imóvel: " + idImovel)

                email = input("Novo email ([Enter] para manter): ")
                nomeSocial = input("Novo nome social ([Enter] para manter:")
                idImovel = input("Novo imóvel ([Enter] para manter: ")

                if email == "":
                    email = registros[0][0]

                if nomeSocial == "":
                    nomeSocial = registros[0][1]

                if idImovel == "":
                    idImovel = registros[0][2]

            comando = "UPDATE timeB.Estudante " +\
                      "SET email = ?, nomeSocial = ?, idImovel = ? " +\
                      "WHERE RA = ?"

            try:
                cursor.execute(comando, email, nomeSocial, idImovel)
                print(Fore.GREEN + "Registro incluído.")
            except:
                print(Fore.RED + "Não foi possível alterar! Verifique.")
    cursor.commit()  

def excluir():
    """
    Exclui registros de estudante no servidor de banco de dados.
    """
    cursor = conexao.cursor()
    ra = ""
    while ra != "0":
        ra = input("RA do estudante (0 para sair): ")
        if ra != "0":
            resultado = cursor.execute(
                    "SELECT NOMEDEPTO, GERENTE_NUMSEGSOCIAL, GERENTE_DATAINICIAL " +\
                    "FROM EMPRESA.DEPARTAMENTO " +\
                    "WHERE NUMDEPTO = ?", numDepto)
            registros = result.fetchall()
            if len(registros) == 0:
                print("Departamento não encontrado.")
            else:
                print("Registro encontrado:")
                nomeDepto = registros[0][0]
                gerente = str(registros[0][1])
                data = registros[0][2]
                print("Nome do departamento: "+nomeDepto)
                print("Gerente:"+gerente)
                print("Data inicial:"+data)
                
                resposta = input("Deseja realmente excluir (s/n)?")
                if resposta == "s":
                    # criamos uma string com o comando Delete para excluir o registro lido
                    sComando = "Delete from empresa.departamento " +\
                            " where numDepto = ? "
                    
                    # fazemos o cursor executar a string com o comando Update que criamos
                    try:        # tente executar o comando abaixo:
                        meuCursor.execute(sComando, numDepto)
                    except:     # em caso de erro
                        print("Não foi possível excluir. Deve ser um departamento em uso.")
    
    # após digitar numDepto = 0, paramos o cadastramento
    # e enviamos os registros inseridos para serem definitivamente
    # gravados no servidor de banco de dados remoto
    meuCursor.commit() # enviar as mudanças para o BD   

def listar():
    # cursor é um objeto que permite que nosso programa execute comandos
    # de SQL lá no servidor remoto:
    meuCursor = conexao.cursor()  # objeto de manipulação de dados
    # busca no BD os registros de departamentos 
    result = meuCursor.execute(
                'SELECT numdepto, NOMEDEPTO, GERENTE_NUMSEGSOCIAL, GERENTE_DATAINICIAL '+\
                ' FROM EMPRESA.DEPARTAMENTO ')   
    registros = result.fetchall()
    print(registros)
    print("Num. Nome       Gerente    Data Inicial")
    for depto in registros:
        print(f"{depto[0]}   {depto[1]}    {depto[2]}    {depto[3]}")
        
    input("Tecle [enter] para terminar:")

if conectou():
    seletor()
    conexao.close()

print("Programa encerrado.")