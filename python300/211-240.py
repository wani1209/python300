#211
def 함수(s) :
    print(s)
함수("안녕")
함수("Hi")                      #안녕\nHi

#212
def 함수(a, b) :
    print(a + b)
함수(3, 4)
함수(7, 8)                      #7\n15

#213
#def 함수(문자열) :
#    print(문자열)
#함수()                          #함수의 정의와 다르게 함수를 호출해서, 함수를 호출할 때 하나의 파라미터(매개변수)를 입력해야 함

#214
#def 함수(a, b) :
#    print(a + b)
#함수("안녕", 3)                 #정의된 함수는 같은 타입의 값을 입력 받아 덧셈 연산을 하도록 설계 되었는데, 입력 받은 두 개의 매개변수의 자료형이 다름

#215
def print_with_smile(s):
    print(f'{s} :D')
    
#216
print_with_smile('안녕하세요')

#217
def print_upper_price(num):
    print(num*1.3)
    
#218
def print_sum(a,b):
    print(a+b)
    
#219
def print_arithmetic_operation(a,b):
    print(f'{a} + {b} = {a+b}')
    print(f'{a} - {b} = {a-b}')
    print(f'{a} x {b} = {a*b}')
    print(f'{a} / {b} = {a/b}')
print_arithmetic_operation(3,4)

#220
def print_max(a,b,c):
    if a >= b and a >= c:
        print(a)
    elif b >= a and b >= c:
        print(b)
    else:
        print(c)
a,b,c = map(int,input('숫자입력 : ').split())           #map함수
print_max(a,b,c)

#221
def print_reverse(s):
    print(s[::-1])
print('python')

#222
def print_score(l):
    sum = 0
    for i in l:
        sum += i
    print(sum/len(l))                                   #print(snum(l)/len(l))
print_score ([1, 2, 3])

#223
def print_even(l):
    for i in l:
        if i%2 == 0:
            print(i)
print_even ([1, 3, 2, 10, 12, 11, 15])

#224
def print_keys(dic):
    for i in dic.keys():
        print(i)
print_keys ({"이름":"김말똥", "나이":30, "성별":0})

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key(dic,s):
    print(dic[s])
print_value_by_key  (my_dict, "10/26")

#226        답안 보고 풀음
def print_5xn(s):
    for i in range(int(len(s)/5)+1):
        print(s[i*5:i*5+5])
print_5xn("아이엠어보이유알어걸")

#227
def printmxn(s,num):
    for i in range(int(len(s)/num)+1):
        print(s[i*num:i*num+num])
printmxn("아이엠어보이유알어걸",3)

#228
def calc_monthly_salary(num):
    print(int(num/12))
calc_monthly_salary(12000000)

#229
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(a=100, b=200)                              #왼쪽: 100\n오른쪽: 200

#230        변수 바인딩
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)
my_print(b=100, a=200)                              #왼쪽: 200\n오른쪽: 100

#231        지역변수 전역변수
def n_plus_1 (n) :
   result = n + 1
n_plus_1(3)
print (result)                                        #오류 발생

#232
def make_url(s):
    return (f'www.{s}.com')
make_url("naver")

#233
def make_list(s):
    return list(s)
make_list("abcd")

#234
def pick_even(l):
    result = []
    for i in l:
        if i % 2 == 0:
            result.append(i)
    return result

#235
def convert_int(s):
    return int(s.replace(',',''))
convert_int("1,234,567")

#236
def 함수(num) :
    return num + 4
a = 함수(10)
b = 함수(a)
c = 함수(b)
print(c)                                            #22

#237
def 함수(num) :
    return num + 4
c = 함수(함수(함수(10)))
print(c)                                            #22

#238
def 함수1(num) :
    return num + 4
def 함수2(num) :
    return num * 10
a = 함수1(10)
c = 함수2(a)
print(c)                                            #140

#239
def 함수1(num) :
    return num + 4
def 함수2(num) :
    num = num + 2
    return 함수1(num)
c = 함수2(10)
print(c)                                            #16

#240
def 함수0(num) :
    return num * 2
def 함수1(num) :
    return 함수0(num + 2)
def 함수2(num) :
    num = num + 10
    return 함수1(num)
c = 함수2(2)
print(c)                                           #28