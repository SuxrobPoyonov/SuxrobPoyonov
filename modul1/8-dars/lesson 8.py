from Tools.scripts.pathfix import keep_flags

ovqat1 = input("birinchi ovqatni kirit : ")
ovqat2 = input("ikkinchi ovqatni kirit : ")
ovqat3 = input("uchinchi ovqatni kirit : ")

menyu = { "manti" : 1000 , "osh" : 2000 , "somsa" : 3000}
matn = ""

for _ in menyu.keys() :
    if ovqat1 or ovqat2 or  ovqat3 in menyu.keys() :
        print(menyu)
    else :
        print("bunday ovqat yo")





