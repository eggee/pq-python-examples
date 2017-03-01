#good overview: https://learnpythonthehardway.org/book/ex44.html

class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()


# class A(object):
#     def foo(self):
#         print 'A'
 
# class B(A):
#     def foo(self):
#         print 'B'
#         super(B, self).foo()
 
# class C(A):
#     def foo(self):
#         print 'C'
#         super(C, self).foo()
 
# class D(B,C):
#     def foo(self):
#         print 'D'
#         super(D, self).foo()
 
# d = D()
# d.foo()
