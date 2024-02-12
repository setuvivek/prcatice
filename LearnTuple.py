# t1 = (2, 2, 324, 22, 22, 'facs', 'caz')
# print(len(t1))
# # with one value we can not create tuple
# t2 = ('biren')
# print(type(t2))
# t2 = ('biren',)
# print(type(t2))
#
# t3 = tuple(("biren", 'chauhan', 'V', 'setu'))
# print(t3)
# print(type(t3))
#
# print(t3[1])
# print(t3[-1])
# print(t3[1:-1])
# print(t3[2:])
# print(t3[:2])
# print(t3[::-1])
# print(t3[-3:-1])
#
# if 'V' in t3:
#     print(True)
#
# # with creating tuple to list you can do all opration in list
# l1 = list(t3)
# l1.append("consulting")
# print(l1)
# t3 = tuple(l1)
# print(t3)
#
# t3 += t2
# print(t3)
#
# del t3
# # Unpack tuple
# t4 = ('Green', 'Red', 'Blue', 'Sky Blue', 'Black', 'White')
# (*Tree, error, water, sky) = t4
# print(Tree)
# print(error)
# print(water)
# print(sky)
#
# (Tree, error, *water, sky) = t4
# print(Tree)
# print(error)
# print(water)
# print(sky)
#
# (Tree, error, water, *sky) = t4
# print(Tree)
# print(error)
# print(water)
# print(sky)
#
# # loops
#
# for i in t1:
#     print(i, end=' ')
#
# print()
# for i in range(len(t1) - 1, 0, -1):
#     print(t1[i], end=' ')
#
# print()
# i = 0
# while i <= len(t1) - 1:
#     print(t1[i], end=' ')
#     i += 1
#
# print()
# t5 = t1 + t4
# print(t5)
#
# t6 = t5 * 2
# print(t6)
#
# print(t6.count(2))
# print(t6.index(22, 7))
#
# print(len(t5))
#
# print('213e' in t5)

