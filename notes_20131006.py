# -*- coding: utf-8 -*-
#Tab为提示输出, list在Python标准库的4.6

#创建列表(list)
movies = ["Old Woman", "Woman", "Girl", "Little Girl"]

#输出
print(movies) #全部
print(movies[0]) #单个数据项
print(len(movies)) #长度

#添加末尾项
movies.append("Ladyboy")
print(movies)

#pop某一项, 默认为最后一项
print(movies.pop(4))

#extend拼接list
woman_shoes = ["High-heeled", "Mules", "Slingbacks", "Ballet flats"]
movies.extend(woman_shoes)
print(movies)

#reverse颠倒顺序
movies.reverse()
print(movies)

#打开文件
sometext = open("thefile.txt", "w")
print >>movies, sometext