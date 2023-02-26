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