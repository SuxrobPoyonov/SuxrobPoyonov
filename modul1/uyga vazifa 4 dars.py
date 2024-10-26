#                               == == == == == == == 1 == == == == == == =
#  matn = "i love python"
#  matn1 = "java"
#  new = matn.replace("python","java")
#  print(new)
#
#                               == == == == == == == 2 == == == == == == =
# from math import trunc
# from symbol import return_stmt
# from traceback import print_tb
# from xmlrpc.client import boolean
#
#  matn = "Assalom mumbay"
#  matn3tasi = matn[11:14]
#  print(matn3tasi)
#                               == == == == == == == 3 == == == == == == =
#
#  matn = "banana"
#  new = ""
#  for i in matn:
#
#      if 65 <= ord(matn[0]) <= 90 :
#          new = chr(ord(matn[0]) + 32)
#      else :
#          new = chr(ord(matn[0]) - 32)
#  print(new ,end="")
#  matn = matn[1 : 6]
#  for j in matn :
#      matn[] = new
#      print(j ,end ="")
#                               == == == == == == == 4 == == == == == == =
#
#  matn = str(input())
#
#  for i in matn :
#      if i == " " :
#          i = "-"
#      print(i ,end="")
#
#                               == == == == == == == 5 == == == == == == =\
#
#  matn = str(input())
#  matn1 = ""
#  matn2 = ""
#  sana = 0
#  sana1 = 0
#  for i in matn :
#      sana +=1
#      if i == " " :
#          matn1 = matn[0 : sana]
#          matn2 = matn[sana : len(matn)+1]
#
#  print(matn2 , end= " " )
#  print(matn1)
#                               == == == == == == == 6 == == == == == == =
#
#  matn = str(input())
#  sana = 0
#  for i in matn :
#      sana+=1
#      if sana % 2 == 0 :
#          print(i , end =" ")
#
#                               == == == == == == == 7 == == == == == == =
#
#  matn = str(input())
#  son = 0
#  for i in matn :
#      if 65 <= ord(i) <= 90 :
#          son = ord(i) + 32
#          print(chr(son) ,end ="")
#      else:
#          son = ord(i) -32
#          print(chr(son),end = "")
#                               == == == == == == == 8 == == == == == == =
#
#  matn = str(input())
#  if matn.isdigit():
#      print("true")
#
#  else :
#      print("false")
#                              == == == == == == == 9 == == == == == == =
#
#  matn = str(input())
#  for i in matn :
#      if "a" <= i <= "z" :
#          print (chr(ord(i) -32) , end ="")
#      else :
#          print(i ,end ="")
#
#                               == == == == == == == 10 == == == == == == =
# matn = str(input())
# for i in matn :
#     print(i,"-",end = "")
#                                == == == == == == == 11 == == == == == == =
#
# matn = str(input())
# my_list = []
# for i in matn :
#
#     my_list = [ord(i)]
#     print(my_list , end=" ")


#                                == == == == == == == 12 == == == == == == =
#
# matn = str(input())
# son = 0
# for i in matn :
#     if "A" <= i <= "Z" :
#         son+=1
# print(son ,"ta katta harf bor")

#                               == == == == == == == 15 == == == == == == =

# matn = str(input())
# for i in matn :
#     if "a" <= i <="z" or "A" <= i <="Z" or "0" <=i<="9" :
#         print(i ,end = "")
#                               == == == == == == == 16 == == == == == == =
#
# matn = str(input())
# matn = matn[0:len(matn)-3]
# print(matn)

#                               == == == == == == == 17 == == == == == == =
#
# matn = str(input("matn kirit : "))
# n = int(input("son kirit : "))
# i = 1
# for i in range(0,n) :
#     print(matn,end="")
#                               == == == == == == == 18 == == == == == == =
#
# matn = str(input())
# a = 0
# for i in matn :
#     a += ord(i)
#
# print(a ," yigindisi")
#                               == == == == == == == 19 == == == == == == =


#  matn = str(input())
#  matn1 = ""
#  matn2 = ""
#  sana = 0
#  sana1 = 0
#  for i in matn :
#      sana +=1
#      if i == " " :
#          matn1 = matn[0 : sana]
#          matn2 = matn[sana : len(matn)+1]
#
#  print(matn2 , end= " " )
#  print(matn1)
#                               == == == == == == == 20 == == == == == == =
#
# matn = str(input())
# matn1, matn2, matn3 = "", "", ""
#
# son = 0
# son1 = 0
# for i in matn:
#     son += 1
#     if i == " ":
#         matn1 = matn[0:son + 1]
#         break
#
# for j in range(son, len(matn)):
#     son1 += 1
#     if j == " ":
#         matn3 = matn[son1: len(matn)]
#
# print( matn3)
#                               == == == == == == == 21 == == == == == == =
#
# matn = str(input("matn kirit : "))
# maks = 0
# result = ""
# for i in matn.split(' '):
#     if maks < len(i):
#         maks = len(i)
#         result = i
# print(result)
#                               == == == == == == == 22 == == == == == == =
# matn = str(input())
#
# for i in matn:
#     print(i)
#                               == == == == == == == 23 == == == == == == =
#
# matn = str(input())
# for i in matn :
#     if i.isdigit():
#         print(i)
#         break
#                               == == == == == == == 24 == == == == == == =
#
# matn = str(input())
# for i in matn :
#     if i == "a" or i=="o" or i =="u" or i =="i" or i =="e" :
#         print(i ,end=" ")
#                               == == == == == == == 25 == == == == == == =
#
# matn = str(input())
# res = ""
# son = 0
# for i in matn.split("-") :
#     if son < len(i) :
#         son = len(i)
#         res = i ;
#
# print(i)
#                               == == == == == == == 26 == == == == == == =
# matn = str(input())
# son = 0
# for i in matn:
#     print(matn[son : son+2])
#     son += 2



