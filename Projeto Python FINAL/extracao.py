import pandas as pd
import psycopg2
import pandas.io.sql as psql
from sqlalchemy import create_engine, text

#Preencher com os parametros do database do elephantsql
db_params = {
    'host': 'kesavan.db.elephantsql.com',
    'database': 'umltvftk',
    'user': 'umltvftk',
    'password': '6MHS_p2qH5sOt902ziUGM-mooye42ulG'
}

#Criando conexão
conn = psycopg2.connect(
    host=db_params['host'],
    database=db_params['database'],
    user=db_params['user'],
    password=db_params['password']
)

# Create um cursor (o que vai fazer os comandos sql)
cur = conn.cursor()

# faz commitar automaticamente pra não precisar ficar chamando conn.commit apos cada mudança nos dados
conn.set_session(autocommit=True)
############################## COMENTADO PORQUE JÁ FOI EXECUTADO ##################################################
'''
leitura = pd.read_csv('dados/turmas_manipulado.xlsx - Table 1.tsv', sep='\t')
leitura[['CÓDIGO DE TURMA','TEORIA','PRÁTICA']]

def subirNaHorarios(Codigo, Dia, Horario,horario2, Semanal):
    sql = 'INSERT INTO "public"."Horário das Turmas" VALUES (%s,%s,%s,%s,%s)'
    cur.execute(sql, (Codigo, Dia, Horario, horario2, Semanal))

for linha in range(len(leitura)):
    #vetorizando o conteúdo da coluna TEORIA linha a linha
    if (leitura.iloc[linha].TEORIA == '#REF!'):
        continue
    # if (leitura.iloc[linha].TURNO == 'noturno'):
    #     continue
    if (leitura.iloc[linha].TEORIA != '0'):
        splitado = leitura.iloc[linha].TEORIA.split(',')

        #encontrando primeiro dia
        dia = splitado[0][:splitado[0].index(' ')]

        #encontrando horario para primeiro dia
        horario = splitado[0][splitado[0].index(' ')+1:len(splitado[0])].strip().split(' ')
        
        #encontrando frequencia semanal~o [1:] é pra pular o primeiro espaço
        freqSemanal = splitado[2][1:].strip()
        subirNaHorarios((leitura.iloc[linha]['CÓDIGO DE TURMA']),dia,horario[1][0:2],horario[3][0:2],freqSemanal)
        if (len(splitado)>4):
            semEspacos = splitado[3].strip()
            dia2 = semEspacos[:semEspacos.index(' ')] #segundo dia
            horario2 = semEspacos[semEspacos.index(' '):len(semEspacos)].strip().split(' ') #segundo horário
            freqSemanal2 = splitado[5].strip() #segunda frequência semanal
            subirNaHorarios((leitura.iloc[linha]['CÓDIGO DE TURMA']),dia2,horario2[1][0:2],horario2[3][0:2],freqSemanal2)

        if(len(splitado)>6):
            semEspacos = splitado[6].strip()
            dia3 = semEspacos[:semEspacos.index(' ')] #terceiro dia
            horario3 = semEspacos[semEspacos.index(' '):len(semEspacos)].strip().split(' ') #segundo horário
            freqSemanal3 = splitado[8].strip() #segunda frequência semanal
            subirNaHorarios((leitura.iloc[linha]['CÓDIGO DE TURMA']),dia3,horario3[1][0:2],horario3[3][0:2],freqSemanal3)

    #vetorizando o conteúdo da coluna PRÁTICA
    if (leitura.iloc[linha].PRÁTICA !='0'):
        splitado = leitura.iloc[linha].PRÁTICA.split(',')

        #encontrando primeiro dia
        dia = splitado[0][:splitado[0].index(' ')]

        #encontrando horario para primeiro dia
        horario = splitado[0][splitado[0].index(' ')+1:len(splitado[0])].strip().split(' ')

        #encontrando frequencia semanal~o [1:] é pra pular o primeiro espaço
        freqSemanal = splitado[2][1:].strip()
        subirNaHorarios((leitura.iloc[linha]['CÓDIGO DE TURMA']),dia,horario[1][0:2],horario[3][0:2],freqSemanal)
        if (len(splitado)>4):
            semEspacos = splitado[3].strip()
            dia2 = semEspacos[:semEspacos.index(' ')] #segundo dia
            horario2 = semEspacos[semEspacos.index(' '):len(semEspacos)].strip().split(' ') #segundo horário
            freqSemanal2 = splitado[5].strip() #segunda frequência semanal
            subirNaHorarios((leitura.iloc[linha]['CÓDIGO DE TURMA']),dia2,horario2[1][0:2],horario2[3][0:2],freqSemanal2)


'''

sql = 'SELECT * FROM "public"."Horário das Turmas" t1 where t1."Semanal" = \'quinzenal I\' OR t1."Semanal" = \'quinzenal II\''
#sql = 'DELETE FROM "public"."Horário das Turmas"'
df = psql.read_sql(sql,conn)

df