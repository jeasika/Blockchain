#############################
# By: Jeasika López
#       A00821863
# Desarrollo de árbol Merkle
#############################

import hashlib

#Definicion de un nodo del arbol merkle
class MerkleNode(object):
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = hashlib.sha256(val.encode('utf-8')).hexdigest()

#Construccion de arbol
def createTree(nodes):
    list_len = len(nodes)
    if list_len == 0:
        return 0
    else:
        while list_len %2 != 0:
            nodes.extend(nodes[-1:])
            list_len = len(nodes)
        secondary = []
        for k in [nodes[x:x+2] for x in range(0, list_len, 2)]:
            d1 = k[0].val.encode()
            d2 = k[1].val.encode()
            md5 = hashlib.md5()
            md5.update(d1+d2)
            newdata = md5.hexdigest()
            node = MerkleNode(left=k[0], right=k[1], val=newdata) #Va agregando la data
            secondary.append(node)
        if len(secondary) == 1:
            return secondary[0]
        else:
            return createTree(secondary) #Es recursivo

#Recorre el árbol con In-Order
def dfs(root):
    if  root != None:
        print("root:", root.data)
        dfs(root.left)
        dfs(root.right)
    print()

#Utiliza una queue para recorrer el arbol
def bfs(root):
    print('START BFS: ')
    queue = []
    queue.append(root)
    while(len(queue)>0):
        e = queue.pop(0)
        print(e.val)
        if e.left != None:
            queue.append(e.left)
        if e.right != None:
            queue.append(e.right)

############################
# Aquí inicia el main()
############################
if __name__ == "__main__":
    blocks = ['A','B','C','D']
    nodes = []
    print("leaf hash")
    for e in blocks:
        md5 = hashlib.md5()
        md5.update(e.encode())
        d=md5.hexdigest()
        nodes.append(MerkleNode(val=d))
        print(d)
    root = createTree(nodes)
    bfs(root)