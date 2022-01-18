# B-Tree order M With Python 

## Start
git clone 을 통해 directory까지 다운받아 사용하면 편합니다. 
```
git clone https://github.com/jun1116/b-tree.git
cd b-tree
```

시작은 main.py를 실행하면서 시작합니다. 
실행 후 B-Tree의 Order를 입력하면 되며, 입력하지 않거나 3보다 작은 숫자 입력시 Default 는 5 입니다.
```python
python3 main.py
Enter the M order of B-Tree (default is 5) {Input Order M}
```

### 1. Insertion -> Search -> Compare
```python
Press number you want to start and [ENTER]
1. insertion    2.deletion      3.quit 
1
Write the Input file name With out extension 
(ex. input, input22 )
input
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
