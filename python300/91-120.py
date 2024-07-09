#91
inventory = {'메로나':[300,20],'비비빅':[400,3],'죠스바':[250,100]}

#92
print(f'{inventory['메로나'][0]}원')

#93
print(f'{inventory["메로나"][1]}개')

#94
inventory['월드콘'] = [500,7]
print(inventory)

#95
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
icecream_key = list(icecream.keys())
print(icecream_key)

#96
icecream_value = list(icecream.values())
print(icecream_value)

#97
print(sum(icecream_value))

#98     update 메소드
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

#99     dictionary는 ditc()와 {}로 최초 정의
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
fruit = dict(zip(keys,vals))
print(fruit)

#100        zip함수 순회 가능한 객체를 인자로 받고 각 자료형의 각각의 요소를 나눈 후 인덱스끼리 잘라서 리스트로 변환
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date,close_price))
print(close_table)

#101
#'bool'

#102
print(3==5)                     #False

#103
print(3<5)                      #True

#104
x = 4
print(1<x<5)                    #True

#105
print((3==3)and(4!=3))          #True

#106
#print(3=>4)                    #틀린 연산자 >= 이게 맞는 연산자

#107
if 4<3:
    print('Hello World')        #아무것도 출력되지 않음
    
#108
if 4<3:
    print('Hello World')
else:
    print('Hi, there.')         #예상 출력 : Hi, there.

#109
if True:
    print('1')
    print('2')
else:
    print('3')
print('4')                      #예상 출력 : 1 \n 2 \n 4

#110
if True:
    if False:
        print('1')
        print('2')
    else:
        print('3')
else:
    print('4')
print('5')                  #예상 출력 : 3 \n 5

#111
print(input('입력 : ')*2)

#112
num = int(input('숫자를 입력하세요 : '))
print(num+10)

#113
3
num1 = int(input('짝홀 판별 : '))
if num1 % 2 == 0:
    print('짝수')
else:
    print('홀수')
    
#114
num2 = 20 + int(input('225 초과 : '))
if num2 <= 225:
    print(num2)
else:
    print(225)

#115
num3 = int(input('입력값 : ')) - 20
if num3 <0:
    print(0)
elif num3 > 225:
    print(225)
else:
    print(num3)
    
#116
time = input('현재 시간 : ')
if time.endswith('00'):
    print('정각입니다')
else:
    print('정각이 아닙니다.')
    
#117
fruit1 = ["사과", "포도", "홍시"]
answer = input('가장 좋아하는 과일은? ')
if answer in fruit1:
    print('정답입니다')
else:
    print('오답입니다')
    
#118
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input('종목명 :')
if user in warn_investment_list:
    print('투자 경고 종목입니다')
else:
    print('투자 경고 종목이 아닙니다')
    
#119
fruit2 = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
season = input('가장 좋아하는 계절은 : ')
if season in fruit2.keys():                 #if season in fruit2: 만 써도 됨
    print('정답입니다')
else:
    print('오답입니다')
    
#120
fruit3 = input('가장 좋아하는 과일은 : ')
if fruit3 in fruit2.values():
    print('정답입니다')
else:
    print('오답입니다')