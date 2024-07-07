#121
char = input('문자 입력 : ')
if char.islower():
    print(char.upper())
else:
    print(char.lower())

#122
score = int(input('점수 : '))
if score >= 81 and score <= 100:
    print('A')
elif score >= 61 and score <= 80:
    print('B')
elif score >= 41 and score <= 60:
    print('C')
elif score >= 21 and score <= 40:
    print('D')
elif score >= 0 and score <= 21:
    print('E')
    
#123
money = input('입력 : ')
money = money.split()
money[0] = int(money[0])
if money[1] == '달러':
    print(f'{money[0]*1167}원')
elif money[1] == '엔':
    print(f'{money[0]*1.096}원')
elif money[1] == '유로':
    print(f'{money[0]*1268}원')
elif money[1] == '위안':
    print(f'{money[0]*171}원')

#정답 코드 딕셔너리/언패킹 
환율 = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
user = input("입력: ")
num, currency = user.split()
print(float(num) * 환율[currency], "원")

#124
num1 = int(input('num1 : '))
num2 = int(input('num2 : '))
num3 = int(input('num3 : '))
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num3:
    num1, num3 = num3,num1
print(num3)

#125
carrier = {'011':'SKT','016':'KT','019':'LGU','010':'알수없음'}
user = input('전화번호 : ')
phone = user.split('-')[0]
print(f'당신은 {carrier[phone]} 사용자입니다.')

#126
post = input('우편번호 : ')
post_num = int(post[2])
if 0 <= post_num <= 2:
    print('강북구')
elif 3 <= post_num <= 5:
    print('도봉구')
else:
    print('노원구')

#127
id = input('주민등록번호 : ')
id_gender = id[7]
if id_gender in ['1','3']:
    print('남자')
else:
    print('여자')

#128
id_place = int(id[8:10])
if 0 <= id_place <= 8:
    print('서울입니다.')
else:
    print('서울이 아닙니다')
    
#129
count1 = int(id[0])*2 + int(id[1])*3 + int(id[2])*4 + int(id[3])*5 + int(id[4])*6 + int(id[5])*7 + int(id[7])*8 + int(id[8])*9 + int(id[9])*2 + int(id[10])*3 + int(id[11])*4 + int(id[12])*5
count2 = 11 - (count1%11)
if count2 == int(id[-1]):
    print('유요한 주민등록번호입니다.')
else:
    print('유효하지 않는 주민등록번호입니다.')
    
#130
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
fluctuation_price = float(bct['max_price']) - float(bct['min_price'])
opening_price = float(bct['opening_price'])
max_price = float(bct['max_price'])
if (opening_price + fluctuation_price) > max_price:
    print('상승장')
else:
    print('하락장')

#131
fruit = ['사과','귤','수박']
for i in fruit:
    print(i)                    #사과\n귤\n수박

#132
for i in fruit:
    print('#####')              ######\n#####\n#####
    
#133
for i in ["A", "B", "C"]:
  print(i)
#동일한 동작
i = "A"
print(i)
i = "B"
print(i)
i = "C"
print(i)


#134
for 변수 in ["A", "B", "C"]:
  print("출력:", 변수)
#동일한 동작
변수 = "A"
print("출력:", 변수)
변수 = "B"
print("출력:", 변수)
변수 = "C"
print("출력:", 변수)


#135
for 변수 in ["A", "B", "C"]:
  b = 변수.lower()
  print("변환:", b)
#동일한 동작
변수 = "A"
b = 변수.lower()
print("변환:", b)
변수 = "B"
b = 변수.lower()
print("변환:", b)
변수 = "C"
b = 변수.lower()
print("변환:", b)

#136
변수 = 10
print(변수)
변수 = 20
print(변수)
변수 = 30
print(변수)
#for문 작성
l = [10, 20, 30]
for 변수 in l:
  print(변수)

#137
print(10)
print(20)
print(30)
#for문 작성
for i in range(10,31,10):
  print(i)
  
#138
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")
#for문 작성
for i in range(10,31,10):
  print(i)
  print("-------")

#139
print("++++")
print(10)
print(20)
print(30)
#for문 작성
print("++++")
for i in range(10,31,10):
  print(i)
  
#140
print("-------")
print("-------")
print("-------")
print("-------")
#for문 작성
for i in range(4):
  print("-------")

#141
list = [100, 200, 300]
for i in list:
  print(i+10)

#142
list = ["김밥", "라면", "튀김"]
for i in list:
  print(f'오늘의 메뉴: {i}')

#143
list = ["SK하이닉스", "삼성전자", "LG전자"]
for i in list:
  print(len(i))
  
#144
list = ['dog', 'cat', 'parrot']
for i in list:
  print(i,len(i))

#145
for i in list:
  print(i[0])
  
#146
list = [1, 2, 3]
for i in list:
  print(f'3 x {i}')
  
#147
for i in list:
  print(f'3 x {i} = {3*i}')
  
#148
list = ["가", "나", "다", "라"]
for i in list[1:]:              #슬라이싱 활용하기
  print(i)

#149
for i in list[::2]:
  print(i)
  
#150
for i in list[::-1]:
  print(i)