
import numpy as np
import pandas as pd
import json

PRECO_MAX = 0.8*(105.69)/12*1
# PRECO_MAX = 100

print("PRECO MAXIMO DE CADA JOGADOR: ", PRECO_MAX)
print("PRECO MAXIMO TIME: ", PRECO_MAX*12)

DB_FILE = 'db_10.json'

def get_atletas():
    with open(DB_FILE) as f:
        db = json.loads(f.readline())
        f.close()
        return db.get('atletas')
    return None

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

df = pd.DataFrame(get_atletas())
df = df[["scout", "posicao_id", "status_id", "pontos_num", "preco_num", "media_num", "apelido", "clube_id"]]

goleiros_prov = df.loc[(df['posicao_id'] == 1) & (df['status_id'] == 7)]
gl = goleiros_prov[["scout", "preco_num", "apelido", "clube_id"]]

def strrr(c, l):
    if c in l:
        return ">>>>> "
    return ""

def translate_clube_id(c_id):
    tops = ["Palmeiras", "Bragantino", "Atlético-GO", "Fluminense", "Fortaleza"]
    with open(DB_FILE) as f:
        db = json.loads(f.readline())
        f.close()
        cname = db.get('clubes').get(str(c_id)).get('nome')
        return "{}{}".format(strrr(cname, tops), cname)
    return None

def magicnumber_def(i):
    # print(i)
    pesos = {
        # cartao amarelo
        'CA': -2, 
        # cartao amarelo
        'CV': -5, 
        # defesas
        'DE': 1,
        # defesas penalti
        'DP': 7,
        # falta cometidas
        'FC': -0.5,
        # falta sofrida
        'FS': 1,
        # gol sofrido
        'GS': -1,
        # jogos s/ sofrer gol
        'SG': 5,
        # penalti cometido
        'PC': -2,
        # desarme
        'DS': 1,
        # "passe incomplero"
        'PI': -0.1,
        # finalização fora
        'FF': 0.8,
        # finalização defendida
        'FD': 1.2,
        # IMPEDIMENTO
        'I': -0.5,
        # penalti sofrido
        'PS': 1,
        # finalizção trave
        'FT': 3,
        # gool
        'G': 8,
        # assistencia
        'A': 5,
        # PENALTI PERDIDO
        'PP': -4,
        # gol contra
        'GC': -5
    }

    return round(sum([float(i[key]*pesos[key]) for key in i.keys()]), 2)

sc = gl['scout'].apply(magicnumber_def)

gl['SC'] = sc
gl = gl.sort_values('preco_num')[['preco_num', 'SC', 'apelido', 'clube_id']]

# jogadores com menores valor até...
gl = gl.loc[gl['preco_num'] <= PRECO_MAX].sort_values('SC', ascending=False)

cl = gl['clube_id'].apply(translate_clube_id)
gl['clube'] = cl

print("GOLEIROS")
print(gl)

# =================================


zag_prov = df.loc[(df['posicao_id'] == 3) & (df['status_id'] == 7)]
zl = zag_prov[["scout", "preco_num", "apelido", "clube_id"]]

# print(zl)

sc = zl['scout'].apply(magicnumber_def)

zl['SC'] = sc
zl = zl.sort_values('preco_num')[['preco_num', 'SC', 'apelido', 'clube_id']]

# jogadores com menores valor até...
zl = zl.loc[zl['preco_num'] <= PRECO_MAX].sort_values('SC', ascending=False)

cl = zl['clube_id'].apply(translate_clube_id)
zl['clube'] = cl

print("ZAGUEIROS")
print(zl)

# =================================


lat_prov = df.loc[(df['posicao_id'] == 2) & (df['status_id'] == 7)]
ll = lat_prov[["scout", "preco_num", "apelido", "clube_id"]]

# print(ll)

sc = ll['scout'].apply(magicnumber_def)

ll['SC'] = sc
ll = ll.sort_values('preco_num')[['preco_num', 'SC', 'apelido', 'clube_id']]

# jogadores com menores valor até...
ll = ll.loc[ll['preco_num'] <= PRECO_MAX].sort_values('SC', ascending=False)

cl = ll['clube_id'].apply(translate_clube_id)
ll['clube'] = cl

print("LATERAIS")
print(ll)
# =================================


mei_prov = df.loc[(df['posicao_id'] == 4) & (df['status_id'] == 7)]
ml = mei_prov[["scout", "preco_num", "apelido", "clube_id"]]

# print(ml)

sc = ml['scout'].apply(magicnumber_def)

ml['SC'] = sc
ml = ml.sort_values('preco_num')[['preco_num', 'SC', 'apelido', 'clube_id']]

# jogadores com menores valor até...
ml = ml.loc[ml['preco_num'] <= PRECO_MAX].sort_values('SC', ascending=False)

cl = ml['clube_id'].apply(translate_clube_id)
ml['clube'] = cl

print("MEIAS")
print(ml)
# =================================


atac_mei = df.loc[(df['posicao_id'] == 5) & (df['status_id'] == 7)]
al = atac_mei[["scout", "preco_num", "apelido", "clube_id"]]

# print(al)

sc = al['scout'].apply(magicnumber_def)

al['SC'] = sc
al = al.sort_values('preco_num')[['preco_num', 'SC', 'apelido', 'clube_id']]

# jogadores com menores valor até...
al = al.loc[al['preco_num'] <= PRECO_MAX].sort_values('SC', ascending=False)

cl = al['clube_id'].apply(translate_clube_id)
al['clube'] = cl

print("ATACANTES")
print(al)

# =================================


tec_mei = df.loc[(df['posicao_id'] == 6) & (df['status_id'] == 7)]
# tec = tec_mei[["scout", "preco_num", "apelido", "clube_id"]]

# print(tec)

# sc = tec['scout'].apply(magicnumber_def)

# tec['SC'] = sc
# tec = tec.sort_values('preco_num')[['preco_num', 'SC', 'apelido', 'clube_id']]

# jogadores com menores valor até...
tec = tec_mei.loc[tec_mei['preco_num'] <= PRECO_MAX].sort_values('media_num', ascending=False)

cl = tec['clube_id'].apply(translate_clube_id)
tec['clube'] = cl

print("TECNICOS")
print(tec)

