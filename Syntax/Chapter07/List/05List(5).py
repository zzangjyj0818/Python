scores = [88, 100, 96, 43, 65, 78]

#오름차순 정렬
scores.sort()
print(scores)

#내림차순 정렬
scores.sort(reverse=True)
print(scores)

for score in scores:
    if score >= 80:
        print(score)
    else:
        print('Fail')