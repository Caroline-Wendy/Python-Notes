# -*- coding: utf-8 -*-

#两种写入文件的方法
movies = ["Old Woman", "Woman", "Girl", "Little Girl"]
name = "Ren Tian Tian"
thefile = open('thefile.txt','w')
print >>thefile, name
thefile.write(name) #只能写入字符串
thefile.close();