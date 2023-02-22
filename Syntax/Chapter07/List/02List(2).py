# List

colors = ['red', 'blue', 'green']

# 수정
colors[2] = 'black'

print(colors)

# 추가
# append 사용 시 List의 가장 마지막 순서에 추가 됨
colors.append('purple')

print(colors)

# 추가
# insert 사용 시 지정된 위치에 원소를 삽입할 수 있음
# colors index = 2 -> yellow
colors.insert(1, 'yellow')
print(colors)

# 제거
# del은 특정 원소를 제거할 수 있음
del colors[0]
print(colors)

# 제거
# pop은 index를 지정해주지 않으면 list의 맨 끝 원소를 제거함
# index를 지정해주면 해당하는 인덱스의 값을 제거함

colors.pop()
print(colors)

# pop은 제거되는 값을 반환해줌
color = colors.pop(0)
print(colors)
print(color)

# 제거
# remove는 실제로 리스트에 속한 값을 직접 제거함
colors.remove('blue')
print(colors)