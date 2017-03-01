class Test():
    def __init__(self, arg1, arg2):
        self.argument1 = arg1
        self.argument2 = arg2

    def method1(self, x):
        print x

    @staticmethod
    def method2(x):
        print x

if __name__ == '__main__':

    #NOT initializing the class - taking advantage of static method
    Test.method2("method2: other test")

    ###this would not work as class not init yet
    # Test.method1("method1: other test")

    #initializing the class - NOT taking advantage of static method
    instance = Test("arg", "blarg")
    instance.method1("method1: test")
    instance.method2("method2: test")