#%%
import pandas as pd 

# %%

df = pd.read_csv("../data/nba_2k25.csv")

#%%

df

# %%

# função que converte a coluna altura para Cm

def Pes_polegadas(x:str):
    partes = x.split("-")
    pes = float(partes[0])
    polegadas = float(partes[1])
    soma_x= (pes * 30.48) + (polegadas * 2.54)
    return round(soma_x, 1)

#%%

# Fazendo a aplicação

df["HEIGHT"] = df["HEIGHT"].apply(Pes_polegadas)

#%%

# Atribuindo a uma nova variavel

df_tratado = df


#%%

df_tratado

#%%

# Deletando dados iguais baseados em 5 colunas 

novo_df = df_tratado.drop_duplicates(subset=["PLAYER", "NUMBER", "POS", "BIRTH_DATE", "NATIONALITY"])

# %%

novo_df

# %%

novo_df["POS"].value_counts().reset_index()

# %%

nacional_qtd = novo_df["NATIONALITY"].value_counts().reset_index()
nacional_qtd

# %%

maiores_Que_2M = novo_df[novo_df["HEIGHT"] > 200].reset_index().sort_values(by="HEIGHT")
maiores_Que_2M

# %%

maiores_Que_2M.shape[0]

# %%

semNumber = novo_df["NUMBER"].isnull().sum()
semNumber

# %%

novo_df[novo_df["NUMBER"].isnull()]

# %%

colegio_frequente = novo_df["COLLEGE"].value_counts().reset_index()
colegio_frequente

# %%

novo_df["COLLEGE"].value_counts().idxmax()  # nome
   
# %%

novo_df["COLLEGE"].value_counts().max()  # quantidade

# %%

novo_df[novo_df["EXPERIENCE"] == "R"].groupby(by="PLAYER")["EXPERIENCE"].nunique().count()
# %%

maior_q2 = novo_df[novo_df["HEIGHT"] > 200].groupby(by=["Team"])["HEIGHT"].count().sort_values(ascending=False).reset_index().iloc[0]
maior_q2
# %%

novo_df.groupby(by=["Team"])["WEIGHT"].mean().sort_values(ascending=False)
# %%

novo_df.groupby(by=["Team"])["POS"].value_counts().groupby(level=0).head(1).reset_index(name="count")
# %%
