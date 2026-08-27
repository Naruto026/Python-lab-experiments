#. Develop a program to generate Fibonacci sequence of length (N).Read N from the console. 
N=int(input("Enter the length of Fibonacci sequence: "))

a=0
b=1

for i in range (N):
    print(a , end=" ")
    a,b=b,a+b
    
    
    
