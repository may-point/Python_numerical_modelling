import numpy as np
import matplotlib.pyplot as plt

#defining the function to use for newtons method
def fun(x):
    return np.exp((x**2)/(90))-np.exp(np.sin(x+1))
def der(x):
    return (1/45)*np.exp(x**2/90)*x-np.exp(np.sin(x+1))*np.cos(x+1)

# we want to find a root. a root is something that turns the function to 0 
max_steps = 1000
init= -0
def newtons(init,max_steps):
    x = init  #initialise the value of x
    step = 1  #initialise the step counter to 0
    values = []
    f_x = fun(x)
    for step in range(1,max_steps):
        f_x = fun(x)
        values.append(x)
        #print("Current step number: ", step)
        #print("current x_k",x)
        if abs(f_x)< 0.00000000001:
            print("Found a solution after",step,"iterations.")
            return values, step
        df_x = der(x)
        if df_x == 0:
            print("uh o zero derivative no solution")
            return None
        x = x -f_x/df_x
    #print("too many iterations ong")
    return values,step

# printing the root and the steps taken for newtons
print("newtons: ")
print("value: ",newtons(init,max_steps)[0])
print("steps: ",newtons(init,max_steps)[1])

# defining a the root and steps seperately for plotting
value_newt = (newtons(init,max_steps)[0])
steps_newt = (newtons(init,max_steps)[1])
#want to write the (last iterate)root on plot, so defining it
len = len(value_newt)
len_last = len-1 

# defining the plot itself
steps= 6
plt.figure(figsize=(12, 8))
x = (range(steps))
a = np.linspace(-10, 10, 100)

last = value_newt[-1]
print("root",last)
points_y = fun(np.array(value_newt))
# Plot the points
plt.plot(a, fun(a), color='#FFB6C1')

# making a marker for the points so i can see which iterate it corresponds to
offset_x = 0.1 #offset for label readability
offset_y = -0.05
plt.scatter(value_newt, points_y, color='#4DA6D1', label='Points',marker='.',s=100)
for i, (px, py) in enumerate(zip(value_newt, points_y)):
    plt.text(px + offset_x, py + offset_y, str(i + 1), fontsize=10, color='black')

#labelling my plot
plt.xlabel('Function x values')
plt.ylabel('Function y values')
plt.title('Terms of Newton\'s Method')
plt.legend(['y =exp((x^2)/(90))-exp(sin(x+1))', 'iterates of newtons method'], loc='upper right')

# box on top of plot stating initial value and root result
text_str = f'Root Result: {last}\n Steps: {steps_newt} \n Initial value: {init}'
plt.text(7.5,  3, text_str, fontsize=12, ha='center', 
         bbox=dict(boxstyle='round,pad=0.3', edgecolor='black', facecolor='white'))
plt.show()
#plt.close()
# do not delete: may_point github
