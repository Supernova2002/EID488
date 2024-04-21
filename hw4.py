from scipy.optimize import linprog


c = [155, 135, 120]
A_ub = [[-0.2, -0.1, -0.1], [-0.2 , -0.2, -0.1], [-0.3, -0.25,-0.2], [-0.2,-0.25,-0.28], [-0.1,-0.2,-0.32]]
B_ub = [-4E5, -6E5, -5E5, -1E6,-3E5]
x1_bounds = (0,None)
x2_bounds = (0,None)
x3_bounds = (0,None)

res  = linprog(c,A_ub=A_ub,b_ub=B_ub,bounds=[x1_bounds, x2_bounds, x3_bounds])
print(f"The optimal values are {res.x}")
print(f"The optimal value is {res.fun}")


standard_c = [155, -155,135,-135,120, -120,0]
standard_A_ub = [[-0.2,0.2,-0.1,0.1,-0.1,0.1,1], [-0.2,0.2,-0.2,0.2,-0.1,0.1,1], [-0.3,0.3,-0.25,0.25,-0.2,0.2,1], [-0.2, 0.2, -0.25, 0.25, -0.28,0.28,1], [-0.1,0.1,-0.2,0.2,-0.32,0.32,1]]
standard_B_ub = [-4E5, -6E5, -5E5, -1E6,-3E5]
standard_bounds = (0,None)
bounds = [standard_bounds for i in range(7)]
standard_res = linprog(standard_c, A_ub = standard_A_ub, b_ub=standard_B_ub, bounds=bounds)
print(f"The optimal values in standard form are {standard_res.x}")
print(f"The optimal value in standard formn is {standard_res.fun}")
