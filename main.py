from BTree_HJ import BTree #, Node
import csv
import os

def search(dir): return os.listdir(dir)
def compare(file1,file2):
    t,f=0,0
    with open(file1,'r') as f1:
        with open(file2,'r') as f2:
            reader1=csv.reader(f1, delimiter='\t')
            reader2=csv.reader(f2, delimiter=',')
            for l1,l2 in zip(reader1,reader2):
                if l1==l2:
                    t+=1
                else:
                    f+=1
    return t,f


if __name__=="__main__":
    m = int(input("Enter the M order of B-Tree (default is 5) "))
    # bt=BTree(5 if m<3 or m=='' else m)
    print("Press number you want to start and [ENTER]")
    while True:
        bt=BTree(5 if m<3 or m=='' else m)
        num = input("1. insertion \t2.deletion \t3.quit \n")
        if num=='1': # Insertion
            ## Insert
            fnames=', '.join([i.split('.')[0] for i in search('./data') if i[:5]=='input'])
            inputname=input(f"Write the Input file name With out extension \n(ex. {fnames} )\n")
            fname="./data/" + inputname + '.csv'
            keylist=[]
            try:
                # f = open(fname,'r')
                with open(fname,'r',newline='',encoding='utf-8') as f:
                    temp=0
                    for line in csv.reader(f,delimiter='\t'):
                        key,value = int(line[0]) , int(line[1])
                        keylist.append(int(key))
                        bt.insert_node(bt.root,[key,value])
            except:
                print(f'There is No File {inputname}\nCheck the file name')
                continue
            
            ## Search and Write
            with open(f"./data/{inputname}_compare.csv",'w', newline='',encoding='utf-8') as f:
                wr=csv.writer(f,delimiter=',')
                for k in keylist:
                    _ , kv = bt.search_key(bt.root,[k,None])
                    if kv:
                        wr.writerow(kv)
                    else:
                        wr.writerow([k,'NF'])

            ## Compare
            t,f=compare(fname, f'./data/{inputname}_compare.csv')
            print(f'Data Count = {t+f} , Correct : {t} , Incorrect : {f} , True Percent : {100*t/(t+f)}%')
                    
        elif num=='2': # Deletion
            pass
        elif num=='3': # Quit
            print("STOP THE LOOP")
            break

