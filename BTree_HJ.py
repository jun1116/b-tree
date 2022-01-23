# Node
class Node:
    def __init__(self, isleaf=False):
        self.isleaf=isleaf
        self.keys=[]
        self.child=[]
    def __repr__(self):
        return f'Node :{self.keys}'
    def split(self):
        length = len(self.keys)
        temp = Node(self.isleaf)
        mid = self.keys[length//2]
        temp.keys = self.keys[length//2+1:]
        self.keys = self.keys[:length//2]
        if self.child:
            temp.child = self.child[length//2+1:]
            self.child = self.child[:length//2+1]
        return self,mid,temp

class BTree:
    def __init__(self, m):
        self.m=m #차수 -> m개의 child를 가질 수 있음
        self.root=Node(True)
        # self.root.isleaf = 'root'
        # self.root=None

    # k : Key 
    # def insert_node(self,p_pos,p_node,node,key):
    def insert_node(self,node,key):
        """ 데이터 추가하는것, Root부터 시작해서 내려가도록 Trigger가 발동되며, 
        현재의 노드(node)가 leaf가 아닐경우, 재귀적으로 child를 내려감. 
        리프에서의 삽입이 이뤄지고나면, 그대로 자기자신만 반환하고, 
        Leaf에서의 삽입이 OverFlow가 일어날경우 중간key와 자기자신을 반환
        삽입을 하고난 이후, 반환되는 key가 있다면, 해당 child에서 OverFlow가 난것이므로, 관련연산 진행
        """
        pos=0
        while pos < len(node.keys):
            # print(pos)
            if key[0]==node.keys[pos][0]:
                #Duplicate
                print(f"Duplicates key {key}")
                return node, None 
            elif key[0]<node.keys[pos][0]: break
            pos+=1
        # print(key," Node : ",node , pos)
        
        # Position 찾기 완료
        if node.isleaf==True : # Leaf라면?? -> Leaf에서의 삽입 로직
            i=len(node.keys)-1
            node.keys.append([1e9,None])
            while i>=0 and key[0]<node.keys[i][0]:
                node.keys[i+1]=node.keys[i]
                i-=1
            node.keys[i+1]=key
            if len(node.keys) >= self.m : # 오버플로 발생?
                if node == self.root:
                    # print("Root OverFlow")
                    ll,mid,rr=node.split()
                    self.root=Node(False)
                    self.root.keys.append(mid)
                    self.root.child.append(ll)
                    self.root.child.append(rr)
                    return self.root, None
                else:
                    # print("Leaf OVERFLOW",node)
                    return node, node.keys[(self.m//2)]

            else: return node, None
        # elif node.isleaf == False: #Leaf가 아니라면?
        else: #Leaf가 아니라면?
            node.child[pos], child_mid_kv = self.insert_node(node.child[pos],key)
            if child_mid_kv: # Child에서 OverFlow발생 -> 자기에 추가시켜줘야해
                ll,mid,rr=node.child[pos].split()

                i=len(node.keys)-1
                node.keys.append([1e9,None])
                node.child.append([])
                while i>=0 and mid[0] < node.keys[i][0]:
                    node.keys[i+1]=node.keys[i]
                    node.child[i+2]=node.child[i+1]
                    i-=1
                node.keys[i+1]=mid
                # i=len(node.child)-1
                node.child[i+2]=rr
                if len(node.keys) >= self.m : # 오버플로 발생?
                    if node == self.root:
                        # print("Root OverFlow")
                        ll,mid,rr=node.split()
                        self.root=Node(False)
                        self.root.keys.append(mid)
                        self.root.child.append(ll)
                        self.root.child.append(rr)
                        return self.root, None
                if len(node.keys)>=self.m:
                    return node, node.keys[(self.m//2)]
            return node, None

    def search_key(self,node,key):
        """ Find Key 
        IF FIND : RETURN [Node, Key]
        else : RETURN [None, None] """
        # print(node)
        pos=0
        while pos < len(node.keys):
            if key[0] == node.keys[pos][0]:
                # print(f'Find! key : {node.keys[pos]}')
                return node, node.keys[pos]
            elif key[0] < node.keys[pos][0] : break
            else:
                pos+=1
        # print(node, pos)
        if node.child:
            return self.search_key(node.child[pos],key)
        else : 
            return None, None
            # return f"NOT FOUND {key}"

    def print_inorder(self,node):
        if node.child:
            for i in range(len(node.keys)):
                self.print_inorder(node.child[i])
                print(node.keys[i])
            self.print_inorder(node.child[-1])
        else:
            for i in node.keys:
                print(i)
    
    def find_change_Pred(self,node,key):
#특정키의 왼쪽자식받아 오른쪽을 찾아내려가서 가장큰수의 키를 바꾸고 바꾸기전 key return
        if node.isleaf: 
            temp = node.keys[-1]
            node.keys[-1] = key
            return temp
        return self.find_change_Pred(node.child[-1],key)

    def find_change_Succ(self,node,key):
#특정키의 오른쪽자식을 받아 왼쪽으로쭉내려가 가장 작은수의 키를 바꾸고 바꾸기전 key return
        if node.isleaf:
            temp=node.keys[0]
            node.keys[0] = key
            return temp
        return self.find_change_Succ(node.child[0],key)


## DELETE PACKER
    def delete_pack(self,node,key):
        self.delete(node,key)
        if self.root.keys:
            pass
        else:
            pass
            self.root = self.root.child[0]
            # self.root.child = [i for i in self.root.child]
            # self.root = [i for i in self.root.child]

## DELETE
    def delete(self,node,key):
        pos = 0
        # FIND POSITION
        while pos<len(node.keys) and key[0] > node.keys[pos][0]:
            pos+=1

        # print("DELETE",node,"KEY : ",key,pos)

        if node.isleaf==True : # Leaf 에서 키를 찾든 못찾든
            if pos<len(node.keys) and key[0]==node.keys[pos][0]:
                node.keys.pop(pos)
                # print("find node : ",node,' key : ',key)
                # return "DELETE FROM LEAF COMPLETED" # 삭제연산완료표시
                return node
            else :
                # print("NOT FOUND")
                return node # "NOT FOUND" # 리프까지 갔는데 못찾음
        else: # Leaf가 아닌 경우
            if pos < len(node.keys):
                if key[0]==node.keys[pos][0]:
                    # 리프가 아닌데 찾은경우
                    ## Leaf에서 찾아서(Pred or Succ) 바꿔주는 연산
                    ## 바꾼이후 해당방향 child로 delete연산수행
                    # print(f"find_Internal -> change, Now Node : {node}, Now Pos : {pos}")
                    if len(node.child[pos].keys) >= len(node.child[pos].keys):
                        # print('changePred (left)',pos)
                        node.keys[pos] = self.find_change_Pred(node.child[pos],key)
                        self.delete(node.child[pos], key)
                        self.balancing_child(node,pos,pos)
                    else:
                        # print('changeSucc (right)',pos)
                        node.keys[pos] = self.find_change_Succ(node.child[pos+1],key)
                        self.delete(node.child[pos+1], key)
                        self.balancing_child(node,pos,pos+1)
                    # pass ## TODO : Internal Node Deletion Process
                else:
                    self.delete(node.child[pos],key)    
            else: # 리프가 아닌데 키값도 아닌데 pos는찾은경우 => 아래로 내려가자
                self.delete(node.child[pos],key)
        
        # print(f"Check The Node {node} 's Stability")
        ## Check Child Keys for M
        if len(node.child[pos].keys)>= self.m//2:
            # print("It is safe , RETURN",node)
            return node
        else:
            ## Not Enough Keys For child[pos] => Balancing
            # print("Not Stable => Balancing")
            node = self.balancing_child(node,pos,pos)
            return node
        

    def balancing_child(self,pnode,pos,cpos):
        # print("Balancing Child ", pnode ,"cpos :", cpos , pnode.child[cpos])
        if cpos==0:# 맨 왼쪽 자식
            # print("맨 왼쪽 자식 rebalancing")
            if self.distribute_with_right(pnode,cpos):
                return pnode
            else:
                # print("Merge")  
                self.merge(pnode,pos,cpos,cpos+1)
                pass
                ## Merge
        elif cpos==len(pnode.child)-1: # 맨 오른쪽 자식
            # print("맨 오른쪽 자식 rebalancing")
            if self.distribute_with_left(pnode,cpos):
                return pnode
            else:
                # print("Merge") 
                self.merge(pnode,pos-1,cpos-1,cpos)
                pass
            ## Merge
        else:
            # print("중간에 껴있는 자식")
            if self.distribute_with_left(pnode,cpos) :
                return pnode
            elif self.distribute_with_right(pnode,cpos):
                return pnode
            else:
                # print("중간녀석의 Merge")
                self.merge(pnode,pos-1,cpos-1,cpos)


    def distribute_with_right(self, pnode,pos):
        if len(pnode.child[pos+1].keys) >= self.m//2+1:# 오른쪽으로부터 가져오기 가능
            pnode.child[pos].keys.append(pnode.keys[pos])
            pnode.keys[pos] = pnode.child[pos+1].keys[0]
            pnode.child[pos+1].keys.pop(0)
            if pnode.child[pos+1].child: #자식이 있다면? 옮겨진곳으로 붙여주자구
                pnode.child[pos].child.append(pnode.child[pos+1].child[0])
                pnode.child[pos+1].child.pop(0)
            return True
        else:
            return False
    def distribute_with_left(self, pnode,pos):
        if len(pnode.child[pos-1].keys) >= self.m//2 + 1: # 왼쪽으로부터 가져오기 가능
            # print(f"FROM LEFT pnode: {pnode} , pos: {pos} , child: {pnode.child}")
            pnode.child[pos].keys = [pnode.keys[pos-1]] + pnode.child[pos].keys
            pnode.keys[pos-1] = pnode.child[pos-1].keys[-1]
            pnode.child[pos-1].keys.pop()
            if pnode.child[pos-1].child:
                pnode.child[pos].child = [pnode.child[pos-1].child[-1]] + pnode.child[pos].child
                pnode.child[pos-1].child.pop()
            # print(f'pnode : {pnode}, pnode.child : {pnode.child}')
            return True
        else:
            return False
            # pnode.child[pos].keys = pnode.child[pos-1].key[-1] + pnode.child[pos].keys
    def merge(self,pnode,ppos,lpos,rpos):
        # print("MERGE ##-##- pnode : ",pnode, "ppos: ",ppos,"\t l,r pos : ",lpos,rpos)
        # print("MergingChild"," lpos : " , pnode.child[lpos]," Ppos : " , pnode.keys[ppos]," rpos : " , pnode.child[rpos])
        pnode.child[lpos].keys = pnode.child[lpos].keys + [pnode.keys[ppos]] + pnode.child[rpos].keys
        pnode.keys.pop(ppos)
        if pnode.child[lpos].child:
            # print("CHILD MERGING이 필요해",pnode.child[lpos].child, "<->",pnode.child[rpos].child)
            pnode.child[lpos].child += pnode.child[rpos].child
        pnode.child.pop(rpos)
            # pass
        pass




if __name__=="__main__":
    print("Start")
    # bt = BTree(3)
    # for i in range(1,50):
    #     bt.insert_node(bt.root,[i,i*10])
    