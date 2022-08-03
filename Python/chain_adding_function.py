# Currying provides a way for working with functions that take multiple 
# arguments, and using them in frameworks where functions might take 
# only one argument. For example, some analytical techniques can only 
# be applied to functions with a single argument. Practical functions 
# frequently take more arguments than this.

# def change(a):
#     def sum(b):
#         def x(c):
#             def y(d):
#                 def z(e):
#                     print(a, b, c, d, e)
#                 return z
#             return y
#         return x
#     return sum


# change(10)(20)(30)(40)(50)

class add(int):
    def __call__(self,int):
        return add(self+int)

print(add(10)(5)(3))
