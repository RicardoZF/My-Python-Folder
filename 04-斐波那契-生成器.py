def Builders(num):
    count = 0
    a = 0
    b = 1
    while count < num:
        yield a
        a, b = b, a+b
        count += 1


process = Builders(3)
# for i in process:
#     print(i)
print( next(process))
print( next(process))
print( next(process))
print( next(process))
