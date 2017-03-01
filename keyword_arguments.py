#http://stackoverflow.com/questions/1419046/python-normal-arguments-vs-keyword-arguments

# there are two related concepts, both called "keyword arguments".

# On the calling side, which is what other commenters have mentioned, you have the ability to specify some function arguments by name. You have to mention them after all of the arguments without names (positional arguments), and there must be default values for any parameters which were not mentioned at all.

# The other concept is on the function definition side: You can define a function that takes parameters by name -- and you don't even have to specify what those names are. These are pure keyword arguments, and can't be passed positionally. The syntax is



def my_function(**kwargs):
    print str(kwargs)
    for key, value in kwargs.iteritems():
        print key, value

    if "do_something" in kwargs:
        print "better do something with " + str(kwargs["do_something"])

my_function(a=12, b="abc", do_something="what is this")