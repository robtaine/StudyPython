#1. 숫자 두개를 입력 받아서 사칙연산의 결과 값 내기
num1 = int(input("input integer>"))
num2 = int(input())

print("{} + {} = {}".format(num1, num2, num1+num2))
print("{} - {} = {}".format(num1, num2, num1-num2))
print("{} * {} = {}".format(num1, num2, num1*num2))
print("{} / {} = {}".format(num1, num2, num1/num2))
print()

#2. 문자열을 입력받아서 첫번째 문자를 제외한 나머지 문자열을 3번 출력하기 (print함수는 한 번만 사용해야함)
string = input("input string> ")
print(string[1:]*3)
print()

#3. 숫자 하나를 입력받아서 구구단 출력하기
degree = int(input("input degree> "))

for sub in range(1, 10):
    print("{} x {} = {}".format(degree, sub, degree * sub))

print()


#4. (선택) 입력된 숫자를 한자리수로 쪼갠 뒤 합 구하기
targetNum = input("input integer> ")
result = 0

for i in range(len(targetNum)):
    result += int(targetNum[i])

print("sum of each number =", result)