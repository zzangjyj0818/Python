# Loops(반복문)
# for 구문

i = 0
sum = 0

# i<101 
# 반복문에 들어가는 변수는 초기화 해주는게 좋음
# 초기화를 하지 않으면, 쓰레기 값이 들어가 
# 코드 동작에 오류를 발생시킬 수 있음

for i in range(1, 101):
    sum += i

print(sum)