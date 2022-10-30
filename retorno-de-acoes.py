from tracemalloc import start
from turtle import end_fill
import pandas as pd 
from pandas_datareader import data as pdr 


input_string = input("Insira as empreas que você quer comparar separando-as por um espaço ")
data_inicial = input("Insira a data inicial que você quer ter como base para analise - mes-dia-ano -")
data_final = input("Insira a data inicial que você quer ter como base para analise - mes-dia-ano -")


list  = input_string.split()
dados_bancarios = pdr.get_data_yahoo(list, data_inicial, end = data_final)['Adj Close']
print(dados_bancarios)

lista = dados_bancarios
def retorno (lista):
    retorno = lista[-1]/lista[0] - 1
    return retorno
print (retorno)