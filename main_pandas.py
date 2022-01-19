from BTree_HJ import BTree #, Node
import csv
import os
import pandas as pd
from tqdm import tqdm

def search(dir): return os.listdir(dir)
def compare_df(origin,compare):
    odf=pd.read_csv(origin, sep="\t", names=["key","value"])
    cdf=pd.read_csv(compare, sep=",", names=["key","value"])
    mdf=pd.merge(odf,cdf,how="outer",on='key', suffixes=["_origin","_compare"]).fillna("NF")
    mdf["incorrect"]=mdf.apply(lambda x : 0 if x['value_origin']==x['value_compare'] else 1, axis="columns")
    return mdf


if __name__=="__main__":
    tqdm.pandas()
    m = int(input("Enter the M order of B-Tree (default is 5) "))
    print("Press number you want to start and [ENTER]")
    while True:
        bt=BTree(5 if m<3 or m=='' else m)
        num = input("1. insertion \t2.deletion \t3.quit \n")
        if num=='1': # Insertion
            ## Insert
            fnames=', '.join([i.split('.')[0] for i in search('./data') if i[:5]=='input'])
            inputname=input(f"Write the Input file name With out extension \n(ex. {fnames} )\n")
            fname="./data/" + inputname + '.csv'
            compare_name = f"./data/{inputname}_compare.csv"
            print("\nInsertion Start\n")
            inputdf=pd.read_csv(fname,sep='\t',names=['key','value'])
            for idx,row in tqdm(inputdf.iterrows(), total=inputdf.shape[0]):
                bt.insert_node(bt.root, [row['key'],row['value']])

            print("\nSearch Start\n")
            # Search and Write to CSV            
            arr=[]
            for idx,row in tqdm(inputdf.iterrows(), total=inputdf.shape[0]):
                    _ , kv = bt.search_key(bt.root, [row['key'],None])
            sdf = pd.DataFrame(arr, columns=['key','value'])
            sdf.to_csv(compare_name, index=False, sep=",",encoding='utf-8',header=False, mode='w')
            
            ## Compare
            print("\nCompare Start\n")
            mdf=compare_df(fname, f'./data/{inputname}_compare.csv')
            t , f = len(mdf)-sum(mdf['incorrect']) , sum(mdf['incorrect'])
            print(f'Data Count = {t+f} , Correct : {t} , Incorrect : {f} , True Percent : {100*t/(t+f)}%')

        elif num=='2': # Deletion
            pass
        elif num=='3': # Quit
            print("STOP THE LOOP")
            break

