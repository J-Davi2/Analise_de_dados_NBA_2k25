# 🏀 NBA 2K25 Dataset Analysis with Pandas

Este projeto é uma análise exploratória de dados (EDA) feita com o dataset `NBA 2K25`, utilizando Python e a biblioteca Pandas. O objetivo foi praticar e demonstrar conhecimentos em limpeza de dados, manipulação e extração de insights relevantes.

---

## 📦 Dataset

O dataset foi retirado do Kaggle e contém informações sobre jogadores da NBA, como altura, peso, time, posição, nacionalidade, experiência, entre outros.

---

## 🧹 Limpeza e Preparação

Antes da análise, foi necessário realizar alguns tratamentos no conjunto de dados:

- ✅ Conversão de altura (ex: `6-8` → `203cm`)
- ✅ Remoção de dados duplicados

---

## 📊 Análises Realizadas

### 🔹 Análises Básicas

- Quantos jogadores há em cada posição (`POS`)?
- Quantos jogadores por nacionalidade? 
- Quantos jogadores têm altura maior que 200cm (2m)?
- Quantos jogadores não têm número (`NUMBER`) preenchido?

### 🔹 Análises Intermediárias

- Qual a universidade mais frequente entre os jogadores?
- Quantos jogadores são novatos (rookies)?
- Qual time tem mais jogadores acima de 2 metros?
- Ranking dos times com maior média de peso.
- Quais posições são mais comuns por time?

---

# Começo da Analise

## 🚀 Início da Análise

Para começar a análise exploratória do dataset NBA 2K25, realizamos alguns passos essenciais de **limpeza e padronização dos dados**. Abaixo estão os principais pontos:

---

### 📏 Conversão da Altura (Pés & Polegadas → Centímetros)

A coluna de altura apresentava os valores no formato americano, utilizando pés e polegadas (ex: `6-8`). Para facilitar a análise e padronizar os dados para o sistema métrico (cm), foi criada a seguinte função:

```python
def Pes_polegadas(x: str):
    partes = x.split("-")
    pes = float(partes[0])
    polegadas = float(partes[1])
    soma_x = (pes * 30.48) + (polegadas * 2.54)
    return round(soma_x, 1) 
```
Essa função foi aplicada à coluna HEIGHT, convertendo todos os valores para centímetros.

---

## 🧹 Remoção de Dados Duplicados

Antes de iniciar a análise, identificamos a presença de jogadores duplicados na base. Para resolver isso, utilizamos o seguinte comando:

```python
df.drop_duplicates(subset=["PLAYER", "NUMBER", "POS", "BIRTH_DATE", "NATIONALITY"])
```

Com o "drop_duplicates", conseguimos remover os dados baseados no que queremos, no caso dessa análise, removemos os dados duplicados com base nas colunas: "PLAYER", "NUMBER", "POS", "BIRTH_DATE", "NATIONALITY"

Após essa limpeza, a base de dados passou de 700 para 537 linhas, garantindo que cada jogador fosse único.

---

## 📊 Análises Iniciais

Com os dados limpos, diversas análises foram realizadas para extrair insights relevantes:

### 🔸 Distribuição por Posição (POS)

Aqui pegamos as posições dos jogadores e vamos ver quantos jogadores existem em cada posição, utilizando o ".value_counts()" aplicando na coluna que desejada, nesse caso na coluna "POS", da pra se obter os resultados de forma facilitada.

Quantidade de jogadores em cada posição:

    POS	count
0	SG	141
1	PF	104
2	SF	102
3	PG	98
4	C	92

Esse foi o resultado mostrado no final, cada posição e quantos jogadores existem em cada uma.

---

### 🌎 Nacionalidade dos Jogadores

Novamente utilizando o ".value_counts()", mas, aplicado na coluna "NATIONALITY" 

	NATIONALITY	count
0	    US US	416
1	    CA CA	24
2	    AU AU	14
3	    FR FR	12
4	    DE DE	6
5	    RS RS	4
6	    CM CM	4
7	    NG NG	4
8	    CH CH	3
9	    BS BS	3
10	    CD CD	3
11	    JP JP	3
12	    BE BE	3
13	    BA BA	3
14	    SE SE	2
15	    UA UA	2
16	    ES ES	2
17	    NL NL	2
18	    GB GB	2
19	    SI SI	2
20	    IT IT	2
21	    DO DO	1
22	    SN SN	1
23	    CZ CZ	1
24	    PT PT	1
25	    GR GR	1
26	    LV LV	1
27	    BR BR	1
28	    UK UK	1
29	    HR HR	1
30	    ML ML	1
31	    NZ NZ	1
32	    TR TR	1
33	    GE GE	1
34	    JM JM	1
35	    SD SD	1
36	    IL IL	1
37	    SS SS	1
38	    LT LT	1
39	    AT AT	1
40	    LC LC	1
41	    FI FI	1

Esse foi o resultado mostrado.
Como mostrado, sabemos que temos um jogador Brasileiro na NBA. Nosso menino Gui Santos tem se mostrado muito bom jogador. Apenas uma curiosidade hehe.

---

### 📏 Jogadores com Mais de 2m

Aqui primeiro filtrei a coluna "HEIGHT" pegando os valores > 200 (Maior que 200Cm), logo em seguida foi aplicado um ".reset_index()" e um ".sort_values(by="HEIGHT")", deixando o resultado em ordem crescente mostrando no formato de DataFrame.

```python
maiores_Que_2M = novo_df[novo_df["HEIGHT"] > 200].reset_index().sort_values(by="HEIGHT")
maiores_Que_2M
```

Mas para mostrar apenas o resultado, também pode ser aplicado o: 

maiores_Que_2M.shape[0]

Sendo assim, o resultado é igual a "272". 
Então, existem 272 jogadores maiores que 2m (200Cm)

---

### ❌ Jogadores Sem Número de Camisa

Para identificar jogadores sem número registrado:

```python
semNumber = novo_df["NUMBER"].isnull().sum()
semNumber
```

Usando o ".isnull()" acompanhado do ".sum()", aplicados na coluna "NUMBER", pegamos os jogadores que tem um "NaN" como valor na coluna que pedimos e, somamos o resultado logo em seguida.

Mas assim apenas é mostrado o resultado final.
Para visualizar em formato de DataFrame, podemos utilizar:

```python
novo_df[novo_df["NUMBER"].isnull()]
```

Assim ele mostra um DataFrame detalhado e legal.

E no final o valor de jogadores que não possuem o valor em "NUMBER", é igual a 9 jogadores.

---

## Mais algumas analises que considerei Intermediaria 

### Qual a universidade mais frequente entre os jogadores?

Novamente sendo resolvido de forma simples, utilizando o ".value_counts()", podemos fazer uma analise de forma mais apenas aplicando na coluna analisada, no caso a coluna "COLLEGE"

```python
colegio_frequente = novo_df["COLLEGE"].value_counts().reset_index()
colegio_frequente
```

de forma simples, utilizando o .idxmax(), ele retornaria o nome que mais aparece na analise. da mesma forma que usando o .max(), ele mostraria a quantidade de vezes que aparece

### Quantos jogadores são novatos (rookies)?



### 🏀 Time com mais jogadores acima de 2 metros

Aqui agrupamos os jogadores com mais de 200cm de altura por time e ordenamos para descobrir o time com mais gigantes:

```python
maior_q2 = novo_df[novo_df["HEIGHT"] > 200].groupby(by=["Team"])["HEIGHT"].count().sort_values(ascending=False).reset_index().iloc[0]
maior_q2
```

retornando: 
Team      DENVER NUGGETS
HEIGHT                13

### ⚖️ Média de peso por time

A média de peso por equipe foi calculada assim:

```python
novo_df.groupby(by=["Team"])["WEIGHT"].mean().sort_values(ascending=False)
```

Utilizando o groupBy conseguimos chegar a um resultado bem bacana das medias de peso por time. Porém ficou muito grande para colocar aqui, então, aqui vão os 5 primeiros:

Team
DENVER NUGGETS                      224.722222
LOS ANGELES LAKERS                  224.705882
HOUSTON ROCKETS                     220.722222
PHILADELPHIA WARRIORS               220.000000
SACRAMENTO KINGS                    218.470588

### 🧩 Qual posição é mais comum em cada time?

Essa análise mostra a posição mais frequente em cada equipe:

```python
novo_df.groupby(by=["Team"])["POS"].value_counts().groupby(level=0).head(1).reset_index(name="count")
```
Utilizando dois groupby, conseguimos chegar ao resultado esperado. mas novamente ficou bastante informação, então os 5 primeiros times são: 

            Team	    POS	count
0	ATLANTA HAWKS	    SG	6
1	BOSTON CELTICS	    C	5
2	BROOKLYN NETS	    PF	5
3	CHARLOTTE HORNETS 	SG	8
4	CHICAGO BULLS	    PG	5

são as posições mais frequentes das 5 primeiras equipes.

## Conclusão

Obrigado por ter chegado até aqui, ainda estou aprendendo, mas sempre procuro fazer algo legal e da melhor forma possivel.

## 🔗 Contato

[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/jos%C3%A9-davi-779356240) [![instagram](https://img.shields.io/badge/instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/davi_dg_21?igshid=ZDdkNTZiNTM=) [![github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/J-Davi2) 

Whatsapp: https://api.whatsapp.com/send?phone=5581982425993

📧 E-mail: j.davi2077t@gmail.com

📞 Entre em contato por meio dessas redes sociais, ou envie uma mensagem no meu perfil do GitHub. Estou sempre aberto a novas oportunidades e desafios. 