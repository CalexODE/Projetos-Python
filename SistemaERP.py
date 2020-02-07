import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='erp',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    port=3308
)

autentico = False

def logarCadastrar():
    usuarioExistente = 0
    autenticado = False
    usuarioMaster = False

    if decisao == 1:
        nome = input("Digite seu login: ")
        senha = input("Senha: ")

        for linha in resultado:
            if nome == linha['nome'] and senha == linha['senha']:
                if linha['nivel'] == 1:
                    usuarioMaster = False
                elif linha['nivel'] == 2:
                    usuarioMaster = True
                autenticado = True
            else:
                autenticado = False

        if not autenticado:
            print("Email ou senha errada")
    elif decisao == 2:
        print("Faça seu cadastro")
        nome = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        for linha in resultado:
            if nome == linha["nome"]:
                usuarioExistente+=1
        if usuarioExistente == 1:
            print("Usuário já existente")
        elif usuarioExistente == 0:
            try:
                with conexao.cursor() as cursor:
                    cursor.execute("insert into cadastros(nome, senha, nivel) values (%s, %s, %s)", (nome, senha, 1))
                    conexao.commit()
                print("Usuario cadastrado")
            except:
                print("Erro ao cadastrar")
    return autenticado, usuarioMaster

def cadastrarProdutos():
    nome = input("Digite o nome do produto: ")
    ingredientes = input("Os ingredientes: ")
    grupo = input("Grupo: ")
    preco = float(input("Preço: "))

    try:
        with conexao.cursor() as cursor:
            cursor.execute("insert into produtos(nome, ingredientes, grupo, preco) values (%s, %s, %s, %s)", (nome, ingredientes, grupo, preco))
            conexao.commit()
        print("Produto adicionado")
    except:
        print("Erro ao adicionar produto")


while not autentico:
    decisao = int(input(' 1 - Logar\n 2 - cadastrar\n: '))

    try:
        with conexao.cursor() as cursor:
            cursor.execute('select * from cadastros')
            resultado = cursor.fetchall()

    except:
        print("Erro ao conectar ao banco de dados")
    autentico, usuarioSupremo = logarCadastrar()

if autentico:
    print("Autenticado")

    if usuarioSupremo == True:
        decisaoUser = 1
        while decisaoUser != 0:
            decisaoUser = int(input(" 1 - Cadastrar produto\n 2 - ...\n 0 - Sair\n: "))

            if decisaoUser == 1:
                cadastrarProdutos()

