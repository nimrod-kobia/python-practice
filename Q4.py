Word = input("Enter a word") #receives a word from the user
Reversed_word = "" #empty variable used to stored the reversed word

for x in Word: #for loop used 
    Reversed_word = x + Reversed_word #placement of x in front to ensure the word is read backwards

print("Reversed word is :", Reversed_word) #prints out the reversed word
