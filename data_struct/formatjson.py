import pandas as pd
from nltk.tokenize import word_tokenize
import json

from encontrar_freque import main

def verificar_inicio(frase):
    aux=0
    if dici_dados and frase:
        for i in dici_dados:
            if (i.get("palavra") == frase[0]):
                aux=1
        return aux
    else:
        return 0
    
#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------  

def criar_novo_ramo(palavra):
    if(palavra):
        dici_dados.append({"palavra":palavra,"chance":"nada ainda % ","proximo":[]})
    
    return 0

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def add_ja_existente(endereco,palavra_anterior,palavra_adicionar):
    if endereco["palavra"] == palavra_anterior:
        aux=0
        for i in endereco["proximo"]:
            if i["palavra"] == palavra_adicionar:
                aux=1
        if (aux!=1):
            endereco["proximo"].append({"palavra":palavra_adicionar,"chance":"nada ainda %","proximo":[]})
            aux=0
    else:
        for novo_endereco in endereco["proximo"]:
            add_ja_existente(novo_endereco,palavra_anterior,palavra_adicionar)
    return 0
 

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def endereco_palavra_inicial(palavra):
    for pos,i in enumerate(dici_dados):
        if i["palavra"]==palavra:
            return pos

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def criar_json(frase):
    try:
        endereco = endereco_palavra_inicial(frase[0])
        for pos,palavra in enumerate(frase[1:]):
            if (palavra!=""):
                add_ja_existente(dici_dados[endereco],frase[pos],palavra)      
    except:
        return 0

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def main2(a,b):
    global dici_dados
    global dataset_list
    global palavras_inicial_frequencia
    dici_dados = []
    dataset_list=a
    palavras_inicial_frequencia = b
    for palavra in palavras_inicial_frequencia:
        criar_novo_ramo(palavra)
    for frase in dataset_list:
        print(frase)
        criar_json(frase)
    print(json.dumps(dici_dados, indent='\t'))
