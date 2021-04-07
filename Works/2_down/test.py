# import random

# def Hundred():
#     # count = 0
#     while True:
#         num_a = random.randint(11,99)
#         num_b = random.randint(11,99)
#         if num_a != num_b:
#             if num_a > num_b:
#                 diff = num_a - num_b
#             else:
#                 diff = num_b - num_a
#             # count += 1
#             return diff,num_a,num_b
#         else:
#             continue
# for i in range(10):
#     print(Hundred())
#     print(type(Hundred()))

# def HundredSum():
#     while True:
#         num_a = random.randint(11,80)
#         num_b = random.randint(11,80)
#         if num_a + num_b < 100:
#             sumA = num_a + num_b
#             return sumA,num_a,num_b
#         else:
#             continue


# print('=' * 10)
# def Thousand():
#     while True:
#         num1_1 = random.randint(1,9)
#         num1_2 = random.randint(1,9)
#         if num1_1 != num1_2:
#             num1_2 *= 10
#             num1_1 *= 10

#             if num1_1 > num1_2:
#                 while True:
#                     num2_1 = random.randint(1,9)
#                     num2_2 = random.randint(1,9)
#                     if num2_1 != num2_2:
#                         num2_1 *= 100
#                         num2_2 *= 100
#                         if num2_1 > num2_2:
#                             num_big = num1_1 + num2_1
#                             num_low = num1_2 + num2_2
#                             return num_big - num_low,num_big,num_low
#                         else:
#                             num_big = num1_1 + num2_2
#                             num_low = num1_2 + num2_1
#                             return num_big - num_low,num_big,num_low
#                     else:
#                         continue
#             else:
#                 while True:
#                     num2_3 = random.randint(1,9)
#                     num2_4 = random.randint(1,9)
#                     if num2_3 != num2_4:
#                         num2_3 *= 100
#                         num2_4 *= 100
#                         if num2_3 > num2_4:
#                             num_big = num1_2 + num2_3
#                             num_low = num1_1 + num2_4
#                             return num_big - num_low,num_big,num_low
#                         else:
#                             num_big = num1_2 + num2_4
#                             num_low = num1_1 + num2_3
#                             return num_big - num_low,num_big,num_low
#                     else:
#                         continue
#         else:
#             continue
# for i in range(10):
#     print(Thousand())

# print('=' * 10)


# def Thousand():
#     while True:
#         num_a = random.randint(1,99) * 10
#         num_b = random.randint(1,99) * 10
#         if num_a != num_b:
#             if (num_a / 100) % 10 > (num_b / 100) % 10:
#                 if (num_a / 10) %10 > (num_b / 10) % 10:
#                     numdiff = num_a - num_b
#                     return numdiff,num_a,num_b
#                 else:
#                     continue
#             else:
#                 if (num_a / 10) %10 > (num_b / 10) % 10:
#                     continue
#                 else:
#                     numdiff = num_b - num_a
#                     return numdiff,num_b,num_a
#         else:continue

# for i in range(10):
#     a = Test()
#     print(a)



# def Thousand():
#     while True:
#         num1_1 = random.randint(1,9)
#         num1_2 = random.randint(1,9)
#         if num1_1 != num1_2:
#             num1_2 *= 10
#             num1_1 *= 10

#             if num1_1 > num1_2:
#                 while True:
#                     num2_1 = random.randint(1,9)
#                     num2_2 = random.randint(1,9)
#                     if num2_1 != num2_2:
#                         num2_1 *= 100
#                         num2_2 *= 100
#                         if num2_1 > num2_2:
#                             num_big = num1_1 + num2_1
#                             num_low = num1_2 + num2_2
#                             return num_big - num_low,num_big,num_low
#                         else:
#                             num_big = num1_1 + num2_2
#                             num_low = num1_2 + num2_1
#                             return num_big - num_low,num_big,num_low
#                     else:
#                         continue
#             else:
#                 while True:
#                     num2_3 = random.randint(1,9)
#                     num2_4 = random.randint(1,9)
#                     if num2_3 != num2_4:
#                         num2_3 *= 100
#                         num2_4 *= 100
#                         if num2_3 > num2_4:
#                             num_big = num1_2 + num2_3
#                             num_low = num1_1 + num2_4
#                             return num_big - num_low,num_big,num_low
#                         else:
#                             num_big = num1_2 + num2_4
#                             num_low = num1_1 + num2_3
#                             return num_big - num_low,num_big,num_low
#                     else:
#                         continue
#         else:
#             continue

# import random
# def ThousandSum():
#     while True:
#         num_a = random.randint(1,99) * 10
#         num_b = random.randint(1,99) * 10
#         if num_a != num_b:
#             if ((num_a / 100) % 10 + (num_b / 100 ) % 10 ) < 10 and ((num_a / 10) % 10 + (num_b / 10 ) % 10 ) < 10:
#                 return str(num_a) + ' + ' + str(num_b) + ' = '
#             else:continue


# def CreateCompute():
#     while True:
#         num_a = random.randint(71,899)
#         num_b = random.randint(71,899)
#         if num_a > num_b:
#             # sum_a = num_a + num_b
#             # diff_a = num_a - num_b
#             if random.randint(1,2) == 1:
#                 return str(num_a) + ' + ' + str(num_b) + ' = '
#             else:
#                 return str(num_a) + ' - ' + str(num_b) + ' = '
#         else:
#             # sum_b = num_b + num_a
#             # diff_b = num_b - num_a
#             if random.randint(1,2) == 1:
#                 return str(num_a) + ' + ' + str(num_b) + ' = '
#             else:
#                 return str(num_b) + ' - ' + str(num_a) + ' = '

# for i in range(20):
#     print(CreateCompute())

with open('tmp.txt','rt',encoding='utf-8') as f:
    for line in f.readlines():
        if line != '':
            print(line,end = '')









