# 파이썬의 기초
---

"어떤 프로그래밍 언어든 그 언어의 자료형을 알고 이해하면 이미 그 언어의 절반을 터득한 것이나 다름없다."
그럴 싸한 말로 보이지만 사실 처음 언어를 접하는 입장에서는 무슨소리인가 싶다.
하지만 나중에 프로그래밍으로 일을 하다보면 기본이 더욱 중요해 지기에 노잼이지만 그래도 알아야한다. ㅠㅠ

참고 점프 투 파이썬(https://wikidocs.net/12)
---


### 1. 숫자형
---
정수형(int)과 실수형(float)

```python
a = 123
a = -789
a = 0
b = 1.2

a = 3
b = 4
a + b
>>> 7
a * b
>>> 12
a / b
>>> 0.75

```
### 2. 문자열
---
문자열 기본
```python
'Python is fun'
'Mother's favorite singer is blackpink'
##indexing
a = "Life is too short, You need Python"
a[0]
>>> 'L'
a[12]
>>> 's'
a[-1]
>>> 'n'
a[0:5]
>>> 'Life '
```

문자열 포맷
```python
"I have %s apples" % 3
>>> 'I have 3 apples'

name = 'BLACKPINK'
first_music = 'BOOMBAYAH' 
f'가수 이름은 {name}입니다. 데뷔곡은 {first_music}입니다.'
>>> 가수 이름은 BLACKPINK입니다. 데뷔곡은 BOOMBAYAH입니다.
```

문자열 함수
```python

###join
",".join(['a', 'b', 'c', 'd'])
>>> 'a,b,c,d'

###strip
a = " hi "
a.strip()
>>> 'hi'

###find
a = "Faker is the best player"
a.find('b')
>>> 14

###split
a = "Life is too short"
a.split()
>>> ['Life', 'is', 'too', 'short']

b = "top:jungle:mid:bottom:sup"
b.split(':')
>>> ['top', 'bjungle, 'mid', 'bottom',sup]

```
### 3. 리스트
---
리스트 예시
```python
>>> a = []
>>> b = [1, 2, 3]
>>> c = ['sana', 'mina', 'nayun', 'dahyun']
>>> d = [1, 2, 'Life', 'is']
>>> e = [1, 2, ['Life', 'is']]
```
---
리스트 인덱싱/슬라이싱
```python
c[0]
>>> sana
e[2][0]
>>> Life
c[0:2]
>>> ['sana', 'mina', 'nayun']
c[-1]
>>> dahyun
```
---
리스트 연산
```python
a = [삼성전자, sk하이닉스]
b = [네이버, 카카오]
a + b ### a.extend(b)
>> [삼성전자, sk하이닉스, 네이버, 카카오]

###잦은 오류### 
1 + '삼성전자'
unsupported operand type(s) for +: 'int' and 'str'
>> '1' + '삼성전자'

###리스트 길이
len(a+b)
>> 4
```

---
리스트 함수
```python
### append

favorit_food = ['hamburger', 'pizza', 'cola']
favorit_food.append('sushi')
favorit_food
>> ['hamburger', 'pizza', 'cola','sushi']

### sort
a = [1,4,3,2]
a.sort()
a
>> [1, 2, 3, 4]
### etc
reverse, index, insert, revmove , pop(), count
```


### 4. 튜플
---
튜플(tuple)은 몇 가지 점을 제외하곤 리스트와 거의 비슷하며 리스트와 다른 점은 다음과 같다.

리스트는 [ ]으로 둘러싸지만 튜플은 ( )으로 둘러싼다.
리스트는 그 값의 생성, 삭제, 수정이 가능하지만 튜플은 그 값을 바꿀 수 없다.
함수에서 중요 
ex) 
  def plus_(a,b) :
    return = a+b
>>> plus(3) >> error    
---

### 5. 딕셔너리
---



### 6. 집합
---

### 7. 불
---

### 8. 변수
---
