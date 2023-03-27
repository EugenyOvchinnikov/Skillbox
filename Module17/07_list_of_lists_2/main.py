nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

res_list = [step3 for step1 in nice_list for step2 in step1 for step3 in step2]

print(res_list)