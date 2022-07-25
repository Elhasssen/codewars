x = [1,2,3]

y = [1,2]
s = []

for a in x:
    if a not in y:
        s.append(a)
print(s)
# for b in x : 
#     if y[0] == b:
#         continue
#     s.append(b)
# print(s)
# def array_diff(a, b):
#     Reccu = 0
#     s = []
#     for elm in a:
#         if b == []:
#             return a
#         else : 
#             for m in b :
#                 if m == elm :
#                     Reccu += 1
#                     continue
#                 elif Reccu == 0 : s.append(elm)
              
#     return s
# print(array_diff(x, y))   
# def array_diff(a,b):
