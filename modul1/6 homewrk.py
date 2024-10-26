#                               == == == == == == == 2 == == == == == == =
# def dublicat(satr) :
#     res= "bunday harf yuq"
#     son = -1
#     for i in range(len(satr)-2) :
#         son +=1
#         if satr[son] == satr[son+1] :
#             res = satr[son]
#
#     return res
# print(dublicat("saloom"))
#                               == == == == == == == 3 == == == == == == =
#
# def katta(satr):
#     res = ""
#     for i in satr :
#         if "A" <= i <= "Z" :
#             res += i
#
#     return res
# print(katta("SaLoM"))

#                               == == == == == == == 4 == == == == == == =
# def raqam(satr):
#     res = ''
#     for i in satr:
#         if "0" <= i <= "9":
#             res += i
#     return res
#
#
# print(raqam("sal12m3"))
#                               == == == == == == == 5 == == == == == == =
#
# def ozgar(satr) :
#     res = ""
#     for i in satr :
#         if "A" <= i <= "Z" :
#             res += chr(ord(i) + 32)
#         else :
#             res += chr(ord(i) -32)
#     return res
# print(ozgar("SalOm"))

#                               == == == == == == == 6 == == == == == == =

# def harp(satr) :
#
#     for i in satr :
#         if not ("A" <= i <= "Z" or "a" <= i <= "z") :
#             return False
#     return True
#
# print(harp("1alom"))

#                               == == == == == == == 7 == == == == == == =
#
# def A(satr):
#     res = satr.split()
#     res.reverse()
#
#     return ' '.join(res)
# print(A("salom mening ismim Suxrob"))

#                               == == == == == == == 8 == == == == == == =
#
# def zz(satr):
#     son = 0
#
#     for i in range(len(satr)-1) :
#         son += abs(ord(satr[i]) -ord(satr[i+1]))
#     return son
# print(zz("hello"))

#                               == == == == == == == 9 == == == == == == =
# def S(satr) :
#     res = ""
#     for i in satr :
#         if "." == i :
#             res += '[.]'
#         else :
#             res +=i
#     return res
# print(S("1.1.1.1.1"))
#                               == == == == == == == 10 == == == == == == =
# def sanoq(son) :
#     while








































