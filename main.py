def make_args(crossnum):
    ac1 = crossnum[0:2]
    ac2 = crossnum[2:4]
    ac4 = crossnum[4:6]
    dn2 = crossnum[2] + crossnum[8]
    dn3 = crossnum[3] + crossnum[9]
    ac11 = crossnum[14:16]
    dn10 = crossnum[12] + crossnum[18]
    dn12 = crossnum[17] + crossnum[23]
    ac13 = crossnum[18:21]
    dn7 = crossnum[7] + crossnum[13]
    dn1 = crossnum[0] + crossnum[6]
    ac14 = crossnum[21:24]
    dn9 = crossnum[10] + crossnum[16]
    dn5 = crossnum[5] + crossnum[11]

    return ac1, ac2, ac4, dn2, dn3, ac11, dn10, dn12, ac13, dn7, dn1, ac14, dn9, dn5

def THE_VALIDATOR(args, strcrossnum):
    if strcrossnum[2] == "0" or strcrossnum[3] == "0" or strcrossnum[4] == "0" or strcrossnum[5] == "0" or strcrossnum[6] == "0" or strcrossnum[7] == "0" or strcrossnum[9] == "0" or strcrossnum[10] == "0" or strcrossnum[12] == "0" or strcrossnum[14] == "0" or strcrossnum[17] == "0" or strcrossnum[18] == "0" or strcrossnum[21] == "0":
        return False
    ac1 = int(args[0])
    ac2 = int(args[1])
    ac4 = int(args[2])
    if not triangle_validator(ac1, ac2, ac4):
        return False
    if not check_triangular(ac1 + ac2 + ac4):
        return False
    if not ac1 % 2 == 1 or ac2 % 2 == 1 or ac4 % 2 == 1:
        return False
    if check_prime_2d(ac1) or check_prime_2d(ac2) or check_prime_2d(ac4):
        return False
    
    check_for_coprimes(ac1, ac2, ac4)

    dn2 = int(args[3])
    dn3 = int(args[4])

    if not check_square(dn3+dn2):
        return False
    
    ac11 = int(args[5])
    dn10 = int(args[6])
    dn12 = int(args[7])
    if not check_pythag_triple(ac11, dn10, dn12):
        return False
    
    ac13 = int(args[8])
    dn7 = int(args[9])
    dn1 = int(args[10])
    if not check_pythag_triple(ac13, dn7, dn1):
        return False
    
    ac14 = int(args[11])
    dn9 = int(args[12])
    dn5 = int(args[13])
    if not check_pythag_triple(ac14, dn9, dn5):
        return False
    
    return True



    
def triangle_validator(side1, side2, side3):
    if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
        return False
    else:
        return True

def check_triangular(num):
    triangles = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120,136, 153, 171, 190, 210, 231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990,]
    if not num in triangles:
        return False
    else:
        return True
    
def check_prime_2d(num):
    primes = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    if not num in primes:
        return False
    else:
        return True

def check_prime_3d(num):
    primes = [211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993, 1997, 1999]
    if not num in primes:
        return False
    else:
        return True

def check_square(num):
    squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936]
    if not num in squares:
        return False
    else:
        return True

def get_factors(x):
    arr = []
    for i in range(1, x + 1):
        if x % i == 0:
            arr.append(i)
    arr.pop(0)
    return arr

def check_for_coprimes(num1, num2, num3):
    factors1 = get_factors(num1)
    factors2 = get_factors(num2)
    factors3 = get_factors(num3)
    for i in factors1:
        if i in factors2 or i in factors3:
            return False
    for i in factors2:
        if i in factors3:
            return False
    return True

def check_pythag_triple(num1, num2, num3):
    #CBA to precompute, do this last
    if not check_for_coprimes(num1, num2, num3):
        return False
    a = [num1, num2, num3]
    a.sort()
    if not (a[0]**2 + a[1]**2)**0.5 == a[2]:
        return False
    else:    
        return True