from data_struct.tree import Tree
from encontrar_freque import main

tree = Tree('root')

samples = main()

for sample in samples:
    for word in sample:
        if not tree.navigate_to(word):
            tree.add_node(word)
            tree.navigate_to(word)
    tree.reset()

tree.printTree(tree.root)



'''path=[]
soma_string="raiz/"

x=['raiz/montagem/BHA/reduzido/apenas/01/seção/Comandos/8/''/''/+/01/'] - tirar essas aspas para mostrar arvore

for position,text in enumerate(sentencas_com_palavra_mais_freq):
    for i in text:
        if (i != " '' "):
            soma_string=soma_string+i+'/'
    path.append(soma_string)
    soma_string="raiz/"
        

root = list_to_tree(x)
print_tree(root)'''