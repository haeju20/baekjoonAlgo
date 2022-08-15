#1991
import sys
#전위 순회
def preorder(node):
    if node != '.':
        print(node, end="")
        preorder(Tree[node][0])
        preorder(Tree[node][1])

#중위 순회
def inorder(node):
    if node != '.':
        inorder(Tree[node][0])
        print(node, end="")
        inorder(Tree[node][1])

#후위 순회
def postorder(node):
    if node != '.':
        postorder(Tree[node][0])
        postorder(Tree[node][1])
        print(node, end = "")

N = int(sys.stdin.readline())
Tree = dict()
for _ in range(N):
    root, lnode, rnode = map(str, sys.stdin.readline().split())
    Tree[root] = lnode, rnode

preorder('A')
print()
inorder('A')
print()
postorder('A')

#2250


#11725


#1167


#1967
