print("공백")
print()
print("#공백")
print(1,2,3,4, 5)
print(len("안녕하세요"))
print("안녕" + "하세요"*3)
pi = 3.14
pi = "a"
print(pi)

number = input("입력 : ")
print(type(number))

pets = [
    {"name":"샌디", "age":5},
    {"name":"브라운", "age":2},
    {"name":"해피", "age":1},
    {"name":"안나", "age":3},
]

for pet in pets:
    print(pet["name"],"{}살".format(pet["age"]))
    