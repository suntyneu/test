# 继承
"""
继承：有两个类，A类和B类，当我们说A类继承自B类的时候，那么A类就拥有了
B类中所有的属性和方法。
继承者称为子类，被继承者称为父类。

作用：
简化了代码，减少冗余
提高了代码的健壮性
提高了代码的安全性
是多态的前提

缺点：耦合与内聚是描述内与类之间的关系的。耦合性越低，内聚性越高，代码越好。
"""
from student import Student

stu = Student("tom", 18)
print(stu.name, stu.age)
stu.run()
stu.jump()
stu.eat("apple")
