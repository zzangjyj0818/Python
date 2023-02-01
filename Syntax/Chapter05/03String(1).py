# 문자열(String) -> 문자의 나열

city = "seoul" # Seoul, SEOUL, SEOul
print(city)


#upper
city.upper() # city = city.upper() 해줘야 대문자 값이 적용
print(city.upper()) # 소문자를 대문자로 변경

city = city.upper()
print(city)


#lower
print(city.lower()) # 대문자를 소문자로 변경

city = city.lower()
print(city)


#공백도 컴퓨터에선 문자로 취급함.
#rstrip()은 오른쪽에 남은 공백을 없애주는 기능을 함
occupation = "developer   " #"developer" != "developer  "
print(occupation)


occupation.rstrip() 
print(occupation.rstrip())


#lstrip()은 왼쪽에 남은 공백을 없애주는 기능을 함
occupation = "   developer"
print(occupation)
occupation.lstrip() 
print(occupation.lstrip())


#python에서는 각각 한줄마다 다른 코드로 인식하기 때문에
#print 내에 있는 문자열을 단을 나눠서 출력하고 싶으면
#\n 을 사용해줌
print("INFP\nENFP\nISTJ\nESTJ")

#\t는 Tab의 간격만큼.
print("INFP\tENFP\tISTJ\tESTJ")