#tozihat : barname python chap kardan tamami onsor hayeh yek bst
class Node:
    #sakhtan yek gereh jadid ba estefade az sazandeh class gereh, 2 parametr daryaft mi konad
    def __init__(self, data):
        self.left = None
        self.right = None
        self.node = data
    #agar onsor kochak tar az rishe bashad dar samt chap zir derakht jay mi girad
    #agar onsor Bozorg tar az rishe bashad dar samt rast zir derakht jay mi girad
    def insert(self, data):
        if self.node:
            if data < self.node:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.node:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.node = data
    #chap derahkt bst dar halat peymayesh inorder 
    def Print_Tree(self):
        if self.left:
            self.left.Print_Tree()
        print(self.node, end=' ')
        if self.right:
            self.right.Print_Tree()
#tarif gam halghe while
j = 1
#daryaft tedad gere ha
i = int(input("Tedad gereh ha : "))
#daryaft rishe
root = Node(int(input("Rishe ra vared konid : ")))
while (j < i):
    j += 1
    #daryaft meghdar gereh
    x = int(input("meghdar gereh : "))
    #jay gozari dar derakht
    root.insert(x)
#chap kardan derakht
root.Print_Tree()
