# 제어문(if, while, for)
---

"집을 지을때 나무, 돌, 시멘트 등은 재료가, 철근은 집의 뼈대가 된다. 제어문은 집의 뼈대를 이루는 철근"

참고 점프 투 파이썬(https://wikidocs.net/19)

제어문은 알고리즘의 꽃, 이거만 잘하면 다 잘한다


---


### 1. if문
---
"돈이 있으면 택시를 타고, 돈이 없으면 걸어간다"

```python
money = 10000
if money > 1000000 :
    print("택시를 타고 가라"
    
else : 
    print("걸어 가라")
     
```

들여쓰기가 핵심
```python
if 조건문:
    수행할 문장1
수행할 문장2
    수행할 문장3
```

```python
if 조건문:
    수행할 문장1
    수행할 문장2
    수행할 문장3
```

```python    
If <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
...
else:
   <수행할 문장1>
   <수행할 문장2>
```

### (1.+) if문 조건절(연산자)
---
|비교연산자|설명|
|:--- | ---: |
|x<y|x가 y보다 작다|
|x<=y|x가 y보다 작거나 같다|
|x==y|x와 y가 같다|
|x!=y|x와 y가 같지 않다|

---
and, or, not

```python
money =2000
card = True
if money >= 3000 or card :
  print("택시를 타고가라")
else :
  print("걸어가라")
```


---


### 2. while문
---
"기본 구문"
```python
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
```

```python
treeHit = 0
while treeHit < 10:
     treeHit = treeHit +1
     print("나무를 %d번 찍었습니다." % treeHit)
     if treeHit == 10:
         print("나무 넘어갑니다.")
```

"break와 continue 차이"

```python

coffee = 10
while True:
    money = int(input("돈을 넣어 주세요: "))
    if money == 300:
        print("커피를 줍니다.")
        coffee = coffee -1
    elif money > 300:
        print("거스름돈 %d를 주고 커피를 줍니다." % (money -300))
        coffee = coffee -1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
        print("남은 커피의 양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("커피가 다 떨어졌습니다. 판매를 중지 합니다.")
        break
```

```python
while a < 10:
     a = a + 1
     if a % 2 == 0: continue
     print(a)
```


---


### 3. for문
---
"기본 구문"
```python
for 변수 in 리스트(또는 튜플, 문자열):
    수행할 문장1
    수행할 문장2
```

"전형적 for문 예시"
```python
champion_list = ['garen','lux','diana']
for champion in champion_list:
    print(champion)
```


"특수형태 for문 예시"
```python
hitter_list = ['lee_jb','lee_yk','lee_sy']
for i,hitter in enumerate(hitter_list):
    print(i,"번 타자",hitter)
```

```python
lolchess_dic = {'Dragonsoul':'Tristana','Fortune':'Annie','Mage':'Brand'}
for key,value in lolchess_dic.items():
    print(key,value)
```
