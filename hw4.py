from scipy.optimize import linprog
import numpy as np

c = [155, 135, 120]
A_ub = [[-0.2, -0.1, -0.1], [-0.2 , -0.2, -0.1], [-0.3, -0.25,-0.2], [-0.2,-0.25,-0.28], [-0.1,-0.2,-0.32]]
B_ub = [-4E5, -6E5, -5E5, -1E6,-3E5]
x1_bounds = (0,None)
x2_bounds = (0,None)
x3_bounds = (0,None)

res  = linprog(c,A_ub=A_ub,b_ub=B_ub,bounds=[x1_bounds, x2_bounds, x3_bounds])
print(f"The optimal solution {res.x}")
print(f"The optimal value is {res.fun}")


standard_c = [155, -155,135,-135,120, -120,0,0,0,0,0]
standard_A_eq = [[-0.2,0.2,-0.1,0.1,-0.1,0.1,1,0,0,0,0], [-0.2,0.2,-0.2,0.2,-0.1,0.1,0,1,0,0,0], [-0.3,0.3,-0.25,0.25,-0.2,0.2,0,0,1,0,0], [-0.2, 0.2, -0.25, 0.25, -0.28,0.28,0,0,0,1,0], [-0.1,0.1,-0.2,0.2,-0.32,0.32,0,0,0,0,1]]
standard_B_eq = [-4E5, -6E5, -5E5, -1E6,-3E5]
standard_bounds = (0,None)
bounds = [standard_bounds for i in range(11)]
standard_res = linprog(standard_c, A_eq= standard_A_eq, b_eq=standard_B_eq, bounds=bounds)
print(f"The optimal solution in standard form is {standard_res.x}")
print(f"The optimal value in standard form is {standard_res.fun}")



dual_b = [4E5,6E5,5E5,1E6,3E5]
dual_c = np.asarray([155, -155,135,-135,120, -120,0,0,0,0,0])
dual_A = np.transpose(np.asarray(standard_A_eq))
dual_bounds = [(None,None) for i in range (5)]
dual_res = linprog(dual_b, A_ub = dual_A, b_ub = dual_c, bounds=dual_bounds)
print(f"The optimal solution of the dual is {dual_res.x}")
print(f"The optimal value of the dual is {-1*dual_res.fun}")


# The optimal value of the dual is the same as the optimal value of the original function


