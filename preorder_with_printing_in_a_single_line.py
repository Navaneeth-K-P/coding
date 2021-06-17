q=[]
def preOrder(root):
    preOrderRun(root)
    #printing an array in a single line
    for i in range(0,len(q)):
        if(i==len(q)-1):
            print(q[i],end="\t")#waits untill the newline char is recieved before printing
        else:
            print(q[i],end=" ")

def preOrderRun(root):
    #Write your code here
    q.append(root.info)
    #print(q)
    #print("lol")
    if(root.left is not None):
        preOrderRun(root.left)
        #print("1")
    if(root.right is not None):
        preOrderRun(root.right)
        #print("2")
