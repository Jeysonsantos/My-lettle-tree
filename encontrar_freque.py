import pandas as pd
from nltk.tokenize import word_tokenize
#from bigtree import dict_to_tree, print_tree,list_to_tree

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------  

stop_words ={',','´-','A','O','.','(',')','{','}','[',']','-','!','@','#','$','%','&','*',';',':','/','=','_','estiver', 'estivemos', 'houver', 'forem', 'tínhamos', 'fora', 'terei', 'teve', 'dele', 'houveram', 'éramos', 'foi', 'haver', 'essa', 'pelas', 'tivesse', 'tive', 'ou', 'tivera', 'as', 'qual', 'hão', 'tem', 'a', 'é', 'no', 'estejam', 'estivera', 'estivermos', 'minha', 'estivéssemos', 'houvéssemos', 'mas', 'mesmo', 'à', 'nas', 'são', 'aqueles', 'tua', 'estavam', 'somos', 'entre', 'houvemos', 'haja', 'não', 'estivéramos', 'aquele', 'houverei', 'nossas', 'uma', 'os', 'estive', 'nosso', 'terão', 'tivéssemos', 'houveriam', 'eram', 'seus', 'houvesse', 'quem', 'aos', 'estivesse', 'lhes', 'muito', 'ao', 'delas', 'esta', 'estejamos', 'depois', 'estas', 'fôramos', 'de', 'que', 'esteve', 'ela', 'mais', 'seríamos', 'lhe', 'terá', 'com', 'pelos', 'tivemos', 'nos', 'fomos', 'sou', 'temos', 'tivéramos', 'nossa', 'há', 'vocês', 'estão', 'me', 'tenho', 'estivessem', 'teu', 'era', 'eles', 'para', 'estiverem', 'você', 'houveríamos', 'fosse', 'seu', 'houverem', 'tiveram', 'esteja', 'sem', 'tenham', 'ser', 'tenha', 'do', 'nós', 'numa', 'tu', 'estamos', 'deles', 'sejamos', 'estava', 'isso', 'seremos', 'vos', 'num', 'houvessem', 'esses', 'até', 'houveria', 'houve', 'teremos', 'hajamos', 'essas', 'suas', 'tivermos', 'sua', 'ele', 'o', 'foram', 'tivessem', 'houvéramos', 'se', 'também', 'está', 'pelo', 'meus', 'estiveram', 'sejam', 'tiverem', 'como', 'dos', 'fossem', 'das', 'houvermos', 'elas', 'formos', 'já', 'hei', 'tinha', 'pela', 'isto', 'houverão', 'meu', 'estar', 'quando', 'nossos', 'teríamos', 'aquilo', 'eu', 'nem', 'na', 'teria', 'tiver', 'teus', 'aquela', 'houvera', 'for', 'serei', 'e', 'por', 'seja', 'só', 'fui', 'da', 'tinham', 'havemos', 'te', 'houveremos', 'estes', 'teriam', 'tuas', 'estou', 'será', 'fôssemos', 'hajam', 'um', 'serão', 'este', 'aquelas', 'houverá', 'tém', 'estávamos', 'em', 'dela', 'minhas', 'às', 'tenhamos', 'esse', 'seria', 'seriam'
}

retirar=["/","\\","'"]


#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------
       
def frequencia(palavra):
    freq_da_palavra=0
    for i in dataset_list:
        if i:
            if palavra == i[0]:
                freq_da_palavra=freq_da_palavra+1
    
    return freq_da_palavra

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------  

def palavra_maior_freq():
    for frase in dataset_list:
        for palavra in frase:
            if palavra not in palavras_ja_consultadas:
                freq = frequencia(palavra)
                palavras_ja_consultadas.append(palavra)
                palavras_inicial_frequencia[palavra]=freq
                
    for i in sorted(palavras_inicial_frequencia, key = palavras_inicial_frequencia.get, reverse=True):
        break
    return i

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------  

def sentecas_palavra_freq(palavra_maior_frequencia):
    lista_palavra_freq =[]
    for i in dataset_list:
        if palavra_maior_frequencia in i:
            lista_palavra_freq.append(i)
    
    return lista_palavra_freq

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------  

def tokenizar(frase,stop_words):
    word_tokens = word_tokenize(frase)
    
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
    
    filtered_sentence = []
    aux=0
    for w in word_tokens:
        if w not in stop_words:
            if (w != "''") and (w!="``"):
                for i in w:
                    if i in retirar:
                        aux=1
                if aux==0:
                    filtered_sentence.append(w)
            
    return filtered_sentence

#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------  

def eliminar_freq_zero(palavras_inicial_frequencia):
    novo_dici = {}
    for i in palavras_inicial_frequencia:
        if (palavras_inicial_frequencia.get(i))!=0:
            novo_dici[i]=palavras_inicial_frequencia.get(i)
    return novo_dici


#--------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------  

def main():
    global dataset_list
    global palavras_inicial_frequencia
    global palavras_ja_consultadas
    global palavra_maior_frequencia
    global sentencas_com_palavra_mais_freq
    global dataset

    try:
        dataset = pd.read_excel("licoes_aprendidas.xlsx")
    except:
        dataset = pd.read_excel("/Users/Teteu/Desktop/arvore-python/licoes_aprendidas.xlsx")
    
    dataset = dataset.drop_duplicates()
    dataset = dataset.dropna()
    dataset_list = dataset['textos'].tolist()

    palavras_inicial_frequencia={}
    palavras_ja_consultadas=[]
    
    for indice, frase in enumerate(dataset_list):
        dataset_list[indice] = tokenizar(frase,stop_words)
        
    palavra_maior_frequencia=palavra_maior_freq()
    sentencas_com_palavra_mais_freq = sentecas_palavra_freq(palavra_maior_frequencia)
    palavras_inicial_frequencia = eliminar_freq_zero(palavras_inicial_frequencia)
   


    return dataset_list,palavras_inicial_frequencia