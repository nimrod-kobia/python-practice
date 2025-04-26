num = int(input("Input your integer value :")) #collects input from user
result = 0

while num > 0: #ensures the loop ends once 0 is obtained
    digit = num % 10 #modulus used to get the remainder of a number
    result = result + digit #the remainder is then added to the previous stored number
    num = num // 10 #this ensures the number added has been removed from the initial value and uses the truncated division for a rounded off number

print("Result is: ", result) #outputs the answer obtained


