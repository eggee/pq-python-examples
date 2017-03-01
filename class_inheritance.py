class a():
    def test(arg):
        """
        blah
        """
        print 'hello'

class b(a):
    pass
    


instance = b()
instance.test()