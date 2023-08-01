#Encryption Program
#Input a string, string returned will be encrypted

def encryption(string,shift):               #function
    cipher = " "
    for char in string:
        if char == " ":
            cipher=cipher+char
        elif char.isupper():
            cipher=cipher+chr((ord(char)+shift-65)%26+65)
        elif char.islower():
            cipher=cipher+chr((ord(char)+shift-97)%26+97)
        elif char.isalnum():
            cipher=cipher+chr((ord(char)+shift-33)%15+33)
        elif char.isnum:
            cipher=cipher+chr((ord(char)+shift-48)%10+48)
    return cipher  

text = input("Enter a message: ")                   #user input
s = int(input("Enter the distance value: "))        #shift key
print("The encoded message is : ",encryption(text,s))     #encrypted message output
