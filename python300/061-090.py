#61
price = ['20180728',100,130,140,150,160,170]
print(price[1::])

#62
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[0::2])                       #print(nums[::2])

#63
print(nums[1::2])

#64
print(nums[::-1])

#65
interest = ['삼성전자','LG전자','Naver']
print(interest[0],interest[2])

#66     join함수란? 리스트를 문자열로 합치는 함수 사용 예시 : '구분자'.join(리스트)
interest1 = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(' '.join(interest1))

#67
print('/'.join(interest1))

#68
print('\n'.join(interest1))

#69
string = "삼성전자/LG전자/Naver"
interest2 = string.split('/')
print(interest2)

#70
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()                         #data = sorted(data) / .sort() 와 sorted()의 차이점 : .sort는 리스트에 저장되지만 sorted()는 저장되지 않기 때문에 직접 할당해줘야 함
print(data)

#71
my_variable = ()

#72
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")

#73
nums1 = (1)
print(type(nums1))                  #튜플이 아니라 숫자면 숫자형으로 문자면 문자형으로 인식함
nums2 = (1,)
print(type(nums2))                  #하나의 데티어가 저장되는 경우 쉼표를 입력해야만 튜플로 인식

#74
#t = (1, 2, 3)
#t[0] = 'a'                         #오류 원인 : 튜플은 수정불가한 자료형임

#75
t = 1,2,3,4
print(type(t))                      #<class 'tuple'>    사용자 편의를 위해 괄호 없이도 작동

#76
t1 = ('a', 'b', 'c')                #튜플은 수정불가능하기 때문에 새로운 변수를 만들고 t라는 변수를 업데이트 해야 함
t1 = ('A', 'b', 'c')
print(t1)

#77
interest3 = ('삼성전자', 'LG전자', 'SK Hynix')
interest3 = list(interest3)
print(interest3)

#78
interest4 = ['삼성전자', 'LG전자', 'SK Hynix']
interest4 = tuple(interest4)
print(interest4)

#79
temp = ('apple', 'banana', 'cake')
a, b, c = temp
print(a, b, c)                      #예상 출력 : apple banana cake

#80
my_tuple = tuple(range(2,99,2))     #리스트도 같은 방식으로 생성 가능 my_list = list(range(2,99,2))
print(my_tuple)

#81     
#별표현식(start expression): 이를 사용하면 좌변과 우변의 변수 개수가 달라도 데이터 언패킹 가능
a,b,*c = (0,1,2,3,4,5)              #추가 용어 설명 : 언패킹 - 한 변수의 데이터를 각각의 변수로 반환하는 것
print(a,b,c)                        #my_list = [0] * 100 ; rint(my_list) 새로운 리스트가 생성되는 것이 아니라 리스트의 원소가 100개 생성됨
print(type(c))                      #a1,b1,*c1 = [0,1,2,3,4,5] ; print(a1,b1,c1,type(c1)) 리스토 같은 방식으로 별표현식을 사용할 수 있음. 또한, 별표현식을 사용한 변수의 자료형은 리스트임

scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score,a,a = scores           #a는 계속해서 업데이트 되기 때문에 마지막 저장된 데이터가 저장됨
print(valid_score,a)

#82
b,b,*valid_score1 = scores
print(valid_score1)

#83
c,*valid_score2,c = scores
print(valid_score2)

#84     딕셔너리 {key : value} 순서
temp = {}

#85
ice_cream = {'메로나':1000 , '폴라포':1200 , '빵빠레':1800}

#86
ice_cream['죠스바'] = 1200
ice_cream['월드콘'] = 1500
print(ice_cream)

#87
print(f'메로나 가격 : {ice_cream['메로나']}')

#88
ice_cream['메로나'] = 1300

#89
del ice_cream['메로나']             #ice_cream.pop('메로나')
print(ice_cream)

#90
#icecream = {'폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
#icecream['누가바']                 #key값에 누가바가 없기 때문에 오류가 남(딕셔너리에 없는 키를 인덱싱하면 오류 발생)