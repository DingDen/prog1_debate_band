from itertools import count
import pandas as pd
import csv, string

frame = pd.read_excel("debate_band.xlsx", usecols='F')

sem_punct = frame["Texto"].str.translate(str.maketrans('', '', string.punctuation)).str.lower()

data = sem_punct.str.split()

palavras = []
frequencia = []
palavras_sem_repeticao = []
frequencia_sem_repeticao = []

for i in data:
    palavras += i
for quant in palavras:
    frequencia.append(palavras.count(quant))

for elementos in palavras:
    if elementos not in palavras_sem_repeticao:
        palavras_sem_repeticao.append(elementos)
for numeros in frequencia:
    if numeros not in frequencia_sem_repeticao:
        frequencia_sem_repeticao.append(numeros)

colunas = ['PALAVRA', 'FREQUÊNCIA'] 
linhas = list(zip(palavras_sem_repeticao, frequencia_sem_repeticao))

with open ('word_frequence.csv', 'w', newline='') as f:
    arquivo = csv.writer(f, delimiter=';')
    arquivo.writerow(colunas)
    arquivo.writerows(linhas)
