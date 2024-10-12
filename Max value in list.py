import sqlite3
print(sqlite3.Connection)

num=[2,1,54,15,45,35,84,32,51,32,32,12,11,2,32,38,87,54]
c=0
# by looping
for i in range(18):
    b = num[i]
    if b>c:
        c=b
print(c)        
# by built in function
print(max(num))