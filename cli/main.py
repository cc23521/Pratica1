import pyodbc as bd
import os
import getpass as gp

def conectou():
    global conexao
    os.system('cls')
    senha = gp.getpass("Digite a senha do seu banco de dados: ")
    try:
        conexao = bd.connect(driver="{SQL Server}",
                            server="regulus.cotuca.unicamp.br",
                            database="BD23521",
                            uid="BD23521",
                            pwd=f"{senha}") 
        print("Conexão bem sucedida!")
        return True
    except:
        print("Não foi possível conectar ao servidor de BD!")
        return False
    
def incluir_imovel():
    meuCursor = conexao.cursor()
    bloco = "foo"
    while bloco != "":
        bloco = input("Bloco (Enter para terminar): ")
        if bloco != "":
            sComando = "insert into timeB.Imovel (bloco) values (?)"
            try:
                meuCursor.execute(sComando, bloco)
            except:
                print("Não foi possível incluir. Bloco deve ser apenas UM caractere.")    
    meuCursor.commit()        
    
def incluir_estudante():
    meuCursor = conexao.cursor()
    ra = "12345"
    while ra != "":
        ra = input("RA (Enter para terminar): ")
        if ra != "":
            email = input("Email: ")
            nomeSocial = input("Nome social (Enter para pular): ")
            idImovel = input("Id Imóvel: ")
            sComando = "insert into timeB.Estudante (RA, email, nomeSocial, idImovel) values (?, ?, ?, ?)"
            try:
                meuCursor.execute(sComando, ra, email, nomeSocial, idImovel)
            except:
                print("Não foi possível incluir. Campos RA, Email e idImovel são obrigatórios.")    
    meuCursor.commit()

def incluir_apontamento():
    meuCursor = conexao.cursor()
    ra = "12345"
    while ra != "":
        ra = input("RA (Enter para terminar): ")
        if ra != "":
            entrada = input("Data de entrada: ")
            sComando = "insert into timeB.Apontamento (ra, entrada) values (?, ?)"
            try:
                meuCursor.execute(sComando, ra, entrada)
            except:
                print("Não foi possível incluir. Campos RA e Data de entrada são obrigatórios.")    
    meuCursor.commit()
    
def excluir_registro():
    meuCursor = conexao.cursor()
    ra = "12345"
    while ra != "":
        ra = input("RA (Enter para terminar): ")
        if ra != "":
            try:
                meuCursor.execute("DELETE FROM timeB.Correspondencia WHERE RA = ?", ra)
                meuCursor.execute("DELETE FROM timeB.Veiculo WHERE RA = ?", ra)
                meuCursor.execute("DELETE FROM timeB.Apontamento WHERE RA = ?", ra)
                meuCursor.execute("DELETE FROM timeB.Estudante WHERE RA = ?", ra)

                meuCursor.execute("SELECT * FROM timeB.Estudante WHERE RA = ?", ra)
                rows = meuCursor.fetchall()
                for row in rows:
                    print(row)

                conexao.commit()

                print("Registros excluídos com sucesso!")

            except bd.Error as ex:
                print("Ocorreu um erro ao excluir os registros:", ex)

# def alterar():
#     # cursor é um objeto que permite que nosso programa execute comandos
#     # de SQL lá no servidor remoto:
#     meuCursor = conexao.cursor()  # objeto de manipulação de dados
#     numDepto = 1
#     while numDepto != 0:
#         # pedimos que o usuário digite o número do departamento a ser alterado
#         numDepto = int(input("Número do departamento (0 para terminar): "))
#         if numDepto != 0:    # usuário não quer terminar o cadastro
#             # verifica no BD se existe um departamento com esse número digitado
#             result = meuCursor.execute(
#                     'SELECT NOMEDEPTO, GERENTE_NUMSEGSOCIAL, GERENTE_DATAINICIAL '+\
#                     ' FROM EMPRESA.DEPARTAMENTO '+\
#                     ' WHERE NUMDEPTO = ?', numDepto)
#             registros = result.fetchall()
#             if len(registros) == 0:
#                 print("Departamento não encontrado.")
#             else:
#                 print("Registro encontrado:")
#                 print(registros)
#                 nomeDepto = registros[0][0]
#                 gerente = registros[0][1]
#                 data = registros[0][2]
#                 print("Nome do departamento: "+nomeDepto)
#                 print("Gerente:"+gerente)
#                 print("Data inicial:"+data)
                
#                 nomeDepto = input("Novo nome do departamento ([Enter] para manter): ")
#                 gerente = input("Novo gerente do departamento ([Enter] para manter:")
#                 data = input("Nova data de início do gerente (dd/mm/aaaa) ([Enter] para manter: ")
                
#                 if nomeDepto == "":  # usuário digitou [Enter]
#                      nomeDepto = registros[0][0]    # nome original do BD
                     
#                 if gerente == "":   # usuário digitou [Enter]
#                     gerente = registros[0][1]   # gerente original do BD
                    
#                 if data == "":   # usuário digitou [Enter]
#                     data = registros[0][2]  # data original do BD
                        
#             # criamos uma string com o comando Update para atualizar os novos dados
#             sComando = "Update empresa.departamento " +\
#                        "       set nomeDepto = ?, gerente_numSegSocial = ?,"+\
#                        "           gerente_dataInicial = ? "+\
#                        " where numDepto = ? "
               
#             # fazemos o cursor executar a string com o comando Update que criamos
#             try:        # tente executar o comando abaixo:
#                 meuCursor.execute(sComando, nomeDepto, gerente, data, numDepto)
#             except:     # em caso de erro
#                 print("Não foi possível alterar. Verifique.")
    
#     # após digitar numDepto = 0, paramos o cadastramento
#     # e enviamos os registros alterados para serem definitivamente
#     # gravados no servidor de banco de dados remoto
#     meuCursor.commit() # enviar as mudanças para o BD   
    
# def excluir():
#     # cursor é um objeto que permite que nosso programa execute comandos
#     # de SQL lá no servidor remoto:
#     meuCursor = conexao.cursor()  # objeto de manipulação de dados
#     numDepto = 1
#     while numDepto != 0:
#         # pedimos que o usuário digite o número do departamento a ser excluído
#         numDepto = int(input("Número do departamento (0 para terminar): "))
#         if numDepto != 0:    # usuário não quer terminar o cadastro
#             # verifica no BD se existe um departamento com esse número digitado
#             result = meuCursor.execute(
#                     'SELECT NOMEDEPTO, GERENTE_NUMSEGSOCIAL, GERENTE_DATAINICIAL '+\
#                     ' FROM EMPRESA.DEPARTAMENTO '+\
#                     ' WHERE NUMDEPTO = ?', numDepto)
#             registros = result.fetchall()
#             if len(registros) == 0:
#                 print("Departamento não encontrado.")
#             else:
#                 print("Registro encontrado:")
#                 nomeDepto = registros[0][0]
#                 gerente = str(registros[0][1])
#                 data = registros[0][2]
#                 print("Nome do departamento: "+nomeDepto)
#                 print("Gerente:"+gerente)
#                 print("Data inicial:"+data)
                
#                 resposta = input("Deseja realmente excluir (s/n)?")
#                 if resposta == "s":
#                     # criamos uma string com o comando Delete para excluir o registro lido
#                     sComando = "Delete from empresa.departamento " +\
#                             " where numDepto = ? "
                    
#                     # fazemos o cursor executar a string com o comando Update que criamos
#                     try:        # tente executar o comando abaixo:
#                         meuCursor.execute(sComando, numDepto)
#                     except:     # em caso de erro
#                         print("Não foi possível excluir. Deve ser um departamento em uso.")
    
#     # após digitar numDepto = 0, paramos o cadastramento
#     # e enviamos os registros inseridos para serem definitivamente
#     # gravados no servidor de banco de dados remoto
#     meuCursor.commit() # enviar as mudanças para o BD   

# def listar():
#     # cursor é um objeto que permite que nosso programa execute comandos
#     # de SQL lá no servidor remoto:
#     meuCursor = conexao.cursor()  # objeto de manipulação de dados
#     # busca no BD os registros de departamentos 
#     result = meuCursor.execute(
#                 'SELECT numdepto, NOMEDEPTO, GERENTE_NUMSEGSOCIAL, GERENTE_DATAINICIAL '+\
#                 ' FROM EMPRESA.DEPARTAMENTO ')   
#     registros = result.fetchall()
#     print(registros)
#     print("Num. Nome       Gerente    Data Inicial")
#     for depto in registros:
#         print(f"{depto[0]}   {depto[1]}    {depto[2]}    {depto[3]}")
        
#     input("Tecle [enter] para terminar:")
    
def seletor():
    opcao = 1
    while opcao != 0:
        os.system('cls') or None
        print("Operações disponíveis")
        print("=" * 9, "=" * 9, "\n")
        print("0 - Terminar este programa")
        print("1 - Incluir Imóvel")
        print("2 - Incluir Estudante")     
        print("3 - Incluir Apontamento")
        print("4 - Excluir Registro")
        opcao = int(input("\nDigite o número da opção desejada: "))
        match opcao:
            case 1: incluir_imovel()
            case 2: incluir_estudante()
            case 3: incluir_apontamento()
            case 4: excluir_registro()

if conectou():
    seletor()
    conexao.close()

print("Programa encerrado.")