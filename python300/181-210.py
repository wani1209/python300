#181
apart = [[101,102],[201,202],[301,302]]

#182
stock = [['시가',100,200,300],['종가',80,210,330]]

#183
stock = {'시가':[100,200,300],'종가':[80,210,330]}

#184
stock = {'10/10':[80,110,70,90],'10/11':[210,230,190,200]}

#185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(f'{j}호')
        
#186
for i in range(-1,-len(apart)-1,-1):
    for j in range(len(apart[i])):
        print(f'{apart[i][j]}호')
# # 정답 코드
# for i in apart[::-1]:
#     for j in i:
#         print(f'{j}호')

#187
for i in apart[::-1]:
    for j in i[::-1]:
        print(f'{j}호')
        
#188
for i in apart:
    for j in i:
        print(f"{j}호")
        print('-----')
        
#189
for i in apart:
    for j in i:
        print(f'{j}호')
    print('-----')
    
#190
for i in apart:
    for j in i:
        print(f'{j}호')
print('-----')

#191
data = [
    [ 2000,  3050,  2050,  1980],
    [ 7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]
for i in data:
    for j in i:
        print(j*1.00014)
        
#192
for i in data:
    for j in i:
        print(j*1.00014)
    print('----')
    
#193
result = []
for i in data:
    for j in i:
        result.append(j*1.00014)
print(result)

#194
result = []
for i in data:
    sub = []
    for j in i:
        sub.append(j*1.00014)
    result.append(sub)
print(result)

#195
ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]]
for i in ohlc[1:]:                          #슬라이싱
    print(i[-1])
    
#196
for i in ohlc[1:]:
    if i[-1] > 150:
        print(i[-1])
        
#197
for i in ohlc[1:]:
    if i[-1] >= i[0]:
        print(i[-1])
        
#198
volatility = []
for i in ohlc[1:]:
    volatility.append(i[1]-i[2])
print(volatility)

#199
for i in ohlc[1:]:
    if i[-1] > i[0]:
        print(i[1]-i[2])
        
#200
sum = 0
for i in ohlc[1:]:
    sum += i[-1] - i[0]
print(sum)

#201
def print_coin():
    print('비트코인')
    
#202
print_coin()

#203
for i in range(100):
    print_coin()
    
#204
def print_coins():
    for i in range(100):
        print('비트코인')
        
#205
#hello()
#def hello():
#    print("Hi")                         #에러 발생 원인 : 함수가 정의되기 전에 호출됐기 때문에
    
#206
def message() :
    print("A")
    print("B")
message()
print("C")
message()                               #A\nB\nC\nA\nB

#207
print("A")
def message() :
    print("B")
print("C")
message()                               #A\nC\nB

#208
print("A")
def message1() :
    print("B")
print("C")
def message2() :
    print("D")
message1()
print("E")
message2()                              #A\nC\nB\nE\nD

#209
def message1():
    print("A")
def message2():
    print("B")
    message1()
message2()                              #B\nA

#210
def message1():
    print("A")
def message2():
    print("B")
def message3():
    for i in range (3) :
        message2()
        print("C")
    message1()
message3()                          #B\nC\nB\nC\nB\nc\nA