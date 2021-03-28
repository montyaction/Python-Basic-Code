# def test():
# f = file('tmp.txt', 'w')
# for ch in 'abcdefg':
# f.write(ch * 10)
# f.write('\n')
# f.close()
# test()

# class A(object):
# def __init__(self, name):
# self.name = name
# def show(self):
# print 'name: %s' % (self.name, )
# class B(A):
# def __init__(self, name, desc):
# A.__init__(self, name)
# self.desc = desc
# def show(self):
# A.show(self)
# print 'desc: %s' % (self.desc, )


import string
def test():
    a = 'axbycz'
    t = string.maketrans('abc', '123')
    print(a)
    print a.translate(t)
test()