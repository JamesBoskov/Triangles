# from main import *

# #1ac, 2ac and 4ac
# arr = []
# for i in range(10, 99):
#     for j in range(10, 99):
#         for k in range(10, 99):
#             if triangle_validator(i, j, k):
#                 if check_triangular(i+j+k):
#                     if check_for_coprimes(i, j, k):
#                         if not i == j or i==k or  j==k:
#                             arr = [str(i), str(j), str(k)]
#                             f = open("text.txt", "a")
#                             f.write(str(arr)+", ")
#                             f.close()
# print("done")

#11ac, 10dn, 12dn
# for i in range(10, 99):
#     for j in range(10, 99):
#         for k in range(10, 99):
#             if check_pythag_triple(i, j, k):
#                 arr = [str(i), str(j), str(k)]
#                 f = open("text.txt", "a")
#                 f.write(str(arr))
#                 f.close()
# print("done")


# #13ac, 7dn, 1dn
# for i in range(100, 999):
#     for j in range(100, 999):
#         for k in range(10, 99):
#            if check_pythag_triple(i, j, k):
#                 arr = [str(i), str(j), str(k)]
#                 f = open("text.txt", "a")
#                 f.write(str(arr))
#                 f.close() 
# print("done")

#check 2dn and 3dn
# arr = []
# squares = [225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936]
# for i in range(100, 1000):
#     for j in range(100, 1000):
#         if i+j in squares:
#             arr.append([i, j])
# print(arr)

from file import *

