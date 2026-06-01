# 扩展,chain的使用
class Test(object):
    def __init__(self,name):
        self.name = name
    def __or__(self, other):
        return MySequence(self) | other
    def __str__(self):
        return str(self.name)

class MySequence(object):
    def __init__(self,*args):
        self.sequence = []
        for o in args:
            self.sequence.append(o)
    def __or__(self, other):
        self.sequence.append(other)
        return self

    def run(self):
        for o in self.sequence:
            print(o)


if __name__ == '__main__':
    a = Test("a")
    b = Test("b")
    c = Test("c")

    d = a | b | c

    d.run()
    print(d)
# class Test(object):
#     def __init__(self, name):
#         self.name=name
#     def __or__(self, other):
#         return MySequence(self,other)
#     def __str__(self):
#         return str(self.name)
#
# class MySequence(object):
#     def __init__(self,*args):
#         self.sequence = []
#         for o in args:
#             self.sequence.append(o)
#
#     def __or__(self, other):
#         self.sequence.append(other)
#         return self
#
#     def run(self):
#         for o in self.sequence:
#             print(o)
