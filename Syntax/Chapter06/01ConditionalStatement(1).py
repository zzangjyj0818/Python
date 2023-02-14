# conditional statement

'''
if True:
    print("True")
else:
    print("False")
'''
# if문 사용 후, if 문 안에 코드를 작성할때
# 들여쓰기는 필수
# if의 조건을 충족하지 못하는 경우, else문 실행

'''
if 4>3:
    print("a")
else:
    print("b")
'''


# val = input("Input the Value : ") 는 문자열로 값이 입력됨
# 결론 : input은 입력 값을 모두 string으로 처리
# 따라서, 아래와 같이 형 변환을 해줘야함
val = int(input("Input the Value : "))

'''
if val > 10:
    print("a")
else:
    print("b")
'''

val = input("Input the Value : ")
val = val.upper()
if val == "INFP":
    print("INFP")
else:
    print("nothing")
