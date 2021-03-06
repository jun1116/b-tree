# B-Tree order M With Python 

## Start
### Python Version : 3.8.10

git clone 을 통해 directory까지 다운받아 사용하면 편합니다. 
```
git clone https://github.com/jun1116/b-tree.git
cd b-tree
```

### 환경세팅
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```
___
## 1. 시작 및 M 사이즈 설정

시작은 main.py를 실행하면서 시작합니다. 
실행 후 B-Tree의 Order를 입력하면 되며, 입력하지 않거나 3보다 작은 숫자 입력시 Default 는 5 입니다.  

대량의 데이터의 경우 M이 너무 크다고 속도가 빠른것이 아닙니다.   
적절한 M이 중요하며 약 100만건의 데이터에서 M의 차이에 따라 연산의 속도가 다릅니다.  

|M|Row Count|Insertion Time|
|---|---|---|
|10000|1,000,000|26 min|
|1000|1,000,000|5.5 min|
|500|1,000,000|3 min|

약 100만건의 Input Data에 대하여 M=10000 일때 insertion에 26분이 소요되며  
M=500일 경우 약 3분만에 Insertion 을 완료하였습니다.  
Node 내부의 Key의 대소비교에 대하여 순차적으로 진행하는 특성상 M이 클수록 순차비교에 소모되는 시간이 크기 때문이라 볼 수 있습니다.  

<!-- ### csv 라이브러리 사용
```python
python3 main.py
Enter the M order of B-Tree (default is 5) {Input Order M}
``` -->

### pandas,tqdm 라이브러리 사용
```python
python3 main_pandas.py
Enter the M order of B-Tree (default is 5) {Input Order M}
```
___

## 2. Insertion -> Search -> Compare
```python
Press number you want to start and [ENTER]
Press number you want to start and [ENTER]
1. insertion 	2.deletion 	3.quit
1
Write the Input file name With out extension
(ex. input, input3, input_compare, input3_compare, input22 )
input  

Insertion Start  

100%|█████████████████████████████████████████████████████████| 1000000/1000000 [00:31<00:00, 31957.53it/s]  

Search Start  

100%|█████████████████████████████████████████████████████████| 1000000/1000000 [00:19<00:00, 50348.90it/s]  

Compare Start  

Data Count = 1000000 , Correct : 1000000 , Incorrect : 0 , True Percent : 100.0%
```
어느연산을 수행할 지 선택하면 되며, (1,2,3의 옵션) 위 과정은 반복됩니다.   
data 라는 폴더안에 존재하는 파일명(확장자명 제외) 을 입력한 경우 해당 옵션에 맞는 기능으로 동작합니다.   

Insertion의 경우 input 파일을 입력하면 B-Tree에 해당 파일의 key value 가 입력되며,   
이후 search, compare 과정을 위해 입력한 input파일에서 저장된 키들에 대하여 모든 key, value B-Tree에서 Search합니다.   
해당 Search의 결과로 input 파일명 뒤에 {}_compare.csv 로 파일이 저장되고, 

이후 compare과정을 진행하며, 이 과정에서 입력한 input파일과 Search를 통해 생성된 compare 파일의 비교를 진행하여 결과를 출력합니다.   

출력형식 : ex. Data Count = 10 , Correct : 10 , Incorrect : 0 , True Percent : 1.0
Data Count : 총 데이터 개수  
Correct : 맞게 Search되어 key, value가 정확히 존재하는 개수  
Incorrect : key,value가 틀린 개수  
True Percent : 100 * Correct / Data Count  

## 3. Deletion
** 2번 과정에서의 Insertion 을 마친 이후 진행해야합니다. **
```python
1. insertion 	2.deletion 	3.quit  
2  
Write the Delete Operation file name With out extension  
(ex. delete, delete2 )  
delete

Deletion Start  

100%|███████████████████████████████████████████████████████████| 500000/500000 [00:10<00:00, 45684.10it/s]  

Search Start  

100%|█████████████████████████████████████████████████████████| 1000000/1000000 [00:22<00:00, 45012.02it/s]  

Compare Start  

Data Count = 2000000 , Correct : 2000000 , Incorrect : 0 , True Percent : 100.0%  
```

1. Insertion 이후 진행이 가능하며, 입력한 delete.csv 와 같은 파일에 대하여 delete operation을 진행합니다.  

2. Insertion에서 사용되었던 전체 키에대하여 Search를 진행하며, 이 때 찾아지지 않는 값은 "NF" 로 기록하고, delete_saved.csv 와 같은 형식으로 저장합니다.  

3. 마지막으로 compare를 진행하며, 2번과정엥서 저장한 delete_saved.csv 와 같은 파일과 data폴더에 존재하는 delete_compare.csv 와 같은 파일에 대하여 비교를 진행합니다. 

최종적으로 Insertion과 같이 해당 데이터에 대한 Count, Correct, Incorrect, True Percent를 출력합니다. 


