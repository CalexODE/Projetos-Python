import pymysql.cursors

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    db='interacaopython',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor,
    port=3308
)

dropT = 'drop table pessoas'

createT = 'create table pessoas(nome varchar(30), idade int, endereco varchar(100));'
createTeste = 'create table teste(nome varchar(10))'
createTable = 'create table cadastros(id int primary key auto_increment, nome varchar(50) not null, endereco varchar(300));'


#x = input("Digite o nome: ")
#y = input("Digite o endereço: ")

#insertInto = 'insert into cadastros(nome, endereco) values ("{}","{}")'.format(x, y)

selectFrom = ' select * from cadastros'

with conexao.cursor() as cursor:
    cursor.execute(selectFrom)
    dados = cursor.fetchall()


print(dados)
print(dados[1]['nome'])
#print(dados[0].pop('nome', 'Não encontrado')) #Retorna e remove

for dado in dados:
    print(dado['nome'])

