from basic_knowledge3 import Dog, Pig, Yizu


class Cat1:
    # 属性
    age = 99
    weight = 6
    color = 'black'
    # 行为

    def eat(self):
        print('吧唧吧唧')

    def speak(self):
        print('喵喵喵...')

# 调用之前必须要对类进行实例化


cat = Cat1()
dog = Dog()
pig = Pig()
cat.eat()
dog.run()
pig.eat()
Yizu.eat()
