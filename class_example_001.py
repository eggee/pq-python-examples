class a():
    def test(arg):
        """
        blah
        """
        print 'hello'

class b():
    instance = a()
    instance.test()


instance_other = b()
