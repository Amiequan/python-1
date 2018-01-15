from time import sleep
from selenium import webdriver

from invking_function3 import Cat1

'''
class Cat(object):
    x = 99

    def age(self):
        print('小花猫的年龄:', Cat.x)


class Zeng(Cat):
    x = 165

    def shengao(self):
        print('小小的身高为:', Zeng.x)


def login():
    driver = webdriver.Firefox()
    driver.get('http://localhost/ranzhi/www')
    sleep(1)
    driver.find_element_by_id('account').send_keys('admin')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    sleep(1)


def login1(name, pwd):
    driver = webdriver.Chrome()
    driver.get('http://localhost/ranzhi/www')
    sleep(1)
    driver.maximize_window()
    driver.find_element_by_id('account').send_keys(name)
    driver.find_element_by_id('password').send_keys(pwd)
    driver.find_element_by_id('submit').click()
    sleep(1)


def machine(x, y='珍珠奶茶'):
    print(x, y)
# machine(1)
# machine(2,'烧仙草')


def machine1(x, z, y='珍珠奶茶'):
    print(x, y, z)
# machine1(1,'你喜欢的口味')
# machine1(2, '香芋味的奶茶')
'''


class Cat:

    # def __init__(self):
    #     print('我是构造方法')

    def __del__(self):
        print('我是析构方法')
    age = 99
    weight = 6
    color = 'black'

    def eat(self):
        print('吧唧吧唧')

    def speak(self):
        print('喵喵喵...')

    def __init__(self):
        print('我是构造方法')


class Dog:
    def sleep(self):
        print('呼呼呼...')

    @staticmethod
    def run():
        print('我会跑...')


class Pig:
    weight = 100

    def sleep(self):
        print('呼噜呼噜...')

    def eat(self):
        print('呱啦呱啦...')


class Yizu(Cat1,Dog,Pig):
    age = 20
    weight = 70

    @staticmethod
    def eat():
        print('我们是吃货！')

    def sing(self):
        print('我们说话比唱歌还好听！')


# 代码入口
if __name__ == '__main__':
    # cat=Cat()
    # dog=Dog()
    # pig=Pig()
    yizu=Yizu()
    yizu.sing()
    yizu.eat()
    yizu.speak()
    yizu.sleep()
    # cat.speak()
    # dog.run()
    # dog.sleep()
    # pig.sleep()
    # Dog.run()

print(__name__)
