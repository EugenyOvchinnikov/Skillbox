# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
#              [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
#
# res_list = [res_list.extend(x) for x in nice_list]
#
# print(res_list)

nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

flat = [lvl_1 for lvl_1 in nice_list]
# flat = [lvl_3 for lvl_1 in nice_list for lvl_2 in lvl_1 for lvl_3 in lvl_2]
print(flat)