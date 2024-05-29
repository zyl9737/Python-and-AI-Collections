# 1. 当一个实例方法对象被调用时，会调用对应的下层函数 (__func__)，并将类实例 (__self__) 插入参数列表的开头。
# 例如，当 A 是一个包含了 f() 函数定义的类，而 o 是 A 的一个实例，则调用 0.f(1) 就等同于调用 A.f(o, 1)。
# 2. 还有一个需要关注的要点是作为一个类实例属性的用户定义函数不会被转换为绑定方法；
# 这样的变换 仅当 函数是类属性时才会发生。
# 1
class A:
    def f(self, data):
        print(self.name)
        print(data)

o = A()
o.name = "Bob"

A.f(o, "hello")
o.f("hello")


# 2
# class FuncDescr:
#     def __get__(self, *args):
#         def f(self, data):
#             print(self.name)
#             print(data)
#         return f

# class A:
#     f = FuncDescr()

# o = A()
# o.name = "Bob"
# print(o)
# # 哪个是对的？
# # o.f("hello")
# o.f(o, "hello")