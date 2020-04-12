"""
2주차 스터디 퀴즈

- 1번 문제

정수를 하나 씩 입력 받아서 0을 입력하면 이전까지 입력한 정수 모든 합을 출력하기
ex)
숫자 입력 : 5
숫자 입력 : 4
숫자 입력 : 3
숫자 입력 : 2
숫자 입력 : 10
숫자 입력 : -1
숫자 입력 : 0
결과 :  23
"""
valueSum = 0

while True:
    inputValue = int(input("숫자 입력 >"))

    if inputValue == 0 :
        print("결과 : {}".format(valueSum))
        break

    valueSum += inputValue


"""
- 2번 문제

피라미드 별찍기
ex) 찍을 줄 수 : 4
   *
  ***
 *****
*******
"""

rowCount = int(input("줄 수>"))

for i in range(1, rowCount + 1):
    print(" " * (rowCount - i), "*" * (i * 2 - 1), sep="")


"""
- 3번 문제

리스트 내포를 사용해서 0 ~ 100 까지의 수 중 2와 3의 공배수를 출력하기
단, 답은 한줄로 표현 가능해야 함 (2와 3이 포함되어야함)
단, if 안에는 하나의 조건만 판단해야 함
ex)  [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]
추가: 플머님들은 if문에 조건은 단 하나로 해야하고, 가장 최적화된 결과를 도출해 낼 수 있도록 할것
"""
print( [ i for i in range(0, 100+1, 2) if i % 3 == 0])


"""
- 4번 문제

10개의 문자를 입력 받아서 같은 문자열의 개수를 세는 Dict를 print 한다.

ex)
1문자 입력 : ABC
2문자 입력 : ABC
3문자 입력 : GOOD
4문자 입력 : BC
5문자 입력 : BC
6문자 입력 : ABC
7문자 입력 : GOOD
8문자 입력 : ABC
9문자 입력 : ABC
10문자 입력 : ABC

결과 : {'ABC': 6, 'GOOD' : 2, 'BC':2}
"""

inputCount = 1
dic = {}

while True:
    inString = str(input("{}문자 입력 >".format(inputCount)))
    inputCount += 1

    if inString == "quit":
        break
    
    if not (inString in dic):
        dic[inString] = 1
    else:
        dic[inString] += 1
            
print(dic)