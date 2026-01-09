import numpy as np




productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])
# productivity <8
print(productivity[productivity<8])
print(productivity[(productivity>=5 )& (productivity <= 7)])
# print working hrs of first employee
first_emp_working_hrs=productivity[:,0]
print(first_emp_working_hrs)
print(first_emp_working_hrs[first_emp_working_hrs<8])
# print last two employees working hrs<7
last_two_emp_working_hrs=productivity[:,8:10]
print(last_two_emp_working_hrs)#[[78]
                                #[67]
                                #[8 9]
                                #[6 5]
                                #[7 8]
                                #[8 9]]
print(last_two_emp_working_hrs[last_two_emp_working_hrs<7])# 6 6 5
# print working hrs <8 =0
productivity[productivity<8]=0
print(productivity)#[[8 0 8 0 0 8 9 8 0 8]
                    #[0 0 0 0 0 0 8 0 0 0]
                    #[9 8 9 8 9 9 8 9 8 9]
                    #[0 0 0 0 0 0 0 0 0 0]
                    #[0 8 0 8 0 8 0 8 0 8]
                    #[8 9 8 9 8 9 8 9 8 9]]

                    