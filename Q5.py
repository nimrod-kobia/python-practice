def fact(z): #defining function fact for factorial
 if  z == 0:
    return 1 #factorial of 0 is 1
 else:
    return z * fact(z - 1) 

Num = fact(int(input("Input your number: "))) #Uses the received value to call the function

print("Factorial is :", Num) #Prints out the factorial


