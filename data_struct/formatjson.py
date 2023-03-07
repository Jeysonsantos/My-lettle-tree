import pandas as pd
from nltk.tokenize import word_tokenize
import json
from encontrar_freque import main
global dici_dados
dici_dados = []

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
                break
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
            return dici_dados[pos]

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def criar_json(frase):
    try:
        endereco = endereco_palavra_inicial(frase[0])
        for pos,palavra in enumerate(frase[1:]):
            if (palavra!=""):
                add_ja_existente(endereco,frase[pos],palavra)      
    except:
        return 0

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def porcentagem(lista):
    tamanho = len(lista)
    if(tamanho != 0):
        porcentagem = (1/tamanho)*100
    else:
        porcentagem = 0 
    porcentagem=round(porcentagem, 2)
    return porcentagem

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def adicionar_porcetagem(listas):
    for frase in listas:
        frase["chance"] = porcentagem(listas)
        adicionar_porcetagem(frase["proximo"])
        
    
    return 0

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------

def criarjson(dataset_list,palavras_inicial_frequencia):
    for palavra in palavras_inicial_frequencia:
        criar_novo_ramo(palavra)
    for frase in dataset_list:
        print(frase)
        criar_json(frase)

    adicionar_porcetagem(dici_dados)

    out_file = open("formatojson.json", "w")  
    
    json.dump(dici_dados, out_file, indent = 6)  
    
    out_file.close()  

    return 0

