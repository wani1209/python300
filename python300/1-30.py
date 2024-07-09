#1
print('Hello World')

#2
print("Mary's cosmetics")               #print('Marry\'s cosmetics')

#3
print('신씨가 소리질렀다. \"도둑이야\"')

#4
#print('C:\Windows')                     #이거 왜 오류뜸?

#5
print("안녕하세요. \n만나서\t\t반갑습니다.") #\n 줄바꿈, \t 탭

#6
print("오늘은", "일요일")                 #오늘은 일요일(쉼표 공백)

#7
print('naver','kakao','sk','samsung',sep=';')

#8
print('naver','kakao','sk','samsung',sep='/')


#9
print('first',end=' ');print('second')

#10
print(5/3)

#11
samsung=50000
print(samsung*10)

#12
시가총액 = 2980000000000
현재가 = 50000
per = 15.79
print(시가총액, 현재가, per, type(시가총액),type(현재가),type(per))

#13
s='hello' ; t='python'
print(s,end='! ') ; print(t)            #print(s+"!",t)

#14
print(2+2*3)                            #8

#15
a='132'
print(type(a))                          #<class 'str'>

#16
num_str='720'
num_str=int(num_str)
print(type(num_str))

#17
num = 100
num = str(num)
print(type(num))

#18
f='15.79'
f=float(f)
print(type(f))

#19
year="2020"
print(int(year)-3) ; print(int(year)-2) ; print(int(year)-1)

#20
month = 48584
total = month*36
print(total)

#21
letters = 'python'
print(letters[0],letters[2])

#22
license_plate="24가 2210"
print(license_plate[4::])               #[-4:]

#23
string1='홀짝홀짝홀짝'
print(string1[0::2])

#24
string2='PYTHON'
print(string2[::-1])

#25     replace 메서드
phone_number = '010-1111-2222'
phone_number1 = phone_number.replace('-',' ')
print(phone_number1)

#26
phone_number2 = phone_number.replace('-','')
print(phone_number2)

#27     split 메서드
url = 'http://sharebook.kr'
url_split = url.split('.')
print(url_split[-1])

#28     문자열은 수정 불가능
#lang = 'python'
#lang[0] = 'P'
#print(lang)

#29
s='abcdfe2a354a32a'
s1=s.replace('a','A')
print(s1)

#30     replace 저장되지 않는 게 아니라 문자열이 수정이 불가한 자료형이므로 본 문자열 그대로 출력됨
s2='abcd'
s2.replace('b','B')
print(s2)                           #예상 출력 : abcd