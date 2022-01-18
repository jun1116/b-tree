from BTree_HJ import BTree#, Node
import csv
import os
def search(dir):
    filenames = os.listdir(dir)
    # for filename in filenames:
    #     print(filename)
        # fullname=os.path.join(dir,filename)
        # print(fullname)
    return filenames
if __name__=="__main__":
    m = input("Enter the M order of B-Tree (default is 5) ")
    bt=BTree(m)
    while True:
        print("Press number you want to start and [ENTER]")
        num = input("1. insertion \t2.deletion \t3.quit \n")
        if num=='1': # Insertion
            fnames=', '.join([i for i in search('./data') if i[:5]=='input'])
            inputname=input(f"Write the file name to Input (ex. {fnames} )\n")
            fname="./data/" + inputname
            try:
                f = open(fname,'r')
                temp=0
                for line in csv.reader(f,delimiter='\t'):
                    key,value = line[0] , line[1]
                    # print(key,value)
                    bt.insert_node(bt.root,[key,value])
                    temp+=1
                    if temp==5:break
                
            
            except:
                print(f'There is No File {inputname}\nCheck the file name')


            pass
        elif num=='2': # Deletion
            pass
        elif num=='3': # Quit
            print("STOP THE LOOP")
            break
    # bt = BTree(3)
    # bt.insert_node(bt.root,[1,2])
    # bt.insert_node(bt.root,[2,3])
    # bt.print_inorder(bt.root)

