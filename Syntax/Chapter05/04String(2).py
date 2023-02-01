score = "점수:90"
print(score)

# removeprefix("문자열") -> 앞쪽의 특정 문자열을 지우고 싶을때 선언
print(score.removeprefix("점수:"))

########################################################################

score_2 = "75점"
print(score_2)

# removesuffix("문자열") -> 뒤쪽의 특정 문자열을 지우고 싶을때 선언
print(score_2.removesuffix("점"))

########################################################################

city = "서울 중구"
print(city)

# 특정 문자열만 치환하고 싶을때
# replace("기존 문자열", "새로운 문자열")을 사용
print(city.replace("서울", "서울시"))