num = int(input("Input your number:")) #collects an input from the user and changes it to integer form

fact = 1 #Set it to one to avoid multiplication ny 0
if num == 0: #Factorial of 0 is 1
     print ("Factorial is ", 1)
else:
 for i in range(1, num + 1): #Starts the count at 1 and ends it at the input number thus the +1
    fact = fact * i
print("Factorial is", fact) #prints the answer
