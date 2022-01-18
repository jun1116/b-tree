from BTree_HJ import BTree#, Node
import csv
import os
def search(dir): return os.listdir(dir)

if __name__=="__main__":
    m = int(input("Enter the M order of B-Tree (default is 5) "))
    bt=BTree(m if m>3 else 3)
    while True:
        print("Press number you want to start and [ENTER]")
        num = input("1. insertion \t2.deletion \t3.quit \n")
        if num=='1': # Insertion
            ## Insert
            fnames=', '.join([i.split('.')[0] for i in search('./data') if i[:5]=='input'])
            inputname=input(f"Write the Input file name With out extension (ex. {fnames} )\n")
            fname="./data/" + inputname + '.csv'
            keylist=[]
            try:
                f = open(fname,'r')
                temp=0
                for line in csv.reader(f,delimiter='\t'):
                    key,value = int(line[0]) , int(line[1])
                    keylist.append(int(key))
                    bt.insert_node(bt.root,[key,value])
            except:
                print(f'There is No File {inputname}\nCheck the file name')
            
            ## Search and Write
            with open(f"./data/{inputname}_compare.csv",'a',newline='') as f:
                wr=csv.writer(f,delimiter='\t')
                for k in keylist:
                    _ , kv = bt.search_key(bt.root,[k,None])
                    if kv:
                        wr.writerow(kv)
                    else:
                        wr.writerow([k,'NF'])

            ## Compare
            # with open(fname,'r') as ori:
            #     with open(f"./data/{inputname}_compare.csv",'r') as comp:
            #         ori.readlines
            
        elif num=='2': # Deletion
            pass
        elif num=='3': # Quit
            print("STOP THE LOOP")
            break
    # bt = BTree(3)
    # bt.insert_node(bt.root,[1,2])
    # bt.insert_node(bt.root,[2,3])
    # bt.print_inorder(bt.root)

