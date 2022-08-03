# Currying provides a way for working with functions that take multiple 
# arguments, and using them in frameworks where functions might take 
# only one argument. For example, some analytical techniques can only 
# be applied to functions with a single argument. Practical functions 
# frequently take more arguments than this.

# There is a magic method in class, __call__, which could be used to 
# enable class instances to behave like functions. For example, the 
# following code defines a class Add. The instance of class Add, a, could
#  be used as a function call.


class add(int):
    def __call__(self,int):
        return add(self+int)

print(add(10)(5)(3))
