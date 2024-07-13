#모듈
#241
import datetime
print(datetime.datetime.now())

#242
import datetime
print(type(datetime.datetime.now()))

#243
import datetime
now = datetime.datetime.now()
for i in range(5,0,-1):
    delta = datetime.timedelta(days=i)
    date = now - delta
    print(date)

#244
import datetime
now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

#245
import datetime
day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

#246
import time, datetime
while True:
    now = datetime.datetime.now()
    print(now)
    time.sleep(1)                                 #프로그램을 float초 만큼 일시정지하는 함수

#247
#import 모듈
#import 모듈 as 이름                               모듈 내의 함수를 호출할 때 모듈 이름 대신 새 이름으로 함수를 호출하겠다는 뜻
#from 모듈 import 함수명                           함수를 호출할 대 모듈 이름을 지정하지 않고, 바로 모듈 안의 함수를 호출할 수 있음
#from 모듈 import *                                모듈 안에 있는 못든 것(*)을 임포트하는 방식

#248
from os import getcwd
print(getcwd(),type(getcwd()))

#249
import os
os.rename("C:\Users\user\Desktop\defore.txt","C:\Users\user\Desktop\after.txt")

#250
import numpy
for i in numpy.arange(0,5,0.1):
    print(i)

#클래스
#251
#클래스 - 하나의 타입을 정의하는 방법, 데이터와 함수를 모아 정의할 수 있음, 클래스로 만들어진 결과물 = 객체

#252
class Human:
    pass


#253
class Human:
    pass
areum = Human()

#254
class Human:
    def __init__(self):
        print('응애응애')
areum = Human()

#255
class Human:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human('아름',25,'여자')

#256
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("아름", 25, "여자")
print(areum.age)

#257
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')
areum = Human("조아름", 25, "여자")
areum.who()

#258
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')
    def setInfo(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("불명", '미상', "모름")
areum.setInfo('아름',25,'여자')

#259
class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def __del__(self):
        print('나의 죽음을 알리지마라')
    def who(self):
        print(f'이름: {self.name}, 나이: {self.age}, 성별: {self.sex}')
    def setInfo(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = Human("조아름", 25, "여자")
del(areum)

#260
class OMG : 
    def print() :                   #print 메서드가 클래스로부터 호출될 때 암묵적으로 첫 번째 인자로 인스턴스(self)를 받지 않기 때문에 발생함. 따라서, 클래스의 메서드를 정의할 때 첫 번째 인자로 self를 추가해야 함
        print("Oh my god")
mystock = OMG()
mystock.print()

#261
class Stock:
    pass

#262
class Stock:
    def __init__(self,name,code):
        self.name = name
        self.code = code
삼성 = Stock("삼성전자", "005930")
print(삼성.name) ; print(삼성.code)

#263
class Stock:
    def __init__(self,name,code):
        self.name = name
        self.code = code
    def set_name(self,name):
        self.name = name
a = Stock(None, None)               #Stock.set_name(a,'삼성전자')
a.set_name("삼성전자")
print(a.name)

#264
class Stock:
    def __init__(self,name,code):
        self.name = name
        self.code = code
    def set_name(self,name):
        self.name = name
    def set_code(self,code):
        self.code = code
a = Stock(None,None)
a.set_code('005930')
print(a.code)

#265
class Stock:
    def __init__(self,name,code):
        self.name = name
        self.code = code
    def set_name(self,name):
        self.name = name
    def set_code(self,code):
        self.code = code
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
삼성 = Stock("삼성전자", "005930")
print(삼성.name)
print(삼성.code)
print(삼성.get_name())
print(삼성.get_code())

#266
class Stock:
    def __init__(self, name, code, per, pbr, yld):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.yld = yld

#267
삼성 = Stock('삼성전자','005930',15.79,1.33,2.83)

#268
class Stock:
    def __init__(self, name, code, per, pbr, yld):
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.yld = yld
    def set_per(self, per):
        self.per = per

    def set_pbr(self, pbr):
        self.pbr = pbr

    def set_dividend(self, yld):
        self.yld = yld

#269
삼성 = Stock('삼성전자','005930',15.79,1.33,2.83)
삼성.set_per(12.75)

#270
종목 = []
삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83)
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27)
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37)
종목.append(삼성)
종목.append(현대차)
종목.append(LG전자)
for i in 종목:
    print(i.code,i.per)                                 #i ->Stock 클래스의 객체를 바인딩하기 때문에