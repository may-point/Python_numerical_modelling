import numpy as np
import matplotlib.pyplot as plt




'''def fun(t, x):
	return (t-1)*x'''

def fun(t, x):
	return (-t*x)/(1+(t**2))

h = 0.1
t0 = 0
x0 = 7
x = 0
T= 10
# Finds value of x for a given x using step size h
# and initial value x0 at t0.
def runge(t0, x0, x, h,T):
	# Count number of iterations using step size or
	
	n = (int)((x - t0)/h) 
	# Iterate for number of iterations
	x = x0
	x_list = [0]
	time = 0
	times = [t0]
	N = int(T/h)
	for ti in range(0, N):
		"Apply Runge Kutta Formulas to find next value of x"
		k1 = h * fun(t0, x)
		k2 = h * fun(t0 + 0.5 * h, x + 0.5 * k1)
		k3 = h * fun(t0 + 0.5 * h, x + 0.5 * k2)
		k4 = h * fun(t0 + h, x + k3)

		# Update next value of x
		x = x + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4)
		# Update next value of x
		t0 = t0 + h
		x_list.append(x)
		times.append(t0)
	return x, times, x_list

times = runge(t0,x0,x,h,T)[1]
x_list = runge(t0,x0,x,h,T)[2]
print(x_list)
tl = np.arange(0, T + h, h)




print('\n---------------- runge kutta SOLUTION-----------------')
print('-----------------------------------------')  
##  
print('i \t ti \t xi') # printing header thing
for i in range(0,int(T/h)+1):
    print(i,"\t",round(times[i],9),"\t","x",[i],": ", round(x_list[i],9),"\n")  






############ euler
'''
def euler( t_0, T, x_0, h ):
    # steps we can fit in
    N = T/h
    #
    x = x_0
    t = t_0
    t_list = [t]
    x_list = [x]
    for i in range(0,int(N)):
        x = x + h*fun(t,x)
        t = t+h
        t_list.append(t)
        x_list.append(x)
    return(t_list,x_list)

euler_times = euler(t0,T,x0,h)[0]
euler_x_val = euler(t0,T,x0,h)[1]
tl = np.arange(0, T + h, h)
'''
'''
print('\n----------------SOLUTION-----------------')
print('-----------------------------------------')  
##  
print('i \t ti \t xi') # printing header thing
for i in range(0,int(T/h)+1):
    print(i,"\t",round(times[i],4),"\t",round(euler_x_val[i],4),"\n")  

'''

#########runge kutta plotter

#print ('The value of x at x is:', runge(t0, x, x, h,T)[0])

plt.figure(figsize = (12, 8))
# calculated numerical solution 
plt.plot(times, x_list, 'bo--', label='Approximate')
# plotting exact solution
#plt.plot(tl, np.exp(((tl**2)/2)-tl), 'g', label='Exact')
#plt.plot(tl, np.exp(-20*tl), 'g', label='Exact')

#plt.plot(tl, np.exp(-tl), 'g', label='Exact')

plt.title('Runge kutta Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()


'''
###### euler plotter
plt.figure(figsize = (12, 8))
# calculated numerical solution 
plt.plot(euler_times, euler_x_val, 'bo--', label='Approximate')

# plotting exact solution
#plt.plot(tl, np.exp(((tl**2)/2)-tl), 'g', label='Exact')
plt.plot(tl, np.exp(-20*tl), 'g', label='Exact')


plt.title('Euler Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()


'''
# do not delete: may_point github

