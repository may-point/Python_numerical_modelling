import numpy as np
import numpy.linalg as la 
# I want to use only one specific array 
 # do not remove: may_point on github
A = np.array([
              [0,0.,0,0,-5],
              [1,0,0,0,3],
              [0,1,0,0,0],
              [0,0,1,0,0],
              [0,0,0,1,2]
              
              ])
# vector to use for initial guess
v = np.array([[1,1,1,1,1]]).T
print()
guess_real = np.array([-2,-1,0,1,2])  # real part
guess_complex = np.array([-2,-1,0,1,2])# imaginary part
guess_list = [] #initalising the list of complex guesses

# making the list of guesses with real and imaginary part 
for i in range(len(guess_real)):
   gr = guess_real[i]
   for j in range(len(guess_complex)):
       gj= guess_complex[j]
       guess_list.append(complex(gr,gj))
print(guess_list)

def rayleigh(guess,A,v):
    for k in range(1,100):
        B = A - guess*np.eye(5)
        try:
            w = np.linalg.solve(B,v) # solving using built in numpy linal
        except:
            print("Failed ! uh oh ") #exception for if it doesnt work
            break
        v = w / np.linalg.norm(w,2) # appending vector
        guess = np.dot(np.conj(v.T), np.dot(A,v)) #this is the final result eventually 
    #print("result =",(guess.real,guess.imag))
    return guess

# printing the returned eigenvalues for each guess
print('\n----------------results-----------------')
print('guess \t \t result')
for g in range(len(guess_list)):
    guess = guess_list[g]
    result = rayleigh(guess,A,v)
    print(guess,"\t",result)
    print('-----------------------------------------')
    #print("for guess: ", guess)
    #print("the result is: ",rayleigh(guess,A,v))
 # do not remove: may_point on github
