'''九九乘法表'''

for i in range(1,10):
    for j in range(1,10):
        if i >= j:
            print("%d*%d=%2d" % (j, i, j*i), end="  ")
    print("")

num = 10
for i in range(1, num):
    for j in range(1, i+1):
            print("%d*%d=%2d" % (j, i, j*i), end="  ")
    print("")

i = 1
i_num = 10
j_num = 1
while i < i_num:
    j = j_num
    while j <= i:
        print("%d*%d=%2d" % (j, i, j*i), end="  ")
        j += 1
    print("")
    i += 1
    
'''一句话写出九九乘法表'''
print('\n'.join([' '.join(['%s*%s=%-2s' % (y, x, x*y) for y in range(1, x+1)]) for x in range(1, 10)]))


'''左上三角格式输出九九乘法表'''
for i in range(1, 10):
     for j in range(i, 10):
         print("%d*%d=%2d" % (i, j, i*j), end=" ")
     print("")
