#271
import random
class Account :
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        num1 = str(random.randint(0,999)).zfill(3)
        num2 = str(random.randint(0,99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.account_num = num1 + '-' + num2 + '-' + num3
kim = Account('김민수',100)
print(kim.name)
print(kim.balance)
print(kim.bank)
print(kim.account_num)

#272
import random
class Account :
    account_count = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        num1 = str(random.randint(0,999)).zfill(3)
        num2 = str(random.randint(0,99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.account_num = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
kim = Account('김민수',100)
print(Account.account_count)
lee = Account('이민수',100)
print(Account.account_count)

#273    클래스 메소드
import random
class Account :
    account_count = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        num1 = str(random.randint(0,999)).zfill(3)
        num2 = str(random.randint(0,99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.account_num = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
    def get_account_num(cls):
        print(cls.account_count)
kim = Account('김민수',100)
lee = Account('이민수',100)
kim.get_account_num()

#274
import random
class Account :
    account_count = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        num1 = str(random.randint(0,999)).zfill(3)
        num2 = str(random.randint(0,99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.account_num = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
    def get_account_num(cls):
        print(cls.account_count)
    def deposit(self,num):
        if num >= 1:
            self.balance += num

#275
import random
class Account :
    account_count = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        num1 = str(random.randint(0,999)).zfill(3)
        num2 = str(random.randint(0,99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.account_num = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
    def get_account_num(cls):
        print(cls.account_count)
    def deposit(self, num):
        if num >= 1:
            self.balance += num
    def withdraw(self,num):
        if num <= self.balance:
            self.balance -= num
k = Account('kim',100)
k.deposit(100)
k.withdraw(90)
print(k.balance)

#276
import random
class Account :
    account_count = 0
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        num1 = str(random.randint(0,999)).zfill(3)
        num2 = str(random.randint(0,99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.account_num = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
    def get_account_num(cls):
        print(cls.account_count)
    def deposit(self, num):
        if num >= 1:
            self.balance += num
    def withdraw(self,num):
        if num <= self.balance:
            self.balance -= num
    def dispay_info(self):
        print(f'은행이름 : {self.bank}')
        print(f'예금주 : {self.name}')
        print(f'계좌번호 : {self.account_num}')
        print(f'잔고 : {self.balance:,}')
p = Account('파이썬',10000)
p.display_info()

#277
import random
class Account :
    account_count = 0
    def __init__(self,name,balance):
        self.deposit_count = 0
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        num1 = str(random.randint(0,999)).zfill(3)
        num2 = str(random.randint(0,99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.account_num = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
    def get_account_num(cls):
        print(cls.account_count)
    def deposit(self, num):
        if num >= 1:
            self.balance += num
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01        
    def withdraw(self,num):
        if num <= self.balance:
            self.balance -= num
    def display_info(self):
        print(f'은행이름 : {self.bank}')
        print(f'예금주 : {self.name}')
        print(f'계좌번호 : {self.account_num}')
        print(f'잔고 : {self.balance:,}')
p = Account('python',10000)
for _ in range(3):
    p.deposit(10000)
for _ in range(2):
    p.deposit(5000)
print(p.balance)

#278
data = []
k = Account('KIM',1000000)
l = Account('LEE',1000)
p = Account('PARK',10000)
data.append(k)
data.append(l)
data.append(p)
print(data)

#279
for i in data:
    if i.balance >= 1000000:
        i.display_info()

#280
import random
class Account :
    account_count = 0
    def __init__(self,name,balance):
        self.deposit_count = 0
        self.deposit_log = []
        self.withdraw_log = []
        self.name = name
        self.balance = balance
        self.bank = 'SC은행'
        num1 = str(random.randint(0,999)).zfill(3)
        num2 = str(random.randint(0,99)).zfill(2)
        num3 = str(random.randint(0,999999)).zfill(6)
        self.account_num = num1 + '-' + num2 + '-' + num3
        Account.account_count += 1
    def get_account_num(cls):
        print(cls.account_count)
    def deposit(self, num):
        if num >= 1:
            self.deposit_log.append(num)
            self.balance += num
            self.deposit_count += 1
            if self.deposit_count % 5 == 0:
                self.balance = self.balance * 1.01        
    def withdraw(self,num):
        if num <= self.balance:
            self.withdraw_log.append(num)
            self.balance -= num
    def display_info(self):
        print(f'은행이름 : {self.bank}')
        print(f'예금주 : {self.name}')
        print(f'계좌번호 : {self.account_num}')
        print(f'잔고 : {self.balance:,}')
    def withdraw_history(self):
        for amount in self.withdraw_log:
            print(amount)
    def deposit_history(self):
        for amount in self.deposit_log:
            print(amount)
k = Account("Kim", 1000)
k.deposit(100)
k.deposit(200)
k.deposit(300)
k.deposit_history()
k.withdraw(100)
k.withdraw(200)
k.withdraw_history()

#281
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
car = 차(2,1000)
print(car.바퀴)
print(car.가격)

#282    클래스 상속
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
class 자전차(차):
    pass

#283
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
class 자전차(차):
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
        
bicycle = 자전차(2,100)
print(bicycle.가격)

#284
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계
bicycle = 자전차(2,100,'시마노')
print(bicycle.구동계)
print(bicycle.바퀴)

#285
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
        
class 자동차(차):
    def __init__(self, 바퀴, 가격):
        super().__init__(바퀴, 가격)
    def 정보(self):
        print(f'바퀴수 {self.바퀴}')
        print(f'가격 {self.가격}')
        
car = 자동차(4,1000)
print(car.정보())

#286
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    def 정보(self):
        print(f'바퀴수 {self.바퀴}')
        print(f'가격 {self.가격}')
        
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계
        
bicycle = 자전차(2, 100, "시마노")
print(bicycle.정보())

#287
class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격
    def 정보(self):
        print(f'바퀴수 {self.바퀴}')
        print(f'가격 {self.가격}')
        
class 자전차(차):
    def __init__(self, 바퀴, 가격, 구동계):
        super().__init__(바퀴, 가격)
        self.구동계 = 구동계
    def 정보(self):
        super().정보()
        print(f'구동계 {self.구동계}')
        
bicycle = 자전차(2, 100, "시마노")
print(bicycle.정보())

#288
class 부모:
  def 호출(self):
    print("부모호출")

class 자식(부모):
  def 호출(self):
    print("자식호출")
나 = 자식()
print(나.호출())

# 예상 출력
# 자식호출

#289
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
나 = 자식()

# 예상 출력
# 자식생성

#290
class 부모:
  def __init__(self):
    print("부모생성")

class 자식(부모):
  def __init__(self):
    print("자식생성")
    super().__init__()

나 = 자식()

# 예상 출력
# 자식생성
# 부모생성

#291
f = open(r'D:\알고리즘 스터디\python300\매수종목1.txt', mode = 'wt', encoding='utf-8')
f.write('005930\n')
f.write('005380\n')
f.write('035420')
f.close()

#292
f = open(r'D:\알고리즘 스터디\python300\매수종목2.txt',mode='wt',encoding='utf-8')
f.write('005930 삼성전자\n')
f.write('005380 현대차\n')
f.write('035420 NAVER\n')
f.close()

#293
import csv

f = open(r'D:\알고리즘 스터디\python300\매수종목.csv',mode='wt',encoding='cp949',newline='')
writer = csv.writer(f)
writer.writerow(['NAME','CODE','PER'])
csv.writer(f).writerow(['SAMSUNG','005930',15.59])
writer.writerow(['NAVER','035420',55.82])
f.close()

#294
f = open(r'D:\알고리즘 스터디\python300\매수종목1.txt', encoding='utf-8')
codes = []
for line in f.readlines():
    codes.append(line.strip())
print(codes)
f.close()

#295
f = open(r'D:\알고리즘 스터디\python300\매수종목2.txt', encoding='utf-8')
data = {}
for line in f.readlines():
    line = line.strip()
    k, v = line.split()
    data[k] = v
print(data)
f.close()

#296
per = ["10.31","", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
        
#297
l = []
for i in per:
    try:
        l.append(i)
    except:
        l.append(0)

#298
try:
    a, b = map(int,input().split())
    print(a/b)
except ZeroDivisionError:
    print('0으로 나누면 안되요')
    
#299
data = [1,2,3]
for i in range(5):
    try:
        print(data[i])
    except IndexError as e:
        print(e)
        
#300
per = ["10.31", "", "8.00"]

for i in per:
    try:
        print(float(i))
    except:
        print(0)
    else:
        print('clean data')
    finally:
        print('변환 완료')