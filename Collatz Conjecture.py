# for i in range(0, 11):
#     if i % 2 != 0:
#         print (i)


# x = 1
# while x < 11:
#     if x % 2 != 0:
#         print(x)
#     x += 1


# for ch in "john.smith@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, end="")


# for digit in "0165031806510":
#     if digit == "0":
#         print("x", end="")
#         continue
#     print(digit, end="")

import datetime
a = []

def test():
    count = 0
    for i in range(0, 100001):
        if i % 2 != 0:
            count+=1
            print(i)
    
    # count = 0
    # i = 1
    # while i < 100001:
    #     if i % 2 != 0:
    #         count+=1
    #         print(i)
    #     i += 1

    # i=1
    # while i != 100001:
    #     print(i)
    #     i+=2


y = datetime.datetime.now()
test()
x = datetime.datetime.now()
z=x-y
a.append(z)
y = datetime.datetime.now()
test()
x = datetime.datetime.now()
z=x-y
a.append(z)
y = datetime.datetime.now()
test()
x = datetime.datetime.now()
z=x-y
a.append(z)

print(a)