#31
a = "3" ; b = "4"
print(a+b)              #34 새로운 문자열 생성

#32
print("Hi"*3)          #HiHiHi 문자열의 반복

#33
print("-"*80)

#34
t1="python"
t2="java"
print((t1+' '+t2+' ')*3)

#35
name1= '김민수' ; age1 = 10
name2= '이철희' ; age2 = 13
print('이름 : %s 나이 : %d' %(name1,age1))
print('이름 : %s 나이 : %d' %(name2,age2))

#36
print('이름 : {} 나이 : {}'.format(name1,age1))
print('이름 : {} 나이 : {}'.format(name2,age2))

#37
print(f'이름 : {name1} 나이 : {age1}')
print(f'이름 : {name2} 나이 : {age2}')

#38
num="5,969,782,550"
num=int(num.replace(',',''))
print(num,type(num))

#39
s1="2020/03(E) (IFRS연결)"
print(s1[:7:])

#40     strip()메소드 : 문자열의 사작과 끝에 주어진 문자를 제거하는 함수(보통 괄호가 비어있으면 시작과 끝의 공백을 제거)
data="    삼성전자    "
data=data.strip()
print(data)

#41
ticker1 = 'btc_krw'
ticker1 = ticker1.upper()
print(ticker1)

#42
ticker2 = 'BTC_KRW'
ticker2 = ticker2.lower()
print(ticker2)

#43     capitalize 메소드 - 문자열의 첫 글자는 대문자로 나머지는 소문자로 변환해주는 메소드
str1 = 'helLo'
str1 = str1.capitalize()
print(str1)

#44     endswith 메소드 - 문자열이 지정 문자열로 끝나는지 확인하는 메소드(<->startswith)
file1_name = '보고서.xlsx'
print(file1_name.endswith('xlsx'))

#45
print(file1_name.endswith('xlsx'or'xls'))        #file_name.endswith('xlsx','xls')도 가능

#46
file2_name = '2020_보고서.xlsx'
print(file2_name.startswith('2020'))

#47     split('구분자',분할횟수) 메소드 괄호 안에 아무것도 없으면 띄어쓰기를 기준으로 분할
a = 'hello world'
a = a.split()
print(a)

#48
ticker3 = 'btc_krw'
ticker3 = ticker3.split('_')
print(ticker3)

#49
date = '2020-05-01'
date = date.split('-')
print(date)

#50     rstrip() 오른쪽 공백 제거, lstrip() 왼쪽 공백 제거
data1 = '039490    '
data1 = data1.rstrip()
print(data1)

#50-1 추가 만약 괄호 안에 인자가 있다면 그 인자의 모든 조합을 제거함
print('apple'.lstrip('ap'))     #출력값 le

#51
movie_rank = ['닥터 스트레인지','스플릿','럭키']

#52
movie_rank.append('배트맨')

#53
movie_rank.insert(1,'슈퍼맨')

#54
movie_rank.remove('럭키')

#55     인덱스 값을 사용하기 때문에 남은 원소들의 순서를 고려해야 함
del movie_rank[2]
del movie_rank[2]
print(movie_rank)

#56
lang1 = ['C','C++','JAVA']
lang2 = ['Python','Go','C#']
langs = lang1 + lang2
print(langs)

#57
nums = [1,2,3,4,5,6,7]
print(f'min : {min(nums)}')
print(f'max : {max(nums)}')

#58
numss = [1,2,3,4,5]
print(sum(numss))

#59
cook =['피자','김밥','만두','양념치킨','족발','피자','김치만두','쫄면','소시지','라면','팥빙수','김치전']
print(len(cook))

#60
print(sum(numss)/len(numss))