import sys
from data_struct.tree import Tree
from encontrar_freque import main
from bigtree import print_tree,list_to_tree
sys.setrecursionlimit(15000)

tree = Tree('root')

samples = main()

for sample in samples:
    for word in sample:
        if not tree.navigate_to(word):
            tree.add_node(word)
            tree.navigate_to(word)
    tree.reset()

soma_string="root/"

path=[]
for position,text in enumerate(samples):
    for i in text:
            soma_string=soma_string+i+"/"
    path.append(soma_string)
    soma_string="root/"
        

root = list_to_tree(path)
print_tree(root,style="double")
