import sys
from data_struct.formatjson import criarjson
from data_struct.tree import Tree
from encontrar_freque import main
sys.setrecursionlimit(15000)

tree = Tree('root')

dataset_list,palavras_inicial_frequencia = main()

for sample in dataset_list:
    for word in sample:
        if not tree.navigate_to(word):
            tree.add_node(word)
            tree.navigate_to(word)
    tree.reset()

criarjson(dataset_list,palavras_inicial_frequencia)
