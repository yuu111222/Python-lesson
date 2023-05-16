# (1)
for i in [10,20,30,40,50]:
    print(i)
print('---------------------------')
# (2) //10～50を10ごとに表示
for i in range(10,51,10):
    print(i)
print('---------------------------')
# (3)
a = [10,20,30,40,50]
b = range(10,51,10)
for i in a:
    print(i)
print('---------------------------')
for i in b:
    print(i)
print('---------------------------')
print(type(a))
print(type(b))