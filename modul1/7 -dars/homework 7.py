#                               == == == == == == == 2 == == == == == == =
#
# l = [1, 2, 1 ,5,6]
# res = 0
# for i in l :
#     res+=i
# print(res)
from operator import index

#                               == == == == == == == 3 == == == == == == =
#
# l = [ "suxrob" , "bilimli" ,"bola"]
# a = ",".join(l)
# print(a)

#                               == == == == == == == 4 == == == == == == =
#
# l = [1 ,2,1]
# print(l*2)
#                               == == == == == == == 6 == == == == == == =
#
# l =[1, 2, 3, 4,5]
# print(max(l)) ,print(min(l))
# =========================================================================================================
#                               == == == == == == == 1 == == == == == == =
# l = [1, 2, 3, 5, 4, 21]
# res = ""
# maxx = l[0]
# minn = l[0]
# for i in l:
#     if maxx < i :
#         maxx = i
#     if minn > i :
#         minn = i
# print(maxx)
# print(minn)
#                               == == == == == == == 2 == == == == == == =
#
# l = [1 ,2 ,3, 4, 5]
# A = l[::-1]
# print(A)
#                               == == == == == == == 3 == == == == == == =

# l = [1,2,3,4,5,6]
# juf =[]
# toq =[]
# for i in l :
#     if i % 2 == 0:
#         juf.append(i)
#     else:
#         toq.append(i)
# print("juft sonlar : " ,juf)
# print("toq sonlar : " ,toq)

#                               == == == == == == == 5 == == == == == == =
# l = [1, 2, 3, 4, 5]
# res = 0
# for i in l :
#     res += i
# print(res)
#                               == == == == == == == 6 == == == == == == =
l = ["A" ,1 ,2 ,"C"]
for i in l:
    res = False
    if i == "A":
        res =True
        break
print(res)
#                               == == == == == == == 7 == == == == == == =
#
# l = ["B","D","A","salom"]
# A =sorted(l)
# print(A)
#                               == == == == == == == 8 == == == == == == =
# l = [1 ,2, 3, 4,5]
# x = []
# for i in l :
#     x.append(i**2)
# print(x)
#                               == == == == == == == 9 == == == == == == =
# l = []
# i =1                              ISHLOLMADIM
# while i <= 5:
#     l.extend(i*"A")
#     i+=1
#
# print(l)

#                               == == == == == == == 10 == == == == == == =
# l = [1 ,2,3 ,4 ]
# del l[0]
# print(l)

#                               == == == == == == == 11 == == == == == == =
#
# l = [1 ,2 ,3 ,4,5]
# res = 1
# for i in l :
#     res *= i
# print(res)
#                               == == == == == == == 12 == == == == == == =
# l = [1 ,2 ,3 ,4,4]
# res =0
# for i in l :
#     res += i
# print(res/len(l))
#                               == == == == == == == 13 == == == == == == =
# def almash(l,son) :
#     for i in range(len(l)):
#         if i <= 0 :
#             i = son              ISHLAMADI
#     return l
# l = [1 ,2,-3 ,0]
# yangi = almash(l,10)
# print(yangi)

#                               == == == == == == == 15 == == == == == == =
# c = int(input("index kirit :"))
# a = str(input("str kirit :"))
# l = [1 ,2, 4,5 ,6]
# l[c] = a
# print(l)
#                               == == == == == == == 17 == == == == == == =
# l = ['a','b',"sal"]
# x = []
# for i in l :
#     x.append(i.upper())
# print(x)
#                               == == == == == == == 18 == == == == == == =
#
# l = [1 ,2, 3,4,5]
# y = []
# y = l.copy()
# print(y)

#                               == == == == == == == 19 == == == == == == =

# l = [1 ,2, 4,54,4,4]
# maxx = 0
# se = ""
# for i in l :
#     if maxx <l.count(i) :
#         maxx = count(i)
#         se =str(i)
# print(se)
#                               == == == == == == == 20 == == == == == == =
#
# son = int(input("son kirit :"))
# l = [1 , 3 ,7, 4 ,5, 3,9 ,2,0]
# A =l.index(son)
# x =[]
#
# for i in range(len(l)) :
#     if l[A] < l[i] :
#         x.append(l[i])
#
# print(x)
#                               == == == == == == == 21 == == == == == == =
# l = [1 ,2, 3,5]
# x =[]
# for i in l :
#     x.append(i*2)
# print(x)

#                               == == == == == == == 22 == == == == == == =
# l = [ -1 ,1 ,-2 ,10 ]
# x =[]
# for i in l :
#     if i >= 0:
#         x.append(i)
# print(x)
#                               == == == == == == == 23 == == == == == == =
#
# l = [1 ,2, 3 ,4, 5,6]
# A =l[::-1]
# print(A)


#                               == == == == == == == 24 == == == == == == =


# l = [1 ,2 ,3,4, 5 ]
# res = []
# son = 0
# for i in l :
#     res.append(son*i)
#     son +=1
# print(res)
#                               == == == == == == == 26 == == == == == == =
# l = [1 ,2 ,3,4,5]
# x =[]
# for i in l :
#     x.append(i+10)
# print(x)
#                               == == == == == == == 27 == == == == == == =
# l = [1 ,2 ,3,4,5]
# x =[]
# for i in l :
#     x.append("*"+(i)
# print(x)
#                               == == == == == == == 28 == == == == == == =
# l = [1 ,2 ,3,4,5]
# x =[]
# for i in l :
#     x.append(i+10)
# print(x)
#                               == == == == == == == 29 == == == == == == =

# l = [1 ,2 ,3, 4, 5]
# x =[]
# for i in l:
#     if not i %2 ==0:
#         x.append(i*5)
#     else:
#         x.append(i)
#
# print(x)

#                               == == == == == == == 30 == == == == == == =

# l = [1 ,2 ,3 ,2 ,4, 2]
# son = 0
# for i in l :
#     if i == l[1] :
#         son +=1
# print(son)


