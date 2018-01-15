
'''
import this
美丽比丑陋更好。
显式比隐式更好。
简单的比复杂的更好。
复杂的比复杂的更好。
平面比嵌套更好。
稀疏的比致密的好。
可读性计数。
特殊的情况不够特别，无法打破规则。
虽然实用性胜于纯度。
错误永远不能无声地传递。
除非明确沉默。
在模糊的面前，拒绝猜测的诱惑。
应该有一个——最好是只有一个——显而易见的方法。
虽然这种方式一开始可能不明显，除非你是荷兰人。
现在比永远都好。
虽然从来没有比现在更好正确现在[ 5 ]
如果执行很难解释，这是一个坏主意。
如果执行很容易解释，这可能是一个好主意。
命名空间是一个伟大的想法——让我们做更多的这些！
'''


# 打印和注释
'''
print('  静夜诗')
print("床前明月光")
print('疑是地上霜')
print("举头望明月")
print('低头思姑凉')
'''
"""
print('  静夜诗')
print("床前明月光")
print('疑是地上霜')
print("举头望明月")
print('低头思姑凉')
"""

# 变量(赋值、运算符)
a = 1
b = 1+1
print(a)
print(b)
c = 5 <= 2
print(c)
d = 5 >= 2
print(d)
e = 1 != 2
print(e)
f = 2 == 2   # （=赋值，==判断）
print(f)
g = 5 < 2  and  3 > 2
print(g)
h = 5 < 2 or 3 > 2
print(h)
i = not 1 > 2
print(i)


lay = 4
for i in range(1, lay+1):   # 定义层
    print(' '*(lay-i), end='')  #
    if i == 1 or i == lay:
        print((2*i-1)*'*')
    else:
        print('*', end='')
        print(' '*(2*(i-1)-1), end='')
        print('*')
'''
   *
  * *
 *   *
*******
'''


lay = 4
for i in range(1, lay+1):
    print((lay-i)*' ', end=' ')
    print((2*i-1)*'*')
'''
    *
   ***
  *****
 *******
 '''

lay = 4
for i in range(1, 2*lay, 2):
    print('*'*i)
'''
*
***
*****
*******
'''

lay = 4
for i in range(1, lay + 1):
    print('*'*i)
'''
*
**
***
****
'''

lay = 4
for i in range(1, lay +1):
    print((lay-i)*' ', end=' ')
    print(i*'*')
'''
    *
   **
  ***
 ****
'''