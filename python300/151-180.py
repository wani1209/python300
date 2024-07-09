#151
l = [3, -20, -3, 44]
for i in l:
    if i < 0:
        print(i)
        
#152
l = [3, 100, 23, 44]
for i in l:
    if i%3 == 0:
        print(i)
        
#153
l = [13, 21, 12, 14, 30, 18]
for i in l:
    if i%3==0 and i<20:
        print(i)
        
#154
l = ["I", "study", "python", "language", "!"]
for i in l:
    if len(i) >= 3:
        print(i)
        
#155
l = ["A", "b", "c", "D"]
for i in l:
    if i.isupper():
        print(i)
        
#156
l = ["A", "b", "c", "D"]
for i in l:
    if i.islower():
        print(i)
        
#157
l = ['dog', 'cat', 'parrot']
for i in l:
    print(i.capitalize())
    
#158
l = ['hello.py', 'ex01.py', 'intro.hwp']
for i in l:
    print(i.split('.')[0])
    
#159
l = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in l:
    if 'h'==i.split('.')[-1]:
        print(i)
        
#160
l = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in l:
    if i.split('.')[-1] in ['h','c']:
        print(i)

#161
for i in range(100):
    print(i)

#162
for i in range(2002,2051,4):
    print(i)
    
#163
for i in range(3,31,3):
    print(i)
    
#164
for i in range(99,-1,-1):
    print(i)

#165        rnage문은 정수형만 가능
for i in range(0,10,1):
    print(i/10)
    
#166
for i in range(1,10,1):
    print(f'3 x {i} = {3*i}')
    
#167
for i in range(1,10,2):
    print(f'3 x {i} = {3*i}')
    
#168
sum = 0
for i in range(1,11):
    sum += i
print(sum)

#169
sum = 0
for i in range(1,10,2):
    sum += i
print(sum)

#170
total = 1                   #곱하기이기 때문에 0이 아니라 1로 기본값을 두어야 함
for i in range(1,11):
    total *= i
print(total)

#171
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])
    
#172
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(i, price_list[i])
    
#173
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(len(price_list)-(i+1),price_list[i])
    
#174
price_list = [32100, 32150, 32000, 32500]
for i in range(1,4):
    print(100+(i-1)*10,price_list[i])
    
#175
my_list = ["가", "나", "다", "라"]
for i in range(3):
    print(my_list[i],my_list[i+1])
    
#176
my_list = ["가", "나", "다", "라", "마"]
for i in range(3):
    print(my_list[i],my_list[i+1],my_list[i+2])
    
#177
my_list = ["가", "나", "다", "라"]
for i in range(3,0,-1):
    print(my_list[i],my_list[i-1])
    
#178
my_list = [100, 200, 400, 800]
for i in range(len(my_list)-1):
    print(my_list[i+1]-my_list[i])
    
#179
my_list = [100, 200, 400, 800, 1000, 1300]
for i in range(len(my_list)-2):
    print((my_list[i]+my_list[i+1]+my_list[i+2])/3)
    
#180
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]
volatility = []
for i in range(len(low_prices)):
    volatility.append(high_prices[i]-low_prices[i])
print(volatility)