#!/usr/bin/python

class Parent:        # define parent class
   parentAttr = 100
   def __init__(self):
      print "Calling parent constructor"
   def myMethod(self):
	  print "parent method"		
   def parentMethod(self):
      print 'Calling parent method'
   def setAttr(self, attr):
      Parent.parentAttr = attr
   def getAttr(self):
      print "Parent attribute :", Parent.parentAttr

class Child(Parent): # define child class
   def __init__(self):
      print "Calling child constructor"
   def myMethod(self):
	  print "parent method overidden"
   def childMethod(self):
      print 'Calling child method'


p = Parent()
print p.parentAttr	  
c = Child()  
p.setAttr(75) 
print c.parentAttr         # instance of child
c.setAttr(50)
print c.parentAttr
print p.parentAttr
print '-------------'
print p.myMethod()
print c.myMethod()
c.childMethod()      # child calls its method
c.parentMethod()     # calls parent's method
c.setAttr(200)       # again call parent's method
c.getAttr()          # again call parent's method



# class Parent:        # define parent class
#    def myMethod(self):
#       print 'Calling parent method'

# class Child(Parent): # define child class
#    def myMethod(self):
#       print 'Calling child method'

# c = Child()          # instance of child
# c.myMethod()         # child calls overridden method
# p = Parent()
# p.myMethod()
