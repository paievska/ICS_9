import numpy as np

print('Ex.1')
A = np.array([[1,2],[4,-1]])
B = np.array([[2,-3],[-4,1]])
res=A.dot(B)-B.dot(A)
print('A=', A)
print('B=', B)
print('res= ', res)
print('\n')

print('Ex.2')
A = np.array([[-1,2],[0,1]])
res = np.linalg.matrix_power(A,2)
print('A= ', A)
print('res= ', res)
print('\n')

print('Ex.3')
A = np.array([[3,5],[6,-1]])
B = np.array([[2,1],[-3,2]])
res=A.dot(B)
print('A=', A)
print('B=', B)
print('res= ', res)
print('\n')

print('Ex.4')
A = np.array([[2,3,4],[1,0,6],[7,8,9]])
print('A=', A)
det_A=round(np.linalg.det(A),4)
print('det_A=', det_A)
print('\n')

print('Ex.5')
A = np.array([[1,2,3,4],[-2,1,-4,3],[3,-4,-1,2],[4,3,-2,-1]])
print('A=', A)
det_A=round(np.linalg.det(A),4)
print('det_A=', det_A)
print('\n')

print('Ex.6')
A = np.array([[1,2,-3],[0,1,2],[0,0,1]])
print('A=', A)
inv_A=np.linalg.inv(A)
print('inv_A=', inv_A)
print('\n')

print('Ex.7')
A = np.array([[1,2,3,4],[3,-1,2,5],[1,2,3,4],[1,3,4,5]])
print('A=', A)
rank_A=np.linalg.matrix_rank(A)
print('rank_A=', rank_A)
print('\n')

print('Ex.8')
delta = round(np.linalg.det([[14,4,6],[5,-3,2],[10,-11,5]]),1)
delta_x = round(np.linalg.det([[30,4,6],[15,-3,2],[36,-11,5]]),1)
delta_y = round(np.linalg.det([[14,30,6],[5,15,2],[10,36,5]]),1)
delta_z = round(np.linalg.det([[14,4,30],[5,-3,15],[10,-11,36]]),1)
if delta != 0:
    x=delta_x/delta
    y=delta_y/delta
    z=delta_z/delta
    print('x= ', x)
    print('y= ', y)
    print('z= ', z)
else:
    print('ERROR')
print('\n')

print('Ex.9')
A = np.array([[1,2,-1],[3,4,1],[5,1,-3]])
B = np.array([-3,1,-2])
delta_A = round(np.linalg.det(A),1)

if delta != 0:
    x=np.linalg.solve(A,B)
    print('x= ',x)

else:
    print('ERROR')
print('\n')

print('Ex.10.2')
m=2
n=3
A=np.random.randint(0,100, size=(m,n))
print('A=', A)
def maxline(mtx):
    return max(sum(line)/len(line) for line in mtx)
print(maxline(A))