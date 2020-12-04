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

>>> a = 3
>>> b = 4
>>> a + b
7
>>> a * b
12
>>> a / b
0.75

```
### 2. 문자열
---

```python
'Python is fun'
'Mother's favorite singer is blackpink'
##indexing
>>> a = "Life is too short, You need Python"
>>> a[0]
'L'
>>> a[12]
's'
>>> a[-1]
'n'
>>> a[0:5]
'Life '
##format
>>> "I have %s apples" % 3
'I have 3 apples'

>>> name = 'BLACKPINK'
>>> first_music = 'BOOMBAYAH' 
>>> f'가수 이름은 {name}입니다. 데뷔곡은 {first_music}입니다.'
가수 이름은 BLACKPINK입니다. 데뷔곡은 BOOMBAYAH입니다.

##func
>>> ",".join(['a', 'b', 'c', 'd'])
'a,b,c,d'

>>> a = " hi "
>>> a.strip()
'hi'

```
### 3. 리스트
---
```python
>>> a = []
>>> b = [1, 2, 3]
>>> c = ['sana', 'mina', 'nayun', 'dahyun']
>>> d = [1, 2, 'Life', 'is']
>>> e = [1, 2, ['Life', 'is']]
```
### 4. 튜플
---

### 5. 딕셔너리
---

### 6. 집합
---

### 7. 불
---

### 8. 변수
---
