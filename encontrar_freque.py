import pandas as pd
from nltk.tokenize import word_tokenize


stop_words ={'/',',','A','O','.','(',')','{','}','[',']','-','!','@','#','$','%','&','*',';',':','/','=','_','estiver', 'estivemos', 'houver', 'forem', 'tínhamos', 'fora', 'terei', 'teve', 'dele', 'houveram', 'éramos', 'foi', 'haver', 'essa', 'pelas', 'tivesse', 'tive', 'ou', 'tivera', 'as', 'qual', 'hão', 'tem', 'a', 'é', 'no', 'estejam', 'estivera', 'estivermos', 'minha', 'estivéssemos', 'houvéssemos', 'mas', 'mesmo', 'à', 'nas', 'são', 'aqueles', 'tua', 'estavam', 'somos', 'entre', 'houvemos', 'haja', 'não', 'estivéramos', 'aquele', 'houverei', 'nossas', 'uma', 'os', 'estive', 'nosso', 'terão', 'tivéssemos', 'houveriam', 'eram', 'seus', 'houvesse', 'quem', 'aos', 'estivesse', 'lhes', 'muito', 'ao', 'delas', 'esta', 'estejamos', 'depois', 'estas', 'fôramos', 'de', 'que', 'esteve', 'ela', 'mais', 'seríamos', 'lhe', 'terá', 'com', 'pelos', 'tivemos', 'nos', 'fomos', 'sou', 'temos', 'tivéramos', 'nossa', 'há', 'vocês', 'estão', 'me', 'tenho', 'estivessem', 'teu', 'era', 'eles', 'para', 'estiverem', 'você', 'houveríamos', 'fosse', 'seu', 'houverem', 'tiveram', 'esteja', 'sem', 'tenham', 'ser', 'tenha', 'do', 'nós', 'numa', 'tu', 'estamos', 'deles', 'sejamos', 'estava', 'isso', 'seremos', 'vos', 'num', 'houvessem', 'esses', 'até', 'houveria', 'houve', 'teremos', 'hajamos', 'essas', 'suas', 'tivermos', 'sua', 'ele', 'o', 'foram', 'tivessem', 'houvéramos', 'se', 'também', 'está', 'pelo', 'meus', 'estiveram', 'sejam', 'tiverem', 'como', 'dos', 'fossem', 'das', 'houvermos', 'elas', 'formos', 'já', 'hei', 'tinha', 'pela', 'isto', 'houverão', 'meu', 'estar', 'quando', 'nossos', 'teríamos', 'aquilo', 'eu', 'nem', 'na', 'teria', 'tiver', 'teus', 'aquela', 'houvera', 'for', 'serei', 'e', 'por', 'seja', 'só', 'fui', 'da', 'tinham', 'havemos', 'te', 'houveremos', 'estes', 'teriam', 'tuas', 'estou', 'será', 'fôssemos', 'hajam', 'um', 'serão', 'este', 'aquelas', 'houverá', 'tém', 'estávamos', 'em', 'dela', 'minhas', 'às', 'tenhamos', 'esse', 'seria', 'seriam'
}
retirar=["/","\\","'"]

def eliminar_duplicado(dataset):
    dataset_list = dataset['textos'].tolist()
    aux_texto=''
    lista_parada=[1]
    while(lista_parada):
        del lista_parada[0]
        for indice, texto in enumerate(dataset_list):
            if (texto == aux_texto):
                del dataset_list[indice]
                lista_parada.append(1)
                aux_texto=''
                break
            aux_texto = texto
    return dataset_list

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

def frequencia(palavra):
    freq_da_palavra=0
    for i in dataset_list:
        if palavra in i:
            freq_da_palavra=freq_da_palavra+1
    
    return freq_da_palavra

def palavra_maior_freq():
    for frase in dataset_list:
        for palavra in frase:
            if palavra not in palavras_ja_consultadas:
                freq = frequencia(palavra)
                palavras_ja_consultadas.append(palavra)
                palavras_frequencia[palavra]=freq
                
    for i in sorted(palavras_frequencia, key = palavras_frequencia.get, reverse=True):
        break
    return i

def sentecas_palavra_freq(palavra_maior_frequencia):
    lista_palavra_freq =[]
    for i in dataset_list:
        if palavra_maior_frequencia in i:
            lista_palavra_freq.append(i)
    
    
    return lista_palavra_freq

def main():
    global dataset_list
    global palavras_frequencia
    global palavras_ja_consultadas
    global palavra_maior_frequencia
    global sentencas_com_palavra_mais_freq
    try:
        dataset = pd.read_excel("licoes_aprendidas.xlsx")
    except:
        dataset = pd.read_excel("/Users/Teteu/Desktop/arvore-python/licoes_aprendidas.xlsx")
    
    dataset = dataset.dropna()
    dataset_list = eliminar_duplicado(dataset)
    palavras_frequencia={}
    palavras_ja_consultadas=[]
    
    for indice, frase in enumerate(dataset_list):
        dataset_list[indice] = tokenizar(frase,stop_words)
        
    palavra_maior_frequencia=palavra_maior_freq()
    sentencas_com_palavra_mais_freq = sentecas_palavra_freq(palavra_maior_frequencia)
    


    return sentencas_com_palavra_mais_freq