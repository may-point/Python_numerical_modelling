import numpy as np
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# script to model long term behaviour of system given some initial conditions

#initialising values
#t_0 = float(input("enter initial t_0: ")) # uncomment for option to enter initial time
b = 0.05 
t_0 =10 # initial time
T = 500
x1_0 = 30 #alpha
x2_0 = 0 #beta
x3_0 = 30 #gamma
h = 0.05

# euler for f(t,x1)
def euler( t_0, T, x1_0, h ):
    # steps we can fit in
    N =int(T/h)
    #
    x1 = x1_0 #initialising x1
    x2 = x2_0 #initialising x2
    t = t_0 #initialising time
    t_list = [t] #initialising time list
    x1_list = [x1] #initialising x1 list
    for i in range(0,N):
        x1 = x1 + h*(np.sin(x2)-b*x1)
        t = t+h
        t_list.append(t)
        x1_list.append(x1)
    return(t_list,x1_list)

# getting values from euler fn
times_x1 = euler(t_0,T,x1_0,h)[0]
x1_val = euler(t_0,T,x1_0,h)[1]

#arranging the list of times and steps
tl_x1 = np.arange(0, T + h, h)

#euler
#for f(t,x2)
def euler( t_0, T, x2_0, h ):
    # steps we can fit in
    N = int(T/h) 
    #
    x2 = x2_0 #initialising x2
    x3 = x3_0 #initialising x3
    t = t_0 #initialising time
    t_list = [t] #initialising list of times
    x2_list = [x2]
    for i in range(0,N):
        x2 = x2 + h*(np.sin(x3)-b*x2)
        t = t+h
        t_list.append(t)
        x2_list.append(x2)
    return(t_list,x2_list)

# getting values from euler fn
times_x2 = euler(t_0,T,x2_0,h)[0]
x2_val = euler(t_0,T,x2_0,h)[1]

#arranging the list of times and steps
tl_x2 = np.arange(0, T + h, h)



#for f(t,x3)
# euler method
def euler( t_0, T, x3_0, h ):
    # steps we can fit in
    N = int(T/h) # h is steps
    #
    x3 = x3_0 #initialising x3
    x1 = x1_0 #initialising x1
    t = t_0 # starting time
    t_list = [t]
    x3_list = [x3]
    for i in range(0,N):
        x3 = x3 + h*(np.sin(x1)-b*x3)
        t = t+h # next time step
        t_list.append(t)
        x3_list.append(x3)
    return(t_list,x3_list)

# getting values from euler fn
times_x3 = euler(t_0,T,x3_0,h)[0] 
x3_val = euler(t_0,T,x3_0,h)[1]
#arranging the list of times and steps
tl_x3 = np.arange(0, T + h, h)


# printing results for reference
print('\n----------------SOLUTION-----------------')
print('-----------------------------------------')  
##  
print('i \t ti \t x1_i \t x2_i \t x3_i') # printing header thing
for i in range(0,T+1):
    print(i,
          "\t",
          round(times_x1[i],4),
          "\t",round(x1_val[i],4),
          "\t",round(x2_val[i],4),
          "\t",round(x3_val[i],4),
          "\n")  
print('i \t ti \t x1_i \t x2_i \t x3_i') # printing header thing



 
# syntax for 3-D projection
fig = plt.figure()

ax = plt.axes(projection ='3d') # defining axes

#ax.set_xlim(-0.5,0.765)
#ax.set_ylim(-0.5, 0.765)
#ax.set_zlim(-0.5, 0.765)

# defining all 3 axis
x3 = np.array(x3_val)
x1 = np.array(x1_val)
x2 = np.array(x2_val)


#define axes for scale
x = (np.sin(x2)-b*x1)
y = (np.sin(x3)-b*x2)
z = (np.sin(x1)-b*x3)


c=  cm.viridis(times_x3) 


# plotting final behaviour #

#print(times_x3, "timesX3: ")
print("\n initial x1,x2,x3:  \n")
print(x[1],", ",y[1],", ",z[1],"\n")

print("\nfinal x1,x2,x3:  \n")
print(x[-1],", ",y[-1],", ",z[-1],"\n")

scatter = ax.scatter(x, y, z, c = c)

ax.plot3D(x, y, z, 'blue')
ax.set_title('Plot of Given Initial Value Problems Long Term Behaviour',pad=25)
#
#ax.set_box_aspect([1, 1, 1])
ax.set_xlabel('dx1 = sin(x2)-b*x1 ')
ax.set_ylabel('dx2 = sin(x3)-b*x2  ')
ax.set_zlabel('dx3 = sin(x1)-b*x3')

cbar = fig.colorbar(scatter, ax=ax, pad=0.2)
cbar.set_label('T Value (0 to {})'.format(T))  # Dynamic label
print("tlx3: ",tl_x3)
cbar.set_ticks([0, 1])  # Set colorbar ticks to show 0 and T
cbar.set_ticklabels([0, T])  # Label ticks explicitly

# adjustment option #plt.subplots_adjust(left=0.1, right=0.2, top=5, bottom=0)

ax.text(
    -1.7, 1, 0.2,
    f'Interval 3\n b = {b}\nStep size: h= {h}\nTime:,T={T}',
    fontsize=10,
    color='black',
             bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'),
)
# adjustment option #plt.subplots_adjust(left=0.25, right=0.85, top=0.85, bottom=0.15)

plt.show()
