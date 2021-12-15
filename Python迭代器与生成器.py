Python迭代器与生成器

#用一个迭代器类，模拟Python中的range函数

class MyRange():

    def __init__(self,n):
        self.start = 0
        self.end = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            ret = self.start
            self.start += 1
            return ret
        else:
            raise StopIteration

for i in MyRange(10):
    print(i)


#用生成器函数生成Fabonacci数列

def fab(n):

    a,b = 0,1
    i=0

    while i < n:
        yield b
        a,b = b,a+b
        i+=1

for i in fab(10):
    print(i)


#不使用生成器，构建一个函数，能输出Fabonacci数列前n项

def fab1(n):

    a,b = 0,1
    i =0
    l = []

    while i < n:
        l.append(b)
        a,b = b,a+b
        i += 1
    
    return l

fab1(10)


#使用迭代器类，输出Fabonacci数列前n项

class fabo():
    
    def __init__(self,n):
        self.a,self.b = 0,1
        self.i = 0
        self.n = n
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i < self.n:
            self.a,self.b = self.b,self.a+self.b
            self.i += 1
            return self.a
        else:
            raise StopIteration

for j in fabo(10):
    print(j)