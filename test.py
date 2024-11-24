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

# counter = 0
# for j in range(len(dn2_3dn)):
#     valid = 0
#     for i in ac1_ac2_ac4:
#         print(j, len(dn2_3dn ))
#         if i[1][0] == str(dn2_3dn[j][0])[0] and i[1][1] == str(dn2_3dn[j][1])[0]:
#             valid = 1
#     if valid == 0:
#         dn2_3dn[j] = []
#         counter += 1

# for i in range(counter):
#     dn2_3dn.remove([])

# print(dn2_3dn)

for ac1_2_4 in ac1_ac2_ac4:
    for dn2_3 in dn2_3dn:
        for ac_13_dn7_1 in ac13_7dn_1dn_or_14ac_9dn_5dn:
            for ac14_dn9_5 in ac13_7dn_1dn_or_14ac_9dn_5dn:
                for ac11_dn10_12 in ac11_dn10_dn12:
                    pass