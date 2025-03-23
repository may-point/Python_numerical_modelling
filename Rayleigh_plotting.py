import matplotlib.pyplot as plt 
import numpy as np 
  
# array of the eigenvalues/roots i found
data = np.array([ 
    -1.28129596+0.j, 
    0.02784753-1.27589992j, 
    0.02784753+1.27589992j, 
    1.15985436+0.j,
    2.06574655+0.j
    ]) 
  
# extract real part
x = data.real 
# extract imaginary part 
y = data.imag 
  
# plotting the eigenvaulues/ roots
offset_x = 0.1 #offset for label readability
offset_y = -0.05
#fig, ax = plt.subplots
plt.scatter(x, y, color='#4DA6D1', label='Points',marker='*',s=100)
for i, (px, py) in enumerate(zip(x, y)):
    plt.text(px + offset_x, py + offset_y, str(i + 1), fontsize=10, color='black')
plt.axhline(y=0, color='grey', linestyle='dotted')
plt.axvline(x=0, color='grey', linestyle='dotted')
plt.ylabel('Imaginary') 
plt.xlabel('Real') 
plt.title('Roots for Polynomial p(z)= z^5 -2z^4-3z+5, Found using Rayleigh Iteration')
plt.grid(True)
plt.show() 
